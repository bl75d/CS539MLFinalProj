from Data.Collect import *
from Data.Process import *
from Data.File_IO import *
import Models.model as mdl
from Models.LSTM import *
from util import Color as c
import arg_parser

import numpy as np

np.set_printoptions(suppress=True, linewidth=150, edgeitems=3, precision=3)
print(c.RESET)

# parse args
parser = arg_parser.add_args()
args = parser.parse_args()

print(args)

if args.prepare:
    stockDict,labelDict = get_data(args.stocks, args.period, args.interval)
    X_train,X_test,Y_train,Y_test = process(stockDict,labelDict)
    Y_train = np.squeeze(Y_train)

    print("{}Displaying x_train data:{}".format(c.BLUE,c.RESET))
    print(X_train)
    print("{}Displaying x_train shape:{}".format(c.BLUE,c.RESET))
    print(X_train.shape)
    print("{}Displaying y_train data:{}".format(c.BLUE,c.RESET))
    print(Y_train)

    save_to_npy(X_train,"x_train")
    save_to_npy(X_test,"x_test")
    save_to_npy(Y_train,"y_train")
    save_to_npy(Y_test,"y_test")

if args.train:
    X_train = load_from_npy("x_train.npy")
    Y_train = load_from_npy("y_train.npy")

    print(X_train.shape)
    print(Y_train.shape)

    model= mdl.create_model(model_class=LSTM_Model,train_data_shape=X_train.shape)
    print(model.summary())
    # # modelpath="./model_checkpoint/"
    # mdl.load_trained(model, modelpath)
    mdl.compile_model(model)
    mdl.train(model, np.asarray(X_train), np.asarray(Y_train), num_epochs=500, save_period=100)
    res=mdl.evaluate(model, np.asarray(X_test), np.asarray(Y_test))


if __name__=="__main__":
    print("{}WARNING!\nPLEASE RUN THIS FILE LIKE THE FOLLOWING:\n\t{}python3 main.py --prepare\n\tpython3 main.py --train".format(c.YELLOW,c.RESET))