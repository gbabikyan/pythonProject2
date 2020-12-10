import matplotlib.pyplot as plt
import numpy as np

def power():
    l = list(simfunc.split())
    n = np.double(l[1])
    for i in range(np.size(x)):
        x[i] = x[i]**n

def log():
    for i in range (np.size(x)):
        x[i] = np.log(x)

x = list(map(np.double, input().split()))#входные данные оси x
x = np.asarray(x)
y = list(map(np.double, input().split()))#входные данные оси y
y = np.asarray(y)
simfunc = input()
n = int(input())
xlabel = input()
ylabel = input()
xlabel = 'r"' + xlabel
ylabel = 'r"' + ylabel
xlabel = xlabel + '"'
ylabel = ylabel + '"'
if simfunc == "log":
    log()
if simfunc == " ":
    t = 1
else:
    power()
n, bins, patches = plt.hist(x, 50, density=True, facecolor='g', alpha=0.75)

plt.xlabel(xlabel)
plt.ylabel(ylabel)
plt.axis([x.min(), x.max(), y.min(), y.max()])
plt.grid(True)
plt.show()