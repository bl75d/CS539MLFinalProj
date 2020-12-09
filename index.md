# Stock Market Trading Thing

General Purpose


# Background

Some generic background of the project

## Stock Indicators
Stocks go up and down

## Stock Trends of 11 Picked Stocks
The picked eleven stocks are: "AAPL","TSLA","AMZN","GOOG","FB","NIO","BYND","FSLY","MRNA","BABA","BLNK".

# Methods

## Data

### Collection
Stuff
### Feature Engineering
Stuff
### Labeling
Stuff
## Models

### Simple Classification Models
In this part we picked eight models from all the classification mmodels in sklearn package and tried to fit single day data to it.
#### Models picked
RBF SVM, Decision Tree, MLCP, Kneighbors, Gaussian Process, Random Forest, AdaBoost, Gaussian Naive Bayes
#### Training Data
We took two years data for each day and using the balanced label method to build the dataset. And we split them with a traning-testing ratio of 4:1.
There are two different splite settings, thus two different tests.
##### Continuous Splite
In this method, we took the first 75 percent of data as training sets without shuffling it. In this case, when the models are traing, there are still some time continuty inside the training dataset.
##### Shuffled Splite

### LSTM
Stuff
### CNN
Stuff


# Results

## Simple Classification models

### Scores of Eleven Stocks and Using continuly Splite

### Scores of Eleven Stocks and Eight Models using Shuffled Splite

### NAV of All Models based on "BABA" Stock Using Shuffled Splite

A Place for graphs tables all sort of data

# Discussion

## What can we learn from simple classifications

### The Time continuty

### The NAV performance

What model did better and all

# Conclusion
We did something
