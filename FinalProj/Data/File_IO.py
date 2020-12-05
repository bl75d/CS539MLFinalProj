import numpy as np

def save_to_npy(array, filename):
    np.save(filename, array)    # .npy extension is added if not given

def load_from_npy(filename):
    array= np.load(filename)    # .npy extension is added if not given
    return array
