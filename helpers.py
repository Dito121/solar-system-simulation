import numpy as np
from models import Star, Planet, Asteroid


names = np.array(
    [
        "Mercury",
        "Venus",
        "Earth",
        "Mars",
        "Jupiter",
        "Saturn",
        "Uranus",
        "Neptune",
    ]
)
distances = np.array(
    [
        5.79 * 10**10,  # Mercury
        1.082 * 10**11,  # Venus
        1.496 * 10**11,  # Earth
        2.279 * 10**11,  # Mars
        7.786 * 10**11,  # Jupiter
        1.433 * 10**12,  # Saturn
        2.873 * 10**12,  # Uranus
        4.495 * 10**12,  # Neptune
    ]
)
periods = np.array(
    [
        7.603 * 10 ^ 6,  # Mercury
        1.944 * 10 ^ 7,  # Venus
        3.154 * 10 ^ 7,  # Earth
        5.936 * 10 ^ 7,  # Mars
        3.74017 * 10 ^ 8,  # Jupiter
        9.145 * 10 ^ 8,  # Saturn
        2.649 * 10 ^ 9,  # Uranus
        5.203 * 10 ^ 9,  # Neptune
    ]
)
masses = np.array(
    [
        3.3 * 10**23,  # Mercury
        4.87 * 10**24,  # Venus
        5.972 * 10**24,  # Earth
        6.42 * 10**23,  # Mars
        1.898 * 10**27,  # Jupiter
        5.69 * 10**26,  # Saturn
        8.68 * 10**25,  # Uranus
        1.03 * 10**26,  # Neptune
    ]
)
radii = np.array(
    [
        2439000,  # Mercury
        6052000,  # Venus
        6378100,  # Earth
        3397000,  # Mars
        69911000,  # Jupiter
        60268000,  # Saturn
        25559000,  # Uranus
        24764000,  # Neptune
    ]
)


def create_objects(
    names=names,
    distances=distances,
    periods=periods,
    masses=masses,
    radii=radii,
):
    sun = Star(1.989 * 10**30, 695500000)
    asteroid = Asteroid(
        "asteroid",
        2000,
        1.496 * 10**11,
        637810,
    )
    planets = [
        Planet(
            names[i],
            distances[i],
            masses[i],
            periods[i],
            radii[i],
        )
        for i in range(len(names))
    ]

    return sun, planets, asteroid
