from sklearn.preprocessing import MinMaxScaler


def preprocessing(df):
    sc = MinMaxScaler(feature_range=(0, 1))
    scaled_df = sc.fit_transform(df)

    return scaled_df