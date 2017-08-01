import matplotlib.pyplot as plt

x = [1990, 1992, 1994, 1996, 1998, 2000, 2002, 2004, 2006, 2008, 2010, 2012, 2014, 2016]
y = [2.439, 2.5963, 2.7345, 3.4523, 3.8234, 4.0134, 4.5325, 4.94234, 5.232423,
     5.49663, 6.123, 7.123,  7.455, 9.4234]

plt.plot(x, y)

plt.xlabel("Year")
plt.ylabel("Population")
plt.title("World Population Projections")

plt.yticks([0, 2, 4, 6, 8, 10],
           ['0', '2B', '4B', '6B', '8B', '10B'])

plt.show()