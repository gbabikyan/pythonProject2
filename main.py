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
p, v = np.polyfit(x, y, deg=n, cov=True)
p_f = np.poly1d(p)
print(p_f)
x1 = np.arange(x[0], x[np.size(x) - 1], 0.0001)
fig, ax = plt.subplots()
ax.plot(x1, p_f(x1), color = 'blue',linewidth = 1)
ax.plot(x, y, 'ro')
ax.minorticks_on()
ax.grid(which='major',
        color = 'k',
        linewidth = 2)
ax.grid(which='minor',
        color = 'k',
        linestyle = ':')
plt.xlabel(xlabel)
plt.ylabel(ylabel)
fig.set_figwidth(12)
fig.set_figheight(6)

plt.show()