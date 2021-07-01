import matplotlib.pyplot as plt
import numpy as np
from nutons import newton_polynomial, _poly_newton_coefficient
from scipy import interpolate

import pandas as pd


def main():
    x = [2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15]
    y = [24, 17.5, 16.1, 15.7, 15.4, 15.6, 16, 16.9, 18.2, 20.2, 22.7, 24.4, 25.6, 26]

    tck = interpolate.splrep(x, y)
    result, resultX, resultY = [], [], []

    for i in np.arange(2.5, 14.5, 1):
        val = interpolate.splev(i, tck)
        result.append(val)

        resultX.append(i)
        resultY.append(val)

    plt.plot(x, y, 'bo', label="Oriģinālais h = 1")
    plt.plot(resultX, resultY, 'r', label="Kubiskā splaina interpolācija")
    plt.grid(alpha=0.5)
    plt.legend()
    plt.show()

    error = []

    for i in range(len(resultY)):
        error.append((abs(y[i] - resultY[i])/y[i]) * 100)
    # , "Oriģinālā vērtība": y, "Kļūda": error
    d = {'X vērtība': resultX, 'Starpunktu vērtība': resultY}
    df = pd.DataFrame(data=d)
    df.round(4)
    print(df)


if __name__ == "__main__":
    main()
