from Processing import DataBrick,SplitData,DataPipeline,DataBrick,GetclosePrice
import numpy as np
from keras.models import Sequential
from keras.layers import Dense
from keras.layers import LSTM
from keras.layers import Dropout
import matplotlib.pyplot as plt
from NAV import Nav,Generate_nav
from keras.utils import to_categorical

def create_LSTM(X_train):
    # create and fit the LSTM network
    model = Sequential()
    model.add(LSTM(units=50, return_sequences=True, input_shape=(X_train.shape[1], X_train.shape[2])))
    model.add(Dropout(0.1))
    model.add(LSTM(units=50, return_sequences=True))
    model.add(Dropout(0.1))
    model.add(LSTM(units=25, return_sequences=True))
    model.add(Dropout(0.1))
    # model.add(LSTM(units=50))
    # model.add(Dropout(0.1))
    model.add(Dense(units=1, activation='sigmoid'))
    model.compile(optimizer='adam', loss='binary_crossentropy', metrics=['accuracy'])
    return model

def run_LSTM(X_train, X_test, y_train, y_test,symbol,price):
    y_train = to_categorical(y_train)
    y_test = to_categorical(y_test)
    LSTM=create_LSTM(X_train)
    history = LSTM.fit(X_train, y_train, epochs=100, batch_size=32)
    print(LSTM.summary())

    results =LSTM.evaluate(X_test, y_test, batch_size=32)
    print("test loss, test acc:", results)
    # summarize history for accuracy
    plt.plot(history.history['accuracy'], label='Train')
    plt.title('model accuracy')
    plt.ylabel('accuracy')
    plt.xlabel('epoch')
    plt.legend(['train', 'test'], loc='upper left')
    plt.show()

    prediction = LSTM.predict(X_test)
    y_prediction = prediction[:, -1, :]
    y_prediction = np.argmax(prediction, axis=1)
    print(y_prediction)
    NAV_history=Generate_nav(10000,symbol,price,y_prediction)