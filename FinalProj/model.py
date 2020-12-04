# built-in imports
from contextlib import redirect_stdout
import os

# Data processing imports
import numpy as np

# tensorflow imports
import tensorflow as tf
from tensorflow.python.keras.layers import Dense, Dropout, Flatten, LSTM, TimeDistributed
from tensorflow.python.keras.models import Sequential

# custom imports
from Models.LSTM import LSTM_Model

def create_model(model_class=LSTM_Model, **kwargs):
    """Helper function to generate the model. Calls the specific model function for the generation.

    Note:
        The returned model is not compiled yet.

    Args:
    model_class (Class): class of model the model to generate. Must have a generate method.
    **kwargs: keyword arguments such as the following. Includes model specific arguments.
        train_data_shape (tuple): The shape of the training data.
        dropout (double): fractional percent of nodes in some layers to leave out.
        layer_width (int): number of nodes wide to make the common layer.

    Returns:
        tf.python.keras.models.*: model that is created.
    """
    
    model = model_class(kwargs).generate()
    
    return model

def load_trained(model, filepath):
    """Load a previously trained model from a checkpoint.

    Args:
        model (tf.python.keras.models): model to add the weights to which must have same layout 
            as the trained model.
        filepath (str): file to load checkpoint data from (has .ckpt on the end).
    """

    model.load_weights(filepath)

def compile_model(model):
    """Compile the model that is loaded This can be called right after generating model, however, 
    if you wish to load weights, do so before calling this method.

    Args:
        model (tf.python.keras.models): generated model with optionally loaded weights to be 
            compiled.
    """

    model.compile(loss='categorical_crossentropy',
                  optimizer='adam', metrics=['accuracy', 'mse'])

def convert_to_tensor(array):
    return tf.convert_to_tensor(array, np.float32)

def train(model, train_x, train_y, directory="model_checkpoint/", num_epochs=1000, save_period=50):
    """Train on the model with the provided training features and labels.

    Note:
        The directory path must already exist.

    Args:
        model (tf.python.keras.models): model to use for training.
        train_x (tf.Tensor): contains a 2d numpy array as the feature vectors.
        train_y (tf.Tensor): contains a 1d numpy array as the label vectors.
        directory (str, optional): the directory to save model weights. Defaults to 
            "model_checkpoint/".
        num_epochs (int, optional): number of epochs to train for. Defaults to 1000.
        save_period (int, optional): the frequency in epochs of saving weights. Defaults to 50.
    """

    print("----train----")

    # Include the epoch in the file name (uses `str.format`)
    checkpoint_path = "{dir}cp-{epoch}.ckpt".format(dir=directory, epoch="{epoch:04d}")
    description_path = "{dir}Model_Description.log".format(dir=directory)
    statistics_path = "{dir}Log_Train_Statistics.csv".format(dir=directory)

    if not os.path.exists(directory):
        os.makedirs(directory)

    with open(description_path, 'w') as f:
        with redirect_stdout(f):
            model.summary()

    # Create a callback that saves the model's weights
    cp_callback = tf.keras.callbacks.ModelCheckpoint(
        filepath=checkpoint_path,
        verbose=1,
        save_weights_only=True,
        period=save_period
        )

    save_train_info = tf.keras.callbacks.CSVLogger(
        statistics_path,
        separator=",",
        append=False
        )

    # run the training
    model.fit(
        train_x,
        train_y,
        epochs=num_epochs,
        batch_size=64,
        steps_per_epoch=1,
        callbacks=[cp_callback, save_train_info]
        )

def evaluate(model, test_x, test_y):
    """Evaluate the model on test data.

    Args:
        model (tf.python.keras.models): trained model to evaluate.
        test_x (np.array): 2d array as the feature vector.
        test_y (np.array): 1d array as label vector.
    """

    res = model.evaluate(test_x,  test_y, batch_size=64, verbose=1)
    return res

def predict(model, test_x):
    """predict on the test feature vector
    
    Args:
        model (tf.python.keras.models): trained model to use for predictions.
        test_x (np.array): 2d numpy array of test feature vector.
    
    Returns:
        list: predictions for each item in test feature vector
    """

    # make predictions for test data
    pred_y = model.predict(test_x)
    return pred_y

