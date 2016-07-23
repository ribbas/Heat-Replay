from pandas import read_csv


def initSet():

    # URL to dataset
    dataUrl = 'https://raw.githubusercontent.com/kug3lblitz/Heat-Replay/' \
        + 'master/src/data/final/final.csv'

    # Load the dataset
    return read_csv(dataUrl)


def wrangle(df='', dropList=[], removeList=[]):

    # Completely drop from set
    df.drop(dropList, axis=1, inplace=True)

    # Set features to use
    features = list(df)

    for col in removeList:
        try:
            features.remove(col)
        except ValueError:
            print col, 'doesn\'t exist'
            continue

    return df, features
