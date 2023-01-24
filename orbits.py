import matplotlib.pyplot as plt
import numpy as np
from scipy.integrate import odeint
from helpers import create_objects


sun, planets, asteriod = create_objects()


def genOrbitalMotion(y_arr, t):
    n = len(y_arr) // 4

    X = np.zeros(n)
    Y = np.zeros(n)
    ans_arr = np.zeros_like(y_arr)

    X = y_arr[::4]  # assign x position array
    Y = y_arr[2::4]  # assign y position array
    Ax = np.zeros(n)  # acceleration in x direction
    Ay = np.zeros(n)  # acceleration in y direction

    ans_arr[::4] = y_arr[1::4]  # assign Vx
    ans_arr[2::4] = y_arr[3::4]  # assign Vy

    for i in range(n):
        sumx, sumy = 0, 0
        for j in range(n):
            if i == j:
                continue
            R = np.sqrt((X[i] - X[j]) ** 2 + (Y[i] - Y[j]) ** 2)
            sumx += -(G * Mass[j] * (X[i] - X[j])) / (R**3)
            sumy += -(G * Mass[j] * (Y[i] - Y[j])) / (R**3)
        Ax[i], Ay[i] = sumx, sumy

    ans_arr[1::4] = Ax
    ans_arr[3::4] = Ay
    return np.array(ans_arr)


def orbitalMotion(y_arr, t):
    ans_arr = odeint(genOrbitalMotion, y_arr, t)
    return np.array(ans_arr)
