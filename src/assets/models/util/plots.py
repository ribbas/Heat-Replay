import matplotlib.pyplot as plt
from seaborn import set as sns_set
from seaborn import boxplot, pairplot

sns_set(style="whitegrid", font_scale=1)

staticDir = '../../static/{file}.png'


def pairplotify(df):

    return pairplot(df)


def boxplotify(df, feature, path, title, save=True):

    fig, ax = plt.subplots(figsize=(12, 5))

    ax.set_title(title)

    boxplot(
        x=df['decade'], y=df[feature],
        hue=df['charted'],
        linewidth=2, ax=ax, palette={0: 'r', 1: 'g'}
    )

    if save:
        fig.savefig(staticDir.format(file=path))

    plt.show()
