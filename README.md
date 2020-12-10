# Stock Market Prediction AI

## Installation

### Primary Dependencies
Python3
Tensorflow 2.3
Tested on Ubuntu 20.10

### Setup
cd FinalProj/
pip install -r requirements.txt

## Architecture
The order is quite simple, the steps are as follows:
1. Data collection and processing
2. Training the model
3. Evaluating the model
4. Additional results

## Data Collection and Processing
To collect the data. run the following line:
```
python3 main.py --prepare --period 10y --interval 1d
```
The above line will collect 10 years of daily data from Yahoo Finance and pre-process the data into training and testing along with adding labels. Additional configurations may be available, however, they are subject to change.

## Training the Model
To train the model. run the following line:
```
python3 main.py --train --layer_width 60 --save_period 10
```
The above line will begin training the model with a default save location `model_checkpoints/`. This can be configured through an argument. It will save additional information such as the arguments passed in and a model description so that the model can easily be recreated in the future.

## Evaluating the Model

To evaluate the model. run the following line:
```
python3 main.py --eval --model cp-0500.ckpt
```
The above line will load a trained model from the default save location `model_checkpoints/`. This can be configured through an argument.

## Aditional Results
Additional code is available to create plots and graphs, however, that is currently out of the scope of this Readme. If you are interested in this code, check out `results.py`, it uses a similar argument structure as above with the available options inside of the file. Also check out `monte.sh` for code to easily run multiple different models from the command line in an HPC environment such as ace.wpi.edu

The repo is currently in a restructuring state, please see master branch for additional models. Proceed at your own risk.
