import numpy as np
import matplotlib.pyplot as plt

import numpy as np

def kernel_function(X: np.ndarray, l: float, sigma: float) -> np.ndarray:
    "Computes the covariance matrix using the squared exponential"

    x = X[0:-1]
    xl = X[1:]
    K = sigma**2 * np.exp(-0.5 * np.transpose(x - xl) * l**(-2) * (x - xl))
    return K
    

# test set
Xtest = np.linspace(-5,5,10)

# kernel function
l = 1
sigma = 0.5

kernel = kernel_function(Xtest, l, sigma)
print(kernel)

