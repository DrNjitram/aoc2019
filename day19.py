from intcode import get_output
from boilerplates import read_number_from_file

def print_map(m):
    x_s = []
    y_s = []

    for panel in m:
        x_s.append(panel[0])
        y_s.append(panel[1])
    left = (0, 0)
    right = (0, 0)
    for y in range(min(y_s), max(y_s) + 1):

        row = str(y) + " "
        for x in range(min(x_s), max(x_s) + 1):
            row += {1: "#", 0: "."}[m.get((x, y), 0)]
        print(row)


commands = read_number_from_file("day19")

pulling = {}
diagonal = (100**2 + 100**2)**0.5
print(diagonal)

y = 900
while True:
    x = 550
    while True:
        x += 1
        output = get_output(commands[:], [x,y])

        if output[2][0]:
            bl = 1
            tl = get_output(commands[:], [x, y - 99])[2][0]
            tr = get_output(commands[:], [x + 99, y - 99])[2][0]
            br = get_output(commands[:], [x + 99, y])[2][0]
            print(x, y, output[2][0], tl, tr, br)
            break
    if bl and tl and tr and br: #double check
        j = x
        acc = []
        closest_x = x
        closest_y = y - 100
        closest_dist = (closest_x ** 2 + (closest_y - 100) ** 2) ** 0.5
        for i in range(y, y - 99, -1):
            if (closest_x ** 2 + i ** 2) ** 0.5 < closest_dist:
                closest_y = i
                closest_dist = (j ** 2 + closest_y ** 2) ** 0.5
            acc.append(get_output(commands[:], [j, i])[2][0])

        for i in range(y, y - 99, -1):
            acc.append(get_output(commands[:], [j + 100, i])[2][0])

        i = y

        for j in range(x, x + 99):
            acc.append(get_output(commands[:], [j, i])[2][0])

        for j in range(x, x + 99):
            if (j**2 + closest_y**2)**0.5 < closest_dist:
                closest_x = j
                closest_dist = (j**2 + closest_y**2)**0.5

            acc.append(get_output(commands[:], [j, i - 100])[2][0])
        print(sum(acc))

        if sum(acc) == 396: # Doesnt like corners for some reason
            print(closest_x * 10000 + closest_y + 1 )
            exit()

    y += 1


#6190948