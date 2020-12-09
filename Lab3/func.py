import numpy as np
import pandas as pd
import mnist
import matplotlib.pyplot as plt


# x = np.random.rand(60000, 28, 28)
# print(x[:, 0][:, 0])
# print(x[:, 0][:, 0].shape)


def display(p_x_k):
    for i in range(p_x_k.shape[0]):
        image = p_x_k[i].reshape((28, 28))
        plt.imshow(image, cmap='gray')
        plt.show()


def prior_probability(p_k_x, size):
    '''
    maximisation

    p(k)
    '''

    return p_k_x.sum(axis=0) / size


def m_step_part(p_k_x, p_k):
    '''
    maximisation

    p(x|k)
    '''
    n, m = train_images.shape
    p_x_k = np.zeros((2, m))

    p_x_k[0] = np.array([(train_images[:, i] * p_k_x[:, 0]).sum() for i in range(m)]) / (p_k[0] * n)
    p_x_k[1] = np.array([(train_images[:, i] * p_k_x[:, 1]).sum() for i in range(m)]) / (p_k[1] * n)

    return p_x_k


def posterior_probability_first_part(p_x_k):
    '''
    expectation

    P(k|x)
    '''

    n = train_images.shape[0]

    temp = np.array([
        [np.prod((p_x_k[0] ** train_images[z]) * ((1 - p_x_k[0]) ** (1 - train_images[z]))),
         np.prod((p_x_k[1] ** train_images[z]) * ((1 - p_x_k[1]) ** (1 - train_images[z])))] for z in range(n)]
    )

    return temp


def posterior_probability_last_part(weight, p_k):
    '''
    expectation

    P(k|x)
    '''

    p_k_x = np.array([weight[:, 0] * p_k[0], weight[:, 1] * p_k[1]]) / (weight[:, 0] * p_k[0] + weight[:, 1] * p_k[1])
    # t = np.array([[p_k_x[0][i], p_k_x[1][i]] for i in range(X.shape[0])])
    return np.array([[p_k_x[0][i], p_k_x[1][i]] for i in range(train_images.shape[0])])


def em_algorithm(t, train_shape):
    # n = train_images.shape[0]
    p_x_k = np.empty((2, train_shape[1]))
    expert_values_p_k_x = np.random.uniform(low=0.0, high=1, size=(train_shape[0], 2))
    p_k_x = expert_values_p_k_x / expert_values_p_k_x.sum(axis=1).reshape(-1, 1)

    for i in range(t):
        pt_k = prior_probability(p_k_x, train_shape[0])
        p_x_k = m_step_part(p_k_x, pt_k)
        result = posterior_probability_first_part(p_x_k)
        p_k_x = posterior_probability_last_part(result, pt_k)  # p(k|x)  (веса)
    return p_x_k


if __name__ == '__main__':
    # p_k_x = np.random.rand(60000, 2)
    # p_k = np.random.rand(2, )
    # X = np.random.rand(60000, 784)

    train_images_, train_labels_ = mnist.train_images().reshape(60000, -1), mnist.train_labels()
    data = pd.DataFrame(np.concatenate([train_labels_.reshape(-1, 1), train_images_], axis=1))
    # df = pd.concat([train_labels, train_images], axis=1)
    data = data[data.iloc[:, 0].isin([4, 3])].reset_index(drop=True)

    # print(train_images.shape, train_labels.shape)

    targets, values = data.iloc[:, 0], data.iloc[:, 1:]
    train_images = values.astype("bool").to_numpy()

    # display(m_step_part(p_k_x, p_k))
    # print(m_step_part(p_k_x, p_k))
    # a = posterior_probability_first_part(m_step_part(p_k_x, p_k))
    # b = posterior_probability_last_part(a, p_k)
    # print(b)
    # print(b.shape)

    display(em_algorithm(3, train_images.shape))
