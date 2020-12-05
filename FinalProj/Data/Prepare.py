import numpy as np

    for symbol in StockDict:
        stock=StockDict[symbol]
        label=LabelDict[symbol]
        X_train, X_test, y_train, y_test=SplitData(stock,label,size)

        # Code for running the model for each stock
        print(X_train.shape)
        print(y_train.shape)