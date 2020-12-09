# Stock Market Trading Thing


# Background

The trading process has evolved massively, investors and traders have to employ sophisticated parameters and combinations of factors to make decisions on a volatile market. Social sentiment scores, technical indicators and fundamental information, considering and analyzing those factors makes investing today more complicated than ever. 

Machine learning has the potential to ease the whole process by analyzing large chunks of data, spotting significant patterns and generating a single output that navigates traders towards a particular decision based on predicted asset prices. With the help of machine learning, traders can analyze data points that are present very fastly and accurately, and learn trends and form patterns at higher speed, which are generally used for smart trading.

# Tools & Methodology
## Tools
Python is an efficient way to quickly code up models that is widely supported with different capabilities. Numpy is great for mathematical operations and since most of this project will require large tables of data to have numeric computations. Pandas is useful for data analysis while deciding and analyzing feature importance and feature engineering. Tensorflow is a machine learning framework for developing models that can be trained and tested with an easy to use API while still allowing the user to deeply modify.

## Existing Method 
here have been many learning models trying to predict the stock market, thus making money from it. However, many of them either focus too much on the price while the price itself is affected by too many factors that would result in overfitting or lack of accuracy, or disregard the buy and sale procedure that makes the model useless (Dongdong, etc). In our case, we will
combine the stock purchasing simulation, building a classifier that can feed back the best decisions (sell, buy, keep). Also, the starting stock or starting asset will be given, and then we will keep tracking it’s value so that we can get a better evaluation for the model. There have been previous works that used several models and tried to get the best one. We will do this as well. However, we would focus more on the LSTM.
## Unique Challenge
The difference between our model and those most common models in the world is that our output is directly the choice or operations we are going to do with our asset. As a result, we can more easily evaluate the efficiency or the performance of the model. Compared to those models, our models can give more visual results, people can directly see how their assets will change, thus can be more persuasive.

# Stocks Picked
## Stock Trends of 11 Picked Stocks
The picked eleven stocks are: "AAPL","TSLA","AMZN","GOOG","FB","NIO","BYND","FSLY","MRNA","BABA","BLNK".
## Relative stable Stocks
"AAPL", "TSLA", "AMZN", "GOOG", and "FB" have relative stable stock price trends. They are big Internet companies and their stock price keeps rise most of the time.
### Flat and Increase Stocks
"NIO", "MRNA" and "BLNK" has a very stable trend in the beginning, however, their price increased dramatically in the latter days.
### Relative Unstable Stocks
"BYND", "FSLY" and "BABA" have a relatively unstable trend. Their price keeps going up and down and it would be really hard to correctly calculate them.


# Methods

## Data Prepocessing

### Collection
To accomplish the task, we will first perform data mining with the Finnhub API. The API allows for straightforward collection of historical stock data at different time intervals. For example, we could collect minute, hourly, daily stock data based on the timeframe we wish to use. This will likely affect the model’s responsiveness to slight market variations and can be a component that we test to compare results. From this data, we can perform various other feature extraction techniques. One such feature is a Simple Moving Average (SMA), a metric used by traders on Wall Street. To add this feature, we select a window size (n) as a parameter and average the stock price over the last n quotes. This methodology can be applied to a variety of indicators detailed further below.
### Feature Engineering


### Labeling
The goal of the project is to apply machine learning techniques on stock history data to generate instructions of trading strategy for the future, the instructions are basically indicators for users to either buy or sell a stock with confidence. Unlike other machine learning on stock projects that use stock price as the target for model training and testing, this project takes the indicators as the target. Although these are implicit in the stock data, it is impossible to acquire such information from the dataset directly, thus, algorithms that can generate target labels from the data set are necessary.
As the explanation of trading indicators mentioned above, the labels are set to be three signals, buy, hold, and sell, which indicates the trading strategy for the current position. There are 2 major methods for generating labels that turn out to be practical.
The first one is calculated based on price change in percentage between two data, take three-quarters of the positive price change as buy, three-quarters of the negative price change as sell, the rest of the data will be labeled as a hold. The labels for buy, sell, and hold are relatively evenly distributed, however, it may not reflect the buy and sell position very accurately.
The second one uses two features of the stock called moving average convergence divergence(MACD) and relative strength index(RSI), it applies Savitzky–Golay filter on local MACD peaks and valleys, user can choose the window size of the filter and whether apply RSI to generate a more strict and accurate rule on labeling, it heavily affects the distribution of labels, thus, the label may not evenly be distributed, it has a huge impact on the training process.

