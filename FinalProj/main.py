from Data.Collect import *
from Data.Process import *
from Data.File_IO import *
import Models.model as mdl
from Models.LSTM import *
from util import Color as c
import arg_parser

import numpy as np
import collections
import sys
import pickle

def main(args):
    if args.prepare:
        if args.stocks == []:
            args.stocks = ["AAPL"]

        stockDict,labelDict = get_data(args.stocks, args.period, args.interval)
        X_train,X_test,Y_train,Y_test = process(stockDict,labelDict,args.serieslength)
        Y_train = np.squeeze(Y_train)
        Y_test = np.squeeze(Y_test)

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

        return X_train,X_test,Y_train,Y_test

    if args.analyze:
        X_train = load_from_npy("x_train.npy")
        Y_train = load_from_npy("y_train.npy")
        X_test = load_from_npy("x_test.npy")
        Y_test = load_from_npy("y_test.npy")

        train_counter = collections.Counter(Y_train)
        test_counter = collections.Counter(Y_test)

        train_percent = [(i, train_counter[i] / len(Y_train) * 100.0) for i in train_counter]
        train_percent.sort()
        test_percent = [(i, test_counter[i] / len(Y_test) * 100.0) for i in test_counter]
        test_percent.sort()
        
        print("{}Label Distribution:{}".format(c.BLUE,c.RESET))
        # print("Train:", train_counter)
        print("Train Data:")
        [print("\tLabel: {}. Percent: {:.1f}%".format(i, p)) for i,p in train_percent]
        # print("Test:", test_counter)
        print("Test Data:")
        [print("\tLabel: {}. Percent: {:.1f}%".format(i, p)) for i,p in test_percent]

        return train_percent, test_percent

    if args.train:
        X_train = load_from_npy("x_train.npy")
        Y_train = load_from_npy("y_train.npy")

        print(X_train.shape)
        print(Y_train.shape)

        model= mdl.create_model(
            model_class=LSTM_Model,
            train_data_shape=X_train.shape,
            layerwdith=args.layer_width
            )

        print(model.summary())
        mdl.compile_model(model)

        pickle.dump(args, open("{}/args_data.pkl".format(args.dir), "wb"))

        mdl.train(
            model, 
            np.asarray(X_train), 
            np.asarray(Y_train),
            directory=args.dir, 
            num_epochs=args.epochs,
            batch_size_divisor=args.batch_size_divisor,
            save_period=args.save_period
            )

    if args.eval:
        X_test = load_from_npy("x_test.npy")
        Y_test = load_from_npy("y_test.npy")

        model = mdl.create_model(
            model_class=LSTM_Model,
            train_data_shape=X_test.shape,
            layerwdith=args.layer_width
            )

        print(model.summary())
        mdl.load_trained(model,args.dir+args.model)
        mdl.compile_model(model)
        res=mdl.evaluate(model, np.asarray(X_test), np.asarray(Y_test))
        return res

    if args.predict:
        pass

if __name__=="__main__":

    # parse args
    parser = arg_parser.add_args()
    args = parser.parse_args()
    print("{}WARNING!\nPLEASE RUN THIS FILE LIKE THE FOLLOWING:\n\t{}python3 main.py --prepare\n\tpython3 main.py --train".format(c.YELLOW,c.RESET))
   
    np.set_printoptions(suppress=True, linewidth=150, edgeitems=3, precision=3)
    print(c.RESET)

    print(args)
    main(args)