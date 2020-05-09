from pylab import *
from numpy import *

n = random.randn(100000)
fig, axes = plt.subplots(1, 2, figsize = (12, 4))

# x = linspace(0, 5, 10)
# y = x ** 2

axes[0].hist(n)
axes[0].set_title('Default histogram')
axes[0].set_xlim((min(n), max(n)))

axes[1].hist(n, cumulative = True, bins = 50)
axes[1].set_title('Cumulative detailed histogram')
axes[1].set_xlim((min(n), max(n)))

show()