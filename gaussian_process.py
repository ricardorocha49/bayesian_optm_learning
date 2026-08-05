import numpy as np
import matplotlib.pyplot as plt

import numpy as np

def kernel_function(X: np.ndarray, l: float, sigma: float) -> np.ndarray:
    "Computes the covariance matrix using the squared exponential"
    K = np.zeros((np.size(X),np.size(X)))
    for i in range(np.size(X)):
        x = X[i] * np.ones(np.size(X))
        K[i,:] = sigma**2 * np.exp(-0.5 * np.transpose(x - X) * l**(-2) * (x - X))
    return K
    

# test set
Xtest = np.linspace(-5,5,10)

# kernel function
l = 1
sigma = 0.5

covariance = kernel_function(Xtest, l, sigma)



