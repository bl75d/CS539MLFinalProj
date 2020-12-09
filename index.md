# Stock Market Trading Thing

General Purpose


# Background

Some generic background of the project

## Stock Indicators
Stocks go up and down

## Stock Trends of 11 Picked Stocks
The picked eleven stocks are: "AAPL","TSLA","AMZN","GOOG","FB","NIO","BYND","FSLY","MRNA","BABA","BLNK".
### Relative stable Stocks
"AAPL", "TSLA", "AMZN", "GOOG", and "FB" have relative stable stock price trends. They are big Internet companies and their stock price keeps rise most of the time.
### Flat and Increase Stocks
"NIO", "MRNA" and "BLNK" has a very stable trend in the beginning, however, their price increased dramatically in the latter days.
### Relative Unstable Stocks
"BYND", "FSLY" and "BABA" have a relatively unstable trend. Their price keeps going up and down and it would be really hard to correctly calculate them.
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
In this part, we picked eight models from all the classification models in the sklearn package and tried to fit single day data to it.
#### Models picked
RBF SVM, Decision Tree, MLCP, Kneighbors, Gaussian Process, Random Forest, AdaBoost, Gaussian Naive Bayes
#### Training Data
We took two years of data for each day and using the balanced label method to build the dataset. And we split them with a training-testing ratio of 4:1.
There are two different split settings, thus two different tests.
##### Continuous Splite
In this test, we took the first 75 percent of the data as training sets without shuffling it. In this case, when the models are trained, there is still some time continuity inside the training dataset. This split has a problem, when the training period stock trend varies a lot with the testing days, the model can be very inaccurate.
##### Shuffled Splite
In this test, even though we still picked out 75 percent days as the training dataset, but the data was shuffled before taking into use. Thus, the time continues day with each day would be broken.
#### Parameter settings
For Kneighbors, we are using k = 3, since we only have three labels. For the SVM, we are using C = 0.5, in order to make the model more balanced. For the Decision Tree, Random Forest, and MLCP, we gave them a very large max depth and max iteration to make sure that they can find the best result. And we give max_features = 47 to Random Forest since we only have that much.

### LSTM
Stuff
### CNN
Stuff


# Results

## Simple Classification models
### Scores of Eleven Stocks and Using continuly Splite
The table below shows the scores of all the models under all the stocks using continues split.

### Scores of Eleven Stocks and Eight Models using Shuffled Splite
The table below shows the scores of all the models under all the stocks using shuffled split.

### NAV of All Models based on "BABA" Stock Using Shuffled Splite
In this part of testing results, we only picked the most significant stock "BABA", which is increasing in a relatively unstable way. And the split way is Shuffled splite.


# Discussion

## What can we learn from simple classifications

### The Time continuty

### The NAV performance

What model did better and all

# Conclusion
We did something
