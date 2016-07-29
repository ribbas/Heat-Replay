from re import compile

import matplotlib.pyplot as plt
from matplotlib import cm
from numpy import linspace
from pandas import get_dummies, DataFrame


def getBestParam(path):

    paramPat = compile('\{(.*?)\}')

    with open('../params/' + path, 'r') as file:
        return paramPat.findall(
            file.read()
        )[-1].partition(':')[-1].strip()


def sentiment(row):

    if row['sentiment'] <= -0.5:
        return -1
    elif -0.5 < row['sentiment'] < 0.5:
        return 0
    elif row['sentiment'] >= 0.5:
        return 1


def dummyfy(df, feature, y):

    if feature in df.columns:
        # get dummy variables
        df_new = df.join(get_dummies(df[feature], prefix=feature))
        # remove column
        df_new.drop([feature], axis=1, inplace=True)

    # list of features to use to build model
    features = [i for i in df_new.columns if feature + '_' in i]
    features += [y]
    print features
    return df_new, features


def plotFeature(df_new, features, prob, xLabel, yLabel, labels):

    ax = plt.subplot(111)
    colors = [cm.jet(x) for x in linspace(0, 1, len(labels))]
    for i, v in enumerate(labels):
        df_new[df_new[features[i]] == 1].plot(
            xLabel, prob, color=colors[i],
            kind='scatter', label=v, ax=ax
        )

    ax.set(
        title='Probability of Charted\n Based on ' +
        xLabel.capitalize() + ' and ' + yLabel.capitalize()
    )
    plt.legend(loc='upper right')
