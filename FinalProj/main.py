from Data.Collect import *
from Data.Process import *

import numpy as np

stockDict,labelDict = get_data()
X_train,X_test,Y_train,Y_test = process(stockDict,labelDict)

print(X_train)
print(X_train.shape)