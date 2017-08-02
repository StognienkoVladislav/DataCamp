
import numpy as np



if __name__ == '__main__':

    height = [1.73, 1.68, 1.71, 1.89, 1.79]
    weight = [65.4, 59.2, 63.6, 88.4, 68.7]

    np_height = np.array(height)
    np_weight = np.array(weight)

    print(np_height, "\n", np_weight)   #Numpy

    bmi = np_weight / np_height ** 2

    print(bmi)

    print(height + height)
    print(np_height + np_height)        #Numpy

    print(bmi > 23)
    print(bmi[bmi > 23])

    np_2d = np.array([[1.73, 1.68, 1.71, 1.89, 1.79],
                     [65.4, 59.2, 63.6, 88.4, 68.7]])

    print(np_2d)
    print(np_2d.shape)
    print(np_2d[:, 1:3])

    height = np.round(np.random.normal(1.75, 0.20, 5000), 2)
    weight = np.round(np.random.normal(60.32, 15, 5000), 2)
    np_city = np.column_stack((height, weight))