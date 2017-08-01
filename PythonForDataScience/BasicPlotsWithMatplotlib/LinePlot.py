import matplotlib.pyplot as plt

x = [2010, 2012, 2013, 2015]
y = [1.341, 3.235, 4.4234, 5.123]

plt.plot(x, y)
plt.scatter(x, y)
plt.xscale('log')
plt.show()