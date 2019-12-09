from codecs import open
problem = [i.strip() for i in open(r"D:\AdventOfCode2019\probleminput\day6.txt").readlines()]

def get_distance_to(orbit, orbit_dict, to = "COM"):
    distance = 0
    while orbit != to:
        orbit = orbit_dict[orbit]
        distance += 1
    return distance

def get_orbits(orbit, orbit_dict):
    visited = []
    while orbit != "COM":
        orbit = orbit_dict[orbit]
        visited.append(orbit)
    return visited

def solution():
    orbit_dict = {}
    for i in problem:
        orbit_dict[i.split(")")[1]] = i.split(")")[0]

    total_dist = 0
    for orbit in orbit_dict.keys():
        total_dist += get_distance_to(orbit, orbit_dict)

    visited_you = get_orbits("YOU", orbit_dict)
    visited_san = get_orbits("SAN", orbit_dict)

    depth = 0
    vis_you_rev = visited_you[::-1]
    vis_san_rev = visited_san[::-1]
    for i in range(max([len(visited_san), len(visited_you)])):
        a = vis_you_rev[i]
        b = vis_san_rev[i]
        if a == b:
            depth += 1
        else:
            break

    return total_dist, len(visited_san) + len(visited_you) - 2 * depth

print(solution())

from timeit import timeit
print(timeit(solution, number=1000)/1000)