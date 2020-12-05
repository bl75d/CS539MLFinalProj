# built-in imports

# Data structure imports

# tensorflow imports
import tensorflow as tf
from tensorflow.python.keras.layers import Dense, Dropout, Flatten, LSTM, TimeDistributed
from tensorflow.python.keras.models import Sequential

# custom imports
from Models.Abstract import Abstract_Model

class LSTM_Model(Abstract_Model):
    def __init__(self, kwargs):
        """
        Set up LSTM Model specifics. Calls parent method to setup common variables.

        Args:
            kwargs (dict): key,value pairs of all variables
        """

        super().__init__(kwargs)

    def generate(self):
        """
        Generate function of the subclass overriding the abstract method.

        Returns:
            tf.python.keras.models.*: Model that is generated per structure.
        """

        shape = self.train_data_shape[1:]

        print(shape)

        model = Sequential()
        model.add(LSTM(self.layer_width, input_shape=shape, return_sequences=True, go_backwards=False))
        model.add(TimeDistributed(Dense(self.layer_width, activation='relu')))
        model.add(TimeDistributed(Dense(self.layer_width, activation='relu')))
        model.add(Dropout(self.dropout_rate/2))
        model.add(TimeDistributed(Dense(self.layer_width, activation='relu')))
        model.add(Flatten())
        model.add(Dropout(self.dropout_rate))
        model.add(Dense(3, activation="softmax"))
        
        return model