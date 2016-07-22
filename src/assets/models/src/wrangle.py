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
