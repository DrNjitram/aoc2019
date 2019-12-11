from boilerplates import read_number_from_file
from time import time

from intcode import get_output

def get_output2(init_inst, v1, v2):
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

desired = 19690720
program  = read_number_from_file("day2", split=",")

def old_sol(inst):
    for i in range(0, 99):
        for j in range(0, 99):
            inst[1] = i
            inst[2] = j
            output = get_output(inst, debug=True)
            if output == desired:
                print(a * 100 + b)
                exit()



time_0 = time()

#old_sol(program[:])
pr = program[:]
pr[1] = 12
pr[2] = 2
print(get_output(pr[:])[1:])
pr[1] = 64
pr[2] = 72
print(get_output(pr[:])[1:])
exit()

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



