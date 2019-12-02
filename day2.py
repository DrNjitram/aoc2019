from boilerplates import read_number_from_file
from time import time

def get_output(init_inst, v1, v2):
    init_inst[1] = v1
    init_inst[2] = v2

    inst_pnt = 0

    while init_inst[inst_pnt] != 99:
        instruction = init_inst[inst_pnt]
        if instruction == 1:
            init_inst[init_inst[inst_pnt + 3]] = init_inst[init_inst[inst_pnt + 1]] + init_inst[init_inst[inst_pnt + 2]]
        if instruction == 2:
            init_inst[init_inst[inst_pnt + 3]] = init_inst[init_inst[inst_pnt + 1]] * init_inst[init_inst[inst_pnt + 2]]
        inst_pnt += 4

    return init_inst[0]

def get_factors(x):
   for i in range(1, x//2):
       if x % i == 0:
           if i < 100 and x/i < 100:
               return i

def old_sol(inst):
    prev = 0
    for i in range(0, 99):
        for j in range(0, 99):
            # with 0, 0 we get 4320
            a = i  # adds 307200 to output
            b = j  # add one to output
            # output = 4320 + a * b * 3076
            output = get_output(inst[:], a, b)
            #print(a, b, output, output - prev)
            prev = output
            if output == desired:
                print(a * 100 + b)
                exit()

desired = 19690720
program  = read_number_from_file(r"D:\Downloads\day2.txt", split=",")
#program  = read_number_from_file(r"D:\AdventOfCode2019\probleminput\day2.txt", split=",")

time_0 = time()

print("Part 1:")
print(get_output(program[:], 12, 2))
print(time() - time_0)
time_0 = time()

print("Part 2:")
prev_solution = 0

base_no = get_output(program[:], 0, 0)
multiplier = get_output(program[:], 1, 0) - base_no
if multiplier is not 0:
    # format is base + a * multiplier_1 + b * multiplier_2
    multiplier_2 = get_output(program[:], 0, 1) - base_no
    a = ((desired - base_no) // multiplier) // multiplier_2
    b = (desired - base_no) % multiplier
else: # format = base + a * b * multiplier
    multiplier = get_output(program[:], 1, 1) - base_no
    base_no = (desired - base_no)//multiplier
    a = get_factors(base_no)
    b = base_no//a

print(get_output(program[:], a, b))
print(a, b)
print(time() - time_0)



