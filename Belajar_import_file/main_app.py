import numpy as np
import matplotlib.pyplot as plt


def sinus_generator(amplitudo, frekuensi, t_akhir, theta):
    t = np.arange(0, t_akhir, 0.1)
    y = amplitudo * np.sin(2 * frekuensi * t + np.deg2rad(theta))
    return t, y


t1, y1 = sinus_generator(1, 1, 4, 0)
plt.plot(t1, y1)
t2, y2 = sinus_generator(1, 1, 4, 30)
plt.plot(t2, y2, "r")
t3, y3 = sinus_generator(1, 1, 4, 60)
plt.plot(t3, y3, "b--")
t4, y4 = sinus_generator(1, 1, 4, 90)
plt.plot(t4, y4, "b-o")
plt.axis([0, 4, -2, 2])
plt.show()
