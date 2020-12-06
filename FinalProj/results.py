from Data.Collect import *
from Data.Process import *
from Data.File_IO import *
import Models.model as mdl
from Models.LSTM import *

from Results.Generate_Accuracy_Plots import *
from util import Color as c

import numpy as np
import pandas as pd
import collections
import sys
import glob
import argparse

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

if args.directories == []:
    args.directories = ["model_checkpoints"]

if args.train:
    # for d in args.directories:
    d = args.directories[0]
    training_accuracy("{}/Log_Train_Statistics.csv".format(d))

    sys.exit(0)
    
if args.test:
    # for d in args.directories:
    d = args.directories[0]
    training_args = pickle.load(open("{}/training_args.pkl".format(d), "rb"))


    sys.exit(0)