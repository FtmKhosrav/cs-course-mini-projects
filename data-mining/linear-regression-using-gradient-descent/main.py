import numpy as np
import matplotlib.pyplot as plt
import scipy.io as sio
from google.colab import files

# Upload dataset
uploaded = files.upload()

# Load .mat file
mat_data = sio.loadmat('data_for_linearregression_tamrin.mat')

# Extract variables
x = mat_data['x']
y = mat_data['y']

m = len(y)

print("Dataset Overview:")
print(f"x shape: {x.shape}")
print(f"y shape: {y.shape}")

# Plot data
plt.scatter(x, y, color='blue')
plt.xlabel("x")
plt.ylabel("y")
plt.title("Dataset Visualization")
plt.show()

# Add bias term
X = np.hstack((np.ones((m, 1)), x))

# Initialize theta
theta = np.zeros((2, 1))

alpha = 0.01
iterations = 1000

# Cost function
def compute_cost(X, y, theta):
    m = len(y)
    predictions = X.dot(theta)
    return (1 / (2 * m)) * np.sum((predictions - y) ** 2)

# Gradient Descent
def gradient_descent(X, y, theta, alpha, iterations):
    m = len(y)
    cost_history = []

    for _ in range(iterations):
        error = X.dot(theta) - y
        theta -= (alpha / m) * X.T.dot(error)
        cost_history.append(compute_cost(X, y, theta))

    return theta, cost_history

# Train model
theta_optimal, cost_history = gradient_descent(X, y, theta, alpha, iterations)

# Plot cost function
plt.plot(cost_history)
plt.title("Cost Function Over Iterations")
plt.xlabel("Iteration")
plt.ylabel("Cost")
plt.show()

print("Optimal Theta:", theta_optimal.ravel())

# Plot regression line
plt.scatter(x, y, color='blue')
plt.plot(x, X.dot(theta_optimal), color='red')
plt.title("Linear Regression Fit")
plt.show()
