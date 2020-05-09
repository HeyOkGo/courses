from pylab import *

fig, axes = plt.subplots()

x = linspace(0, 5, 10)
y = x ** 2

axes.plot(x, x ** 2, label = "y = x ** 2")
axes.plot(x, x ** 3, label = "y = x ** 3")
axes.legend(loc = 2)
# axes.plot(x, y, 'r')
axes.set_xlabel('x')
axes.set_ylabel('y')
axes.set_title('title')
show()