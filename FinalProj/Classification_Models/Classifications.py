import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.svm import SVC
from sklearn.tree import DecisionTreeClassifier
from Processing import DataBrick,SplitData,DataPipeline,Scale,GetclosePrice
from sklearn.neural_network import MLPClassifier
from sklearn.naive_bayes import GaussianNB
from sklearn.gaussian_process import GaussianProcessClassifier
from sklearn.gaussian_process.kernels import RBF
from sklearn.neighbors import KNeighborsClassifier
from sklearn.ensemble import RandomForestClassifier, AdaBoostClassifier
from joblib import dump, load
import xlsxwriter
import matplotlib.pyplot as plt
from NAV import Nav,Generate_nav

symbol_list = ["BABA"]
#symbol_list = ["AAPL","TSLA","AMZN","GOOG","FB","NIO","BYND","FSLY","MRNA","BABA","BLNK"]
# interval_list = ["1m", "2m", "5m", "15m", "30m", "60m", "90m", "1h", "1d", "5d", "1wk", "1mo", "3mo"]
# period_list = ["1d", "5d", "1mo", "3mo", "6mo", "1y", "2y", "5y", "10y", "ytd", "max"]
period = "2y"
interval = "1d"
#size of databrick(eg.10days/hours as a databrick for training)
X_train_data = []
X_test_data = []
X_testc_data = []
Y_train_data = []
Y_test_data = []
Y_testc_data = []
# return a dictionary of stocks, and a dictionary of labels----{stock_symbol:stock_data;label symbol:label_data}
StockDict, LabelDict=DataPipeline(symbol_list,period,interval)
StockPriceDic=GetclosePrice(symbol_list,period,interval,1)
for symbol in StockDict:
    stock=StockDict[symbol]
    label=LabelDict[symbol]
    x_train, x_test, y_train, y_test = train_test_split(stock,label, test_size=0.2, shuffle=True)
    x_trainc, x_testc, y_trainc, y_testc = train_test_split(stock,label, test_size=0.2, shuffle=False)
    # Code for running the model for each stock
    X_train_data.append(x_train)
    Y_train_data.append(y_train)
    X_test_data.append(x_test)
    Y_test_data.append(y_test)
    X_testc_data.append(x_testc)
    Y_testc_data.append(y_testc)
#store names of the models
names = ["RBF SVM","Decision Tree","MLCP","Nearest Neighbors","Gaussian Process","Random Forest","AdaBoost","Naive Bayes"]\
#stores the models
classifiers = [SVC(kernel='rbf',gamma=2, C=0.5), 
               DecisionTreeClassifier(max_depth=1000), 
               MLPClassifier(alpha=1.1, max_iter=100000),
               KNeighborsClassifier(3),
               GaussianProcessClassifier(1.0 * RBF(1.0)),
               RandomForestClassifier(max_depth=1000, n_estimators=10, max_features=47),
               AdaBoostClassifier(),
               GaussianNB()
              ]
workbook = xlsxwriter.Workbook('result.xlsx')
worksheet = workbook.add_worksheet()
row = 1
for X_train, X_test, Y_train, Y_test, stock, X_testc, Y_testc in zip(X_train_data, X_test_data, Y_train_data, Y_test_data, symbol_list, X_testc_data, Y_testc_data):
    # iterate over classifiers
    column = 1
    print("\n")
    print(stock)
    NAV_history=Generate_nav(10000,stock,StockPriceDic,Y_test)
    worksheet.write(row, 0, stock)
    for name, clf in zip(names, classifiers):
        worksheet.write(0, column, name)
        clf.fit(X_train, Y_train)
        '''if name == "AdaBoost":
            #dump(clf, stock+'_'+name+'.joblib')
            prediction = clf.predict(X_test)
            NAV_history=Generate_nav(10000,stock,StockPriceDic,prediction)'''
        score = clf.score(X_testc, Y_testc)
        worksheet.write(row, column, score)
        print(name)
        prediction = clf.predict(X_testc)
        NAV_history=Generate_nav(10000,stock,StockPriceDic,prediction)
        print(score)
        column += 1
    row += 1
workbook.close()