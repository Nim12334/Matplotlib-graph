import matplotlib.pyplot as plt
import numpy as np
from sympy import cot
data =np.arctanh(np.random.random((50,50,50)))

fig, ax = plt.subplots()

for i in range(12000):
    ax.cla()
    ax.imshow(np.tan(np.radians(np.exp(np.sinc(np.log(data[i]))))))
    b=50
    n1=b-i
    ax.set_title(f"анимация закончится через {n1} секунд")

    plt.pause(0.5)