### Evaluation: Net Asset Value
The project avoids predicting the price of the stocks, instead, it gives predictions on trading strategy for the future, it is more like a classification problem. However, the generated label is not 100% strict, in fact, it is a fuzzy signal for trading, for example, if the price increase is smaller than a threshold, it will predict as hold even if the ground truth indicates that it is a buy signal, but such labeling method is more practical in trading especially day trading since it is impossible for traders to do extreme high-frequency trading. Indeed, it is important to generate a method to evaluate the performance of each model which can track the result of trading operations followed by prediction given by the model, thus, the net asset value (NAV) class is created. NAV is used to track the portfolio change along the time with an initial fund and a series of trading operations followed by the predictions, finally, it clearly shows whether the net asset value increases, in other words, whether the model helps the users make money.
## Models
### Simple Classification Models
In this part, we picked eight models from all the classification models in the sklearn package and tried to fit single day data to it.
#### Models picked
RBF SVM, Decision Tree, MLCP, Kneighbors, Gaussian Process, Random Forest, AdaBoost, Gaussian Naive Bayes
#### Training Data
We took two years of data for each day and using the balanced label method to build the dataset. And we split them with a training-testing ratio of 4:1.
There are two different split settings, thus two different tests.
##### Continuous Splite
In this test, we took the first 75 percent of the data as training sets without shuffling it. In this case, when the models are trained, there is still some time continuity inside the training dataset. This split has a problem, when the training period stock trend varies a lot with the testing days, the model can be very inaccurate.
##### Shuffled Splite
In this test, even though we still picked out 75 percent days as the training dataset, but the data was shuffled before taking into use. Thus, the time continues day with each day would be broken. However, to calculate the NAV, we are still going to use the continuous split testing datas. Or the NAV won't make any sense.
#### Parameter settings
For Kneighbors, we are using k = 3, since we only have three labels. For the SVM, we are using C = 0.5, in order to make the model more balanced. For the Decision Tree, Random Forest, and MLCP, we gave them a very large max depth and max iteration to make sure that they can find the best result. And we give max_features = 47 to Random Forest since we only have that much.

### LSTM
The Long Short-Term Memory model below has a layer width of 60 and two separate dropouts. Note that there is a total of 3,513 trainable parameters for the model.
```
Model: "sequential"
____________________________________________________________
Layer (type)        Output Shape                 Param #
____________________________________________________________
lstm (LSTM)         (None, 10, 15)               2340
____________________________________________________________
time_distributed    (TimeDistri (None, 10, 15)   240
____________________________________________________________
time_distributed_1  (TimeDist (None, 10, 15)     240
____________________________________________________________
dropout (Dropout)   (None, 10, 15)               0
____________________________________________________________
time_distributed_2  (TimeDist (None, 10, 15)     240
____________________________________________________________
flatten (Flatten)   (None, 150)                  0
____________________________________________________________
dropout_1 (Dropout) (None, 150)                  0
____________________________________________________________
dense_3 (Dense)     (None, 3)                    453
____________________________________________________________
Total params: 3,513
Trainable params: 3,513
Non-trainable params: 0
____________________________________________________________________
```

### CNN
![image](https://github.com/bl75d/CS539MLFinalProj/blob/master/FinalProj/Jeff/CNN_parameter.png)

We have built a CNN model for predict 1 day's stock price based on its previous 1 year's stock price.

Stock price data was reshaped as images in shape of 12*21, which represented stock price of a whole year with 12 months and 21 transaction days each month.

Apple company's stock price data in past 40 years was resampled into 6879 (instances) by moving all pixels forward at step of 1.

![image](https://github.com/bl75d/CS539MLFinalProj/blob/master/FinalProj/Jeff/CNN_NAV.png)

We have attained an accuracy of 39.2%.

However, in NAV transaction simulation, we have made 90% profits at the 90th day and 50% at the end of 100 days.

# Results

## Simple Classification models
### Scores of Eleven Stocks and Using continuly Splite
The table below shows the scores of all the models under all the stocks using continues split.
![Con-split](https://user-images.githubusercontent.com/48306738/101673889-c0eeab80-3a25-11eb-88cb-691c61f02cc2.png)
### Scores of Eleven Stocks and Eight Models using Shuffled Splite
The table below shows the scores of all the models under all the stocks using shuffled split.
![random-split](https://user-images.githubusercontent.com/48306738/101673961-dbc12000-3a25-11eb-82a6-6dc521a1414a.png)
### NAV of All Models based on "BABA" Stock Using Shuffled Splite
In this part of testing results, we only picked the most significant stock "BABA", which is increasing in a relatively unstable way.
#### NAV for models without shuffle
![CON-NAV1](https://user-images.githubusercontent.com/48306738/101701271-95cb8280-3a4c-11eb-9ec7-ad6d56e5d59d.png)
![CON-NAV2](https://user-images.githubusercontent.com/48306738/101701276-96fcaf80-3a4c-11eb-9c4f-02545ffc5634.png)
#### NAV for models without shuffle
![RAN-NAV1](https://user-images.githubusercontent.com/48306738/101701282-995f0980-3a4c-11eb-9771-e5543526c6d8.png)
![RAN-NAV2](https://user-images.githubusercontent.com/48306738/101701287-9a903680-3a4c-11eb-9a06-90196e9834be.png)
## CNN

## LSTM

# Discussion

## What can we learn from simple classifications
### The Time continuty
The time continuety doesn't effect most of the models that much. As a matter of fact, all the mathmatical models are tend to label all the data as hold, so that the accuracy could be better. While for other models, it can even have some nagetive effect. The ones that was effected the most is Naive Bayes, after we use random split, the rsults of it became much better. In addition, AdaBoost has a very balanced and stable performance. No matter whether using random split or not.
### The NAV performance
From the tables and the NAV figures, we can clear tell that the accuracy of the model, or the score of the mdoel does not have anything to do with NAV. The NAV is about making right decision at a right time. It seems that the models using random split data have a better performance, and since the data are shuffled, they can perfectly solve those flat first, unstable later trend models.
## CNN and LSTM

# Conclusion
We did something
