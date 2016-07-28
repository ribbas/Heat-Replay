from re import compile

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
        self.__clfs = {}
        self.bestClf = ()

    def initModels(self):

        self.__clfs = {
            'knn': neighbors.KNeighborsClassifier(),
            'lm': linear_model.LogisticRegression(),
            'tm': tree.DecisionTreeClassifier(),
            'rf': ensemble.RandomForestClassifier()
        }

    def defaultParams(self):

        print "Clasifiers with default parameters:\n"

        for clfName, clf in self.__clfs.items():

            clfName = ' '.join(
                splitByCaps.findall(
                    str(clf).partition('(')[0]
                )[:2]
            )

            # Train clf on training set
            print clfName
            clf.fit(self.X_train, self.y_train)

            print "Accuracy: {:.3f}".format(
                clf.score(self.X_test, self.y_test)
            )
            print 'ROC AUC: {:0.3f}\n'.format(
                roc_auc_score(
                    self.y_test, clf.predict_proba(self.X_test)[:, 1]
                )
            )

    def initGridSearches(self):

        self.gs = {clfName: None for clfName in self.__clfs.keys()}

        # Set list of values to grid search over
        n = [2**i for i in range(-10, 11)]
        intN = n[len(n) / 2:]
        intN = [int(i) for i in intN]

        params = {
            'knn': {'n_neighbors': intN},
            'lm': {'C': n},
            'tm': {'max_depth': intN},
            'rf': {'n_estimators': intN}
        }

        # Perform grid search using list of values

        for clf, obj in params.items():

            self.gs[clf] = GridSearchCV(
                estimator=self.__clfs[clf],
                param_grid=obj
            )

    def gridSearch(self):

        print "Grid searching for best parameters:\n"

        maxAccuracy = 0

        for grid, clf in zip(self.gs, self.__clfs):

            self.gs[grid].fit(self.X_train, self.y_train)

            clfName = ' '.join(
                splitByCaps.findall(
                    str(self.__clfs[grid]).partition('(')[0]
                )[:2]
            )

            print clfName

            # Get best value to use
            print "Best Params:", self.gs[grid].best_params_
            self.__bestParams[grid] = self.gs[grid].best_params_

            print "Accuracy of current clf: {:0.3f}".format(
                self.__clfs[grid].score(self.X_test, self.y_test)
            )

            print "Accuracy using best param: {:0.3f}\n".format(
                self.gs[grid].best_score_
            )

            if self.gs[grid].best_score_ > maxAccuracy:
                maxAccuracy = self.gs[grid].best_score_
                self.bestClf = (clfName, self.gs[grid].best_params_)

    def updateParams(self):

        self.__clfs['knn'].set_params(
            n_neighbors=self.__bestParams['knn'].values()[0])

        self.__clfs['lm'].set_params(
            C=self.__bestParams['lm'].values()[0]
        )
        self.__clfs['tm'].set_params(
            max_depth=self.__bestParams['tm'].values()[0]
        )
        self.__clfs['rf'].set_params(
            n_estimators=self.__bestParams['rf'].values()[0]
        )

    def getBestParams(self, path):

        print 'Best clf is {} with {}'.format(
            self.bestClf[0],
            self.bestClf[-1])

        with open('../params/' + path, 'w') as file:
            file.write(
                str(self.bestClf[0]) + ' : ' + str(self.bestClf[-1])
            )

    def initProc(self):

        self.initModels()
        self.initGridSearches()

    def plotModels(self):

        for clf in self.__clfs:

            self.__clfs[clf].fit(self.X_train, self.y_train)

            clfName = ' '.join(
                splitByCaps.findall(
                    str(self.__clfs[clf]).partition('(')[0]
                )[:2]
            )

            try:
                # Plot importances for all features
                features = self.X.columns
                feature_importances = self.__clfs[clf].feature_importances_

                print clfName
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
                print clfName, 'doesn\'t have feature importance.\n'
                continue
