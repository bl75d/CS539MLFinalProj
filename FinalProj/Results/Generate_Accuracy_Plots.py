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
    plt.hlines(1, 0, len(data), linewidth=5)
    plt.plot(acc, linewidth=linewidth, color="blue", label="Accuracy")
    plt.plot(loss, linewidth=linewidth, color="red", label="Loss")
    plt.plot(mse, linewidth=linewidth, color="green", label="MSE")
    plt.vlines(0, 0, 1, linewidth=5)
    plt.hlines(0, 0, len(data), linewidth=5)
    plt.grid(linewidth=3)
    plt.legend(fontsize=legend_font)
    plt.tick_params(axis='both', labelsize=label_font)
    plt.yticks(np.arange(0,1.2,.1))
    plt.xlabel('Num Epochs', size=label_font)
    plt.ylabel('Accuracy, Loss, Error', size=label_font)
    plt.title('Training - Results verus Epochs', size=title_font)
    plt.savefig("Loss.png", bbox_inches='tight',pad_inches = .10)


    # with open('monte_carlo_final.pkl', 'rb') as f:
    #     final_test_results = pickle.load(f)

    # with open('monte_carlo_test.pkl', 'rb') as f:
    #     test_test_results = pickle.load(f)


    # x = np.arange(1, len(final_test_results)*10, 10)
    # x = np.insert(x, 0, 0)
    
    # final_test_results.insert(0, 0)
    # test_test_results.insert(0, 0)

    # print(final_test_results)
    # fig = plt.figure(figsize=(15,10))
    # fig.tight_layout(pad=0.0)
    # plt.hlines(1, 0, len(data), linewidth=5)
    # plt.plot(acc, linewidth=7, color="blue", label="Training Accuracy")
    # plt.plot(x, test_test_results, linewidth=7, color="red", label="Test Accuracy")
    # plt.plot(x, final_test_results, linewidth=7, color="green", label="Final Accuracy")
    # plt.vlines(0, 0, 1, linewidth=5)
    # plt.hlines(0, 0, len(data), linewidth=5)
    # plt.grid(linewidth=3)
    # plt.legend(fontsize=26)
    # plt.tick_params(axis='both', labelsize=24)
    # plt.yticks(np.arange(0,1.2,.1))
    # plt.xlabel('Num Epochs', size=24)
    # plt.ylabel('Accuracy, Loss, Error', size=24)
    # plt.title('Accuracy - Results verus Epochs', size=28)

    # plt.savefig("Accuracy.png", bbox_inches='tight',pad_inches = 0)