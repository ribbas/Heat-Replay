from re import compile

from numpy import power
from sklearn.grid_search import GridSearchCV
from sklearn.metrics import roc_auc_score
from sklearn import neighbors, linear_model, tree, ensemble

splitByCaps = compile('[A-Z][^A-Z]*')

BEST_PARAMS = 'best_params.txt'


class Models():

    def __init__(self, X_train, X_test, y_train, y_test):

        # Create separate training and test sets with 60/40 train/test split
        self.X_train, self.X_test, self.y_train, self.y_test = \
            X_train, X_test, y_train, y_test

        self.__bestParams = {}
        self.__models = {}

    def initModels(self):

        self.__models = {
            'knn': neighbors.KNeighborsClassifier(),
            'lm': linear_model.LogisticRegression(),
            'tm': tree.DecisionTreeClassifier(),
            'rf': ensemble.RandomForestClassifier()
        }

        return self.__models

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
        n = [power(2, i + 1) for i in range(10)]

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

    def getBestParams(self):

        return self.__bestParams
