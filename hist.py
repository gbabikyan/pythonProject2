import matplotlib.pyplot as plt
import numpy as np

x = list(map(np.double, input().split()))#входные данные
z = list()
x = np.asarray(x)
xlabel = input()
ylabel = input()
xlabel = 'r"' + xlabel
ylabel = 'r"' + ylabel
xlabel = xlabel + '"'
ylabel = ylabel + '"'
n, bins, patches = plt.hist(x, x.size, density=True, facecolor='red')
plt.xlabel(xlabel)
plt.ylabel(ylabel)
plt.grid(True)
plt.show()