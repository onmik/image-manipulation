import numpy as np
import matplotlib.pyplot as plt

"""
xk = np.linspace(0, 1, 5)
x = np.linspace(0, 1, 100)
def true_fn(x):
    return x**2 - x - np.cos(np.pi*x) 

plt.figure(figsize=(12,6))
plt.plot(xk, true_fn(xk), 'x', markersize=15)
plt.plot(x, true_fn(x), '--r')

def euclidean_distance(x, xk):
    return np.sqrt((x.reshape(-1, 1) - xk.reshape(1, -1))**2)

def gauss_rbf(radius, eps):
    return np.exp(-(eps * radius)**2)

def rbf(eps, x_k, y_k, x_n):
    transformation_1 = gauss_rbf(euclidean_distance(x_k,x_k), eps)
    w_k = np.linalg.solve(transformation_1, y_k)
    transformation_2 = gauss_rbf(euclidean_distance(x_n, x_k), eps)
    return transformation_2.dot(w_k)

yk = true_fn(xk)

plt.figure(figsize=(12, 6))
plt.plot(xk, yk, 'o')
plt.plot(x, true_fn(x), 'b')
plt.plot(x, rbf(2, xk, yk, x), '--r')

"""
