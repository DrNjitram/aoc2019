from boilerplates import read_number_from_file
import itertools

commands = read_number_from_file("day7", split=",")

def get_output(init_inst, inp, inst_pnt = 0):
    # inputs = [input_strength, phase_setting]
    tmp = 0
    cnt = 0
    while init_inst[inst_pnt] != 99:
        cnt += 1
        instruction = init_inst[inst_pnt]
        positionals = str(instruction)[:-2][::-1] + "00"
        instruction = instruction % 100

        if positionals[0] == "1":
            pos_1 = init_inst[inst_pnt + 1]
        else:
            pos_1 = init_inst[init_inst[inst_pnt + 1]]

        if instruction not in [3, 4]:
            if positionals[1] == "1" :
                pos_2 = init_inst[inst_pnt + 2]
            else:
                pos_2 = init_inst[init_inst[inst_pnt + 2]]

        #print(positionals, instruction, pos_1, inp)

        if instruction == 1:
            init_inst[init_inst[inst_pnt + 3]] = pos_1 + pos_2
            inst_pnt += 4
        elif instruction == 2:
            init_inst[init_inst[inst_pnt + 3]] = pos_1 * pos_2
            inst_pnt += 4
        elif instruction == 3:
            if inp != -1:
                init_inst[init_inst[inst_pnt + 1]] = inp
                inp = -1
                inst_pnt += 2
            else:
                return init_inst, inst_pnt, tmp, False
        elif instruction == 4:
            #print("Output:", pos_1)
            tmp = pos_1

            inst_pnt += 2
        elif instruction == 5:
            inst_pnt = pos_2 if pos_1 != 0 else inst_pnt + 3
        elif instruction == 6:
            inst_pnt = pos_2 if pos_1 == 0 else inst_pnt + 3
        elif instruction == 7:
            init_inst[init_inst[inst_pnt + 3]] = 1 if pos_1 < pos_2 else 0
            inst_pnt += 4
        elif instruction == 8:
            init_inst[init_inst[inst_pnt + 3]] = 1 if pos_1 == pos_2 else 0
            inst_pnt += 4

    return init_inst, inst_pnt, tmp, True

def solution():
    max_str = 0
    permutations = itertools.permutations([5, 6, 7, 8, 9])
    for permutation in permutations:
        phase_memory = [commands[:], commands[:], commands[:], commands[:], commands[:]]

        pnt, values = [0, 0, 0, 0, 0], [0, 0, 0, 0, 0]

        for i, phase in enumerate(permutation):
            phase_memory[i], pnt[i], values[i], halt = get_output(phase_memory[i], phase, pnt[i])

        i = 0
        while True:
            phase_memory[i], pnt[i], values[i], halt = get_output(phase_memory[i], values[i - 1], pnt[i])
            if halt and i == 4:
                break
            i = (i + 1) % 5

        max_str = max(max_str, values[i - 1])

    return max_str

from timeit import timeit
print(solution())
print(timeit(solution, number=10)/10)