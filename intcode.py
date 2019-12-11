def get_output(init_inst, inp = 0, inst_pnt = 0, rel_offset = 0, debug = False):
    init_inst += [0] * 4000
    output_buffer = []
    cnt = 0
    while init_inst[inst_pnt] != 99:
        cnt += 1
        instruction = init_inst[inst_pnt]
        positionals = str(instruction)[:-2][::-1].ljust(3, "0")
        instruction = instruction % 100

        if debug:
            pos_2 = ""
            pos_3 = ""

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

        if debug:
            if pos_2 != "" and pos_3 != "":
                print(positionals, instruction, init_inst[inst_pnt + 1], pos_1,init_inst[inst_pnt + 2], pos_2, init_inst[inst_pnt + 3], pos_3, inp, rel_offset)
            elif pos_2 != "":
                print(positionals, instruction, init_inst[inst_pnt + 1], pos_1,init_inst[inst_pnt + 2], pos_2, inp, rel_offset)
            else:
                print(positionals, instruction, init_inst[inst_pnt + 1], inp, rel_offset)

        if instruction == 1:
            init_inst[pos_3] = pos_1 + pos_2
            inst_pnt += 4
        elif instruction == 2:
            init_inst[pos_3] = pos_1 * pos_2
            inst_pnt += 4
        elif instruction == 3:
            if inp != -1:
                if positionals[0] == "2":
                    pos_1 = init_inst[inst_pnt + 1] + rel_offset
                else:
                    pos_1 = init_inst[inst_pnt + 1]

                init_inst[pos_1] = inp
                inp = -1
                inst_pnt += 2
            else:
                return init_inst, inst_pnt, output_buffer, -1, rel_offset, True
            #print(positionals, instruction, pos_1, inp, rel_offset, init_inst[pos_1])

        elif instruction == 4:
            if debug:
               print("Output:", pos_1)
            output_buffer.append(pos_1)
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
            rel_offset += pos_1
            inst_pnt += 2

    return init_inst, inst_pnt, output_buffer, init_inst[0], rel_offset, False