import matplotlib.pyplot as plt
import numpy as np
from numba import njit


def display(p_x_k):
    for i in range(p_x_k.shape[0]):
        image = p_x_k[i].reshape((28, 28))
        plt.imshow(image, cmap='gray')
        plt.show()


@njit(fastmath=True)
def prior_probability(p_k_x, size):
    """
    maximisation
    p(k)

    >>> prior_probability(np.array([[1,2,3,4,5],[6,7,8,9,10]]), 10)
    array([0.7, 0.9, 1.1, 1.3, 1.5])
    """

    return p_k_x.sum(axis=0) / size


def m_step_part(p_k_x, p_k, train_shape, train_image):
    '''
    maximisation

    p(x|k)
    '''

    n, m = train_shape
    p_x_k = np.zeros((2, m))

    p_x_k[0] = np.array([(train_image[:, i] * p_k_x[:, 0]).sum() for i in range(m)]) / (p_k[0] * n)
    p_x_k[1] = np.array([(train_image[:, i] * p_k_x[:, 1]).sum() for i in range(m)]) / (p_k[1] * n)
    return p_x_k


def posterior_probability_first_part(p_x_k, train_shape, train_image):
    '''
    expectation

    P(k|x)
    '''

    temp = np.array([
        [np.prod((p_x_k[0] ** train_image[z]) * ((1 - p_x_k[0]) ** (1 - train_image[z]))),
         np.prod((p_x_k[1] ** train_image[z]) * ((1 - p_x_k[1]) ** (1 - train_image[z])))] for z in
        range(train_shape[0])]
    )
    return temp


def posterior_probability_last_part(weight, p_k, train_shape):
    '''
    expectation

    P(k|x)
    '''

    p_k_x = np.array([weight[:, 0] * p_k[0], weight[:, 1] * p_k[1]]) / (weight[:, 0] * p_k[0] + weight[:, 1] * p_k[1])
    return np.array([[p_k_x[0][i], p_k_x[1][i]] for i in range(train_shape[0])])


def em_algorithm(t, train_shape, train_image):
    p_x_k = np.empty((2, train_shape[1]))
    expert_values_p_k_x = np.random.uniform(low=0.0, high=1, size=(train_shape[0], 2))
    p_k_x = expert_values_p_k_x / expert_values_p_k_x.sum(axis=1).reshape(-1, 1)

    for i in range(t):
        pt_k = prior_probability(p_k_x, train_shape[0])
        p_x_k = m_step_part(p_k_x, pt_k, train_shape, train_image)
        result = posterior_probability_first_part(p_x_k, train_shape, train_image)
        p_k_x = posterior_probability_last_part(result, pt_k, train_shape)  # p(k|x)  (веса)
    return p_x_k


if __name__ == '__main__':
    import doctest
    doctest.testmod()
