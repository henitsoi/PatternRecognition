from func import display, em_algorithm
import numpy as np
import pandas as pd
import mnist
from time import perf_counter

train_images_, train_labels_ = mnist.train_images().reshape(60000, -1), mnist.train_labels()

data = pd.DataFrame(np.concatenate([train_labels_.reshape(-1, 1), train_images_], axis=1))
data = data[data.iloc[:, 0].isin([4, 3])].reset_index(drop=True)
targets, values = data.iloc[:, 0], data.iloc[:, 1:]
train_images = values.astype("bool").to_numpy()

start = perf_counter()
alg = em_algorithm(5, train_images.shape, train_images)
end = perf_counter()
print(end - start)
display(alg)
