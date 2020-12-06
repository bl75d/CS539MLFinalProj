from Results.Generate_Accuracy_Plots import *
from util import Color as c
from main import main

import numpy as np
import pandas as pd
import collections
import sys
import glob
import argparse
import os

def add_args():
    parser = argparse.ArgumentParser(description='Task')
    parser.add_argument('-t', '--train', action='store_true')
    parser.add_argument('-T', '--test', action='store_true')
    parser.add_argument('-d', '--directories',default=[], action='append', metavar='directories', type=str)
    # parser.add_argument('--series_length',default=10, metavar='series_length', type=int)
    return parser

np.set_printoptions(suppress=True, linewidth=150, edgeitems=3, precision=3)
print(c.RESET)

# parse args
parser = add_args()
args = parser.parse_args()
print(args)

if args.directories == []:
    args.directories = ["model_checkpoints/"]

if args.train:
    # for d in args.directories:
    d = args.directories[0]
    training_accuracy("{}/Log_Train_Statistics.csv".format(d))

    
if args.test:
    # for d in args.directories:
    d = args.directories[0]
    training_args = pickle.load(open("{}/args_data.pkl".format(d), "rb"))
    training_args.train = False
    training_args.eval = True
    training_args.verbose = 0

    data = []
    
    for path in map(os.path.basename, glob.glob('{}/*.index'.format(training_args.dir))):
        path = path[:-6]
        
        training_args.model = path
        result = main(training_args)
        print(result)

        data.append(result)

    print("Done with Loop!")
    testing_accuracy(data, num_epochs=training_args.epochs)

print("Done!")