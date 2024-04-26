import matplotlib.pyplot as plt
import numpy as np


def x_transformation_1(x, y):
    return 0

def x_transformation_2(x, y):
    return 0.85 * x + 0.04 * y

def x_transformation_3(x, y):
    return 0.2 * x - 0.26 * y

def x_transformation_4(x, y):
    return -0.15 * x + 0.28 * y

def y_transformation_1(x, y):
    return 0.16 * y

def y_transformation_2(x, y):
    return -0.04 * x + 0.85 * y + 1.6

def y_transformation_3(x, y):
    return 0.23 * x + 0.22 * y + 1.6

def y_transformation_4(x, y):
    return 0.26 * x + 0.24 * y + 0.44


x_transformations = [x_transformation_1, x_transformation_2, x_transformation_3, x_transformation_4]
y_transformations = [y_transformation_1, y_transformation_2, y_transformation_3, y_transformation_4]

x, y = 0, 0

num_points = 100000

xs = np.zeros(num_points)
ys = np.zeros(num_points)

for i in range(num_points):
    index = np.random.choice(4, p=[0.01, 0.85, 0.07, 0.07])
    x = x_transformations[index](x, y)
    y = y_transformations[index](x, y)

    xs[i] = x
    ys[i] = y



plt.scatter(xs, ys, s=0.2, c='green')
plt.title("paproc")
plt.axis('off')
plt.show()