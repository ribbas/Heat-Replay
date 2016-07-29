from matplotlib.patches import Patch
import matplotlib.pyplot as plt
from numpy import mean
from seaborn import set as sns_set
from seaborn import boxplot, pairplot

sns_set(style="whitegrid", font_scale=1)

staticDir = '../../static/{file}.png'


def pairplotify(df):

    return pairplot(df)


def boxplotify(df, feature, path, title, save=True):

    fig, ax = plt.subplots(figsize=(12, 5))

    fig.suptitle(title, fontsize=20)

    boxplot(
        x=df['decade'], y=df[feature],
        hue=df['charted'],
        linewidth=2, ax=ax,
        palette={0: 'r', 1: 'g'}
    )

    yes = Patch(color='g', label='Yes')
    no = Patch(color='r', label='No')
    plt.legend(
        bbox_to_anchor=(1, 1), loc=2,
        ncol=1, shadow=True, title="Charted",
        handles=[yes, no]
    )

    if save:
        fig.savefig(staticDir.format(file=path))

    plt.show()


def meanLine(df, feature, title, path):

    fig, ax = plt.subplots(figsize=(12, 5))
    fig.suptitle(title, fontsize=20)

    year = set(df['year'])

    # Plot the mean of the feature
    x, y = zip(
        *sorted(
            (
                xVal, mean(
                    [
                        yVal for av, yVal in zip(
                            df['year'], df[feature]
                        ) if xVal == av
                    ]
                )
            ) for xVal in year
        )
    )

    plt.plot(x, y, 'r-')
    fig.savefig(staticDir.format(file=path))

    plt.show()
