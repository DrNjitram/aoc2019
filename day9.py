from boilerplates import read_number_from_file

commands = read_number_from_file("day9", split=",")

commands += [0] * 2000

def get_output(init_inst, inp = 0, inst_pnt = 0):
    # inputs = [input_strength, phase_setting]
    tmp = 0
    cnt = 0
    rel_offset = 0
    while init_inst[inst_pnt] != 99:
        cnt += 1
        instruction = init_inst[inst_pnt]
        positionals = str(instruction)[:-2][::-1] + "00"
        instruction = instruction % 100

        if positionals[0] == "1":
            pos_1 = init_inst[inst_pnt + 1]
        elif positionals[0] == "2":
            pos_1 = init_inst[init_inst[inst_pnt + 1] + rel_offset]
        else:
            pos_1 = init_inst[init_inst[inst_pnt + 1]]

        if instruction not in [3, 4, 9]:
            if positionals[1] == "1" :
                pos_2 = init_inst[inst_pnt + 2]
            elif positionals[1] == "2":
                pos_2 = init_inst[init_inst[inst_pnt + 2] + rel_offset]
            else:
                pos_2 = init_inst[init_inst[inst_pnt + 2]]

            if instruction in [1, 2, 7, 8]:
                if positionals[2] == "1" :
                    pos_3 = inst_pnt + 3
                elif positionals[2] == "2":
                    pos_3 = init_inst[inst_pnt + 3] + rel_offset
                else:
                    pos_3 = init_inst[inst_pnt + 3]


        if instruction == 1:
            init_inst[pos_3] = pos_1 + pos_2
            inst_pnt += 4
        elif instruction == 2:
            init_inst[pos_3] = pos_1 * pos_2
            inst_pnt += 4
        elif instruction == 3:

            if positionals[0] == "1":
                pos_1 = init_inst[inst_pnt + 1]
            elif positionals[0] == "2":
                pos_1 = init_inst[inst_pnt + 1] + rel_offset
            else:
                pos_1 = init_inst[init_inst[inst_pnt + 1]]

            init_inst[pos_1] = inp

            #print(positionals, instruction, pos_1, inp, rel_offset, init_inst[pos_1])
            inst_pnt += 2

        elif instruction == 4:
            print("Output:", pos_1)
            tmp = pos_1
            inst_pnt += 2
        elif instruction == 5:
            inst_pnt = pos_2 if pos_1 != 0 else inst_pnt + 3
        elif instruction == 6:
            inst_pnt = pos_2 if pos_1 == 0 else inst_pnt + 3
        elif instruction == 7:
            init_inst[pos_3] = 1 if pos_1 < pos_2 else 0
            inst_pnt += 4
        elif instruction == 8:
            init_inst[pos_3] = 1 if pos_1 == pos_2 else 0
            inst_pnt += 4
        elif instruction == 9:
            #print(instruction, positionals, rel_offset, pos_1)
            rel_offset += pos_1

            inst_pnt += 2

    return init_inst, inst_pnt, tmp, True

output = get_output(commands, 1)
output = get_output(commands, 2)
