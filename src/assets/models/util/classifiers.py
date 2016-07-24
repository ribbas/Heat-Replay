from re import compile

from numpy import power
from pandas import DataFrame
from seaborn import barplot, plt
from sklearn.cross_validation import train_test_split
from sklearn.grid_search import GridSearchCV
from sklearn.metrics import roc_auc_score
from sklearn import neighbors, linear_model, tree, ensemble

splitByCaps = compile('[A-Z][^A-Z]*')


class Classifiers():

    def __init__(self, X, y):

        self.X = X
        self.y = y

        # Create separate training and test sets with 60/40 train/test split
        self.X_train, self.X_test, self.y_train, self.y_test = \
            train_test_split(
                X, y, test_size=0.4, random_state=42
            )

        self.__bestParams = {}
        self.__models = {}
        self.bestModel = ()

    def initModels(self):

        self.__models = {
            'knn': neighbors.KNeighborsClassifier(),
            'lm': linear_model.LogisticRegression(),
            'tm': tree.DecisionTreeClassifier(),
            'rf': ensemble.RandomForestClassifier()
        }

    def defaultParams(self):

        print "Models with default parameters:\n"

        for modelName, model in self.__models.items():

            modelName = ' '.join(
                splitByCaps.findall(
                    str(model).partition('(')[0]
                )[:2]
            )

            # Train model on training set
            print modelName
            model.fit(self.X_train, self.y_train)

            print "Accuracy: {:.3f}".format(
                model.score(self.X_test, self.y_test)
            )
            print 'ROC AUC: {:0.3f}\n'.format(
                roc_auc_score(
                    self.y_test, model.predict_proba(self.X_test)[:, 1]
                )
            )

    def initGridSearches(self):

        self.gs = {modelName: None for modelName in self.__models.keys()}

        # Set list of values to grid search over
        n = [power(2, i) for i in range(11)]

        params = {
            'knn': {'n_neighbors': n},
            'lm': {'C': n},
            'tm': {'max_depth': n},
            'rf': {'n_estimators': n}
        }

        # Perform grid search using list of values

        for model, obj in params.items():

            self.gs[model] = GridSearchCV(
                estimator=self.__models[model],
                param_grid=obj
            )

    def gridSearch(self):

        print "Grid searching for best parameters:\n"

        maxAccuracy = 0

        for grid, model in zip(self.gs, self.__models):

            self.gs[grid].fit(self.X_train, self.y_train)

            modelName = ' '.join(
                splitByCaps.findall(
                    str(self.__models[grid]).partition('(')[0]
                )[:2]
            )

            print modelName

            # Get best value to use
            print "Best Params:", self.gs[grid].best_params_
            self.__bestParams[grid] = self.gs[grid].best_params_
            print "Accuracy of current model: {:0.3f}".format(
                self.__models[grid].score(self.X_test, self.y_test)
            )
            print "Accuracy using best param: {:0.3f}\n".format(
                self.gs[grid].best_score_
            )

            if self.gs[grid].best_score_ > maxAccuracy:
                maxAccuracy = self.gs[grid].best_score_
                self.bestModel = (modelName, self.gs[grid].best_params_)

    def updateParams(self):

        self.__models['knn'].set_params(
            n_neighbors=self.__bestParams['knn'].values()[0])

        self.__models['lm'].set_params(
            C=self.__bestParams['lm'].values()[0]
        )
        self.__models['tm'].set_params(
            max_depth=self.__bestParams['tm'].values()[0]
        )
        self.__models['rf'].set_params(
            n_estimators=self.__bestParams['rf'].values()[0]
        )

    def getBestParams(self, path):

        print 'Best model is {} with {}'.format(
            self.bestModel[0],
            self.bestModel[-1])

        with open('../params' + path, 'w') as file:
            file.write(
                str(self.bestModel[0]) + ' : ' + str(self.bestModel[-1])
            )

    def initProc(self):

        self.initModels()
        self.initGridSearches()

    def plotModels(self):

        for model in self.__models:

            self.__models[model].fit(self.X_train, self.y_train)

            modelName = ' '.join(
                splitByCaps.findall(
                    str(self.__models[model]).partition('(')[0]
                )[:2]
            )

            try:
                # Plot importances for all features
                features = self.X.columns
                feature_importances = self.__models[model].feature_importances_

                print modelName
                features_df = DataFrame(
                    {
                        'Features': features,
                        'Importance Score': feature_importances
                    }
                )

                features_df.sort_values(
                    'Importance Score', inplace=True, ascending=False)

                barplot(y='Features', x='Importance Score', data=features_df)
                plt.show()

            except:
                print modelName, 'doesn\'t have feature importance.\n'
                continue
