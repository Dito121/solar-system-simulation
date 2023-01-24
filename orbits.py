from matplotlib import animation
import matplotlib.pyplot as plt
import numpy as np
import os, sys
from scipy.integrate import odeint
from helpers import create_objects


G = 6.67408 * 10 ^ (-11)
sun, planets, asteriod = create_objects()

N = 1001
t3 = np.linspace(0, planets[3].period, N)
t5 = np.linspace(0, planets[5].period, N)


def get_positions():
    positions = np.zeros(4 * (len(planets) + 1))

    for i in range(4, len(positions) - 4, 4):
        positions[i] = planets[i].distance * np.cos(np.pi)
        positions[i + 1] = -planets[i].velocity * np.sin(np.pi)
        positions[i + 2] = planets[i].distance * np.sin(np.pi)
        positions[i + 3] = planets[i].velocity * np.cos(np.pi)

    return positions


positions = get_positions()


def genOrbitalMotion(t, positions=positions):
    n = len(positions) // 4
    x, y = np.zeros(n), np.zeros(n)
    ans_arr = np.zeros_like(positions)

    x = positions[::4]  # assign x position array
    y = positions[2::4]  # assign y position array
    a_x = np.zeros(n)  # acceleration in x direction
    a_y = np.zeros(n)  # acceleration in y direction

    ans_arr[::4] = positions[1::4]  # assign Vx
    ans_arr[2::4] = positions[3::4]  # assign Vy

    for i in range(n):
        sumx, sumy = 0, 0
        for j in range(n):
            if i == j:
                continue
            R = np.sqrt((x[i] - x[j]) ** 2 + (y[i] - y[j]) ** 2)
            sumx += -(G * planets[j].mass * (x[i] - x[j])) / (R**3)
            sumy += -(G * planets[j].mass * (y[i] - y[j])) / (R**3)
        a_x[i], a_y[i] = sumx, sumy

    ans_arr[1::4] = a_x
    ans_arr[3::4] = a_y
    return np.array(ans_arr)


def orbitalMotion(positions, t):
    ans_arr = odeint(genOrbitalMotion, positions, t)
    return np.array(ans_arr)


def create_orbital_motion():
    ff_path = os.path.join(
        "C:/", "Program Files/", "ImageMagick-7.0.3-Q16", "ffmpeg.exe"
    )
    plt.rcParams["animation.ffmpeg_path"] = ff_path
    if ff_path not in sys.path:
        sys.path.append(ff_path)

    imgk_path = os.path.join(
        "C:/", "Program Files/", "ImageMagick-7.0.3-Q16", "convert.exe"
    )
    plt.rcParams["animation.convert_path"] = imgk_path
    if ff_path not in sys.path:
        sys.path.append(imgk_path)

    fig = plt.figure()
    ax = plt.axes(
        xlim=(-planets[5].distance, planets[5].distance),
        ylim=(-planets[5].distance, planets[5].distance),
    )
    (data,) = ax.plot([], [], "ro")
    ax.set_xlabel("x position")
    ax.set_ylabel("y position")

    def init():
        data.set_data([], [])
        return (data,)

    def animate(time):
        x = planets[5].period[time, 0::4]
        y = planets[5].period[time, 2::4]
        data.set_data(x, y)
        return (data,)

    anim = animation.FuncAnimation(
        fig, animate, init_func=init, frames=1000, interval=20, blit=True
    )

    FFwriter = animation.FFMpegWriter(fps=30)

    anim.save(
        os.path.join(
            "C:/",
            "Users/",
            "Dito/",
            "Documents/",
            "UPITT/",
            "Fall 2016/",
            "Physics 1321/",
            "Destabilization",
            "basic_solar_system_animation_closeup.mp4",
        ),
        writer=FFwriter,
        extra_args=["-vcodec", "libx264"],
    )

    # anim.save(os.path.join('C:/Users/Dito/Documents/Momentum/Phase5/solar-system-animation/basic_animation.gif'), writer='ImageMagick-7.0.3-Q16', fps=30)
