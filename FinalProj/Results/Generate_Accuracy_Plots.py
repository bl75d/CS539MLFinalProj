import pickle

import numpy as np
import matplotlib.pyplot as plt

def training_accuracy(csv):
    def on_resize(event):
        fig.tight_layout(pad=0.0)
        fig.canvas.draw()

    data = np.loadtxt(open(csv, "rb"), delimiter=",", skiprows=0, dtype=str)
    labels = data[0]
    print(labels)

    data = np.array(data[1:], dtype=float)

    acc = data[:,1]
    loss = data[:,2]
    mse = data[:,3]

    acc = np.insert(acc, 0, 0)
    loss = np.insert(loss, 0, np.inf)
    mse = np.insert(mse, 0, np.inf)
    
    linewidth = 5
    legend_font = 22
    label_font = 22
    title_font = 24

    # print(data)
    fig = plt.figure(figsize=(15,10))
    fig.tight_layout(pad=0.0)
    plt.hlines(1, 0, len(data), linewidth=5, color="black")
    plt.plot(acc, linewidth=linewidth, color="blue", label="Accuracy")
    plt.plot(loss, linewidth=linewidth, color="red", label="Loss")
    plt.plot(mse, linewidth=linewidth, color="green", label="MSE")
    plt.vlines(0, 0, 1, linewidth=5, color="black")
    plt.hlines(0, 0, len(data), linewidth=5, color="black")
    plt.grid(linewidth=3)
    plt.legend(fontsize=legend_font)
    plt.tick_params(axis='both', labelsize=label_font)
    plt.yticks(np.arange(0,1.2,.1))
    plt.xlabel('Num Epochs', size=label_font)
    plt.ylabel('Accuracy, Loss, Error', size=label_font)
    plt.title('Training - Results verus Epochs', size=title_font)
    plt.savefig("Training.png", bbox_inches='tight',pad_inches = .10)


def testing_accuracy(data, num_epochs=500):
    def on_resize(event):
        fig.tight_layout(pad=0.0)
        fig.canvas.draw()

    data = np.array(data[:], dtype=float)

    loss = data[:,0]
    acc = data[:,1]
    mse = data[:,2]

    acc = np.insert(acc, 0, 0)
    loss = np.insert(loss, 0, np.inf)
    mse = np.insert(mse, 0, np.inf)

    x = np.arange(0, num_epochs, num_epochs/(len(acc)-1))
    x = np.append(x, num_epochs)
    print(x)
    
    linewidth = 5
    legend_font = 22
    label_font = 22
    title_font = 24

    fig = plt.figure(figsize=(15,10))
    fig.tight_layout(pad=0.0)
    plt.hlines(1, 0, len(data), linewidth=5, color="black")
    plt.plot(x, acc, linewidth=linewidth, color="blue", label="Accuracy")
    plt.plot(x, loss, linewidth=linewidth, color="red", label="Loss")
    plt.plot(x, mse, linewidth=linewidth, color="green", label="MSE")
    plt.vlines(0, 0, 1, linewidth=5, color="black")
    plt.hlines(0, 0, len(data), linewidth=5, color="black")
    plt.grid(linewidth=3)
    plt.legend(fontsize=legend_font)
    plt.tick_params(axis='both', labelsize=label_font)
    plt.yticks(np.arange(0,1.2,.1))
    plt.xlabel('Num Epochs', size=label_font)
    plt.ylabel('Accuracy, Loss, Error', size=label_font)
    plt.title('Testing - Results verus Epochs', size=title_font)

    plt.savefig("Testing.png", bbox_inches='tight',pad_inches = 0)