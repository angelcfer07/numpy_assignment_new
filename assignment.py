import numpy as np
import matplotlib.pyplot as plt

# Q1
def create_array():
    return np.arange(1, 11)


# Q2
def array_arithmetic(a, b):
    return {
        "addition": a + b,
        "subtraction": a - b,
        "multiplication": a * b,
        "division": a / b
    }


# Q3
def slicing_example(arr):
    return {
        "first_5": arr[:5],
        "last_5": arr[-5:],
        "index_5_to_10": arr[5:11],
        "reverse": arr[::-1]
    }


# Q4
def matrix_multiplication(a, b):
    return np.dot(a, b)


# Q5
def random_numbers():
    return np.random.rand(5)


# Q6
def plot_graph():
    x = np.arange(0, 11)
    y = x ** 2

    plt.plot(x, y, label="y = x^2")
    plt.title("Graph of y = x^2")
    plt.xlabel("X values")
    plt.ylabel("Y values")
    plt.legend()
    plt.show()
