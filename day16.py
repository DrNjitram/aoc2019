import numpy as np
from boilerplates import read_text_from_file

def flatten_list(n):
    nested_list = n[:]
    while nested_list:
        sublist = nested_list.pop(0)
        if isinstance(sublist, list):
            nested_list = sublist + nested_list
        else:
            yield sublist

def parse_input(number):
    return [int(i) for i in str(number)]

def generate_pattern(length):
    base_pattern = [0, 1, 0, -1]
    p_s = []

    for i in range(1, length + 1):
        j = 0
        p = []
        while len(list(flatten_list(p))) - 1 < length:
            p.append([base_pattern[j]] * i)
            j = (j + 1)%len(base_pattern)

        p_s.append(list(flatten_list(p))[1:length + 1])

    return np.array(p_s)

def FFT(number, p_s):
    return [abs(sum(row))%10 for row in number * p_s]

def part1(no):
    patterns = generate_pattern(len(no))

    for i in range(100):
        no = FFT(no, patterns)

    print(("".join([str(i) for i in no[:8]])))

def part2():
    inp = read_text_from_file("day16")[0]
    skip = int(inp[0:7])
    digits = parse_input(inp * 10000)


    for i in range(100):
        print(i)
        leftover = sum(digits[skip:])
        new_digits = [0] * skip + [int(str(leftover)[-1])]
        for n in range(skip + 2, len(digits) + 1):
            leftover -= digits[n - 2]
            new_digits += [int(str(leftover)[-1])]
        digits = new_digits

    print("Part 2 - ", ''.join(str(i) for i in digits[skip:(skip + 8)]))

inp = read_text_from_file("day16")[0]
inp = np.array(parse_input(inp))


#part1(inp)
part2()

