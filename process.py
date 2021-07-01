import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
from scipy import interpolate
from nutons import newton_polynomial, _poly_newton_coefficient

x = [2,  3,    4,    5,    6,    7,    8,  9,    10,   11,   12,   13,   14,   15]
y = [24, 17.5, 16.1, 15.7, 15.4, 15.6, 16, 16.9, 18.2, 20.2, 22.7, 24.4, 25.6, 26]

x1 = [2,  4,    6,    8,  10,   12,   14]
y1 = [24, 16.1, 15.4, 16, 18.2, 22.7, 25.6]
origY = [17.5, 15.7, 15.6, 16.9, 20.2, 24.4, 26]

tck = interpolate.splrep(x, y)
result, resultX, resultY = [], [], []
result1, resultX1, resultY1 = [], [], []
result2, resultX2, resultY2 = [], [], []

for i in np.arange(2.5, 15.5, 1):
    val = newton_polynomial(x, y, i)
    val2 = newton_polynomial(x1, y1, i)

    result.append(val)
    resultX.append(i)
    resultY.append(val)

    result1.append(val2)
    resultX1.append(i)
    resultY1.append(val2)

    val2 = interpolate.splev(i, tck)
    result2.append(val2)

    resultX2.append(i)
    resultY2.append(val2)


error = []

for i in range(len(resultY)):
    error.append((abs(resultY[i] - resultY2[i])/resultY[i]))

d = {'X vērtība': resultX, 'Solis h = 1': resultY, "Kubisko splainu": resultY2, "Atšķirība": error}
df = pd.DataFrame(data=d)
df.round(4)
print(df)

plt.plot(x, y, 'mo', label="Oriģinālais h = 1")
plt.plot(resultX, resultY, 'r', label="Solis h = 1")
plt.plot(resultX1, resultY1, 'g', label="Solis h = 2")
plt.plot(resultX2, resultY2, 'b', label="Kubisko splainu")

plt.grid(alpha=0.5)
plt.legend()
plt.show()
