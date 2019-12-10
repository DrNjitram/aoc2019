from boilerplates import read_text_from_file
from math import atan2, pi

f = read_text_from_file("day10")

def get_visible(file):
    aster = {}
    for r, row in enumerate(file):
        for c, column in enumerate(row):
            if column == "#":
                aster[(c, r)] = 0

    for source in aster:
        angles = set()
        for target in aster:
            angles.add(atan2(source[1] - target[1], source[0] - target[0]))
            aster[source] = len(angles) - 1
    return aster

def get_angles(aster, source, offset = 0):
    angles = {}
    for target in aster:
        x = source[0] - target[0]
        y = source[1] - target[1]
        angle = (atan2(y, x) + offset + 2 * pi)% (2 * pi)
        distance = abs(x) + abs(y)
        if angle not in angles or distance < angles[angle][0]:
            angles[angle] = distance, target
    return angles

def solution():
    asteroids = get_visible(f)

    station = (0, 0)
    for a in asteroids:
        if asteroids[a] == max(asteroids.values()):
            station = a

    angles = get_angles(asteroids, station, -0.5 * pi)
    sorted_angles = sorted(angles)

    destroyed = angles[sorted_angles[199]]

    return max(asteroids.values()) + 1, destroyed[1][0]*100 + destroyed[1][1]

from timeit import timeit
print(solution())
print(timeit(solution, number=100)/100)