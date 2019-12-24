from intcode import get_output
from boilerplates import read_number_from_file, flatten_list

def parse_packets(q, info, n):
    for i in range(0, len(info), 3):
        if info[i] == 255:
            n = [info[i + 1], info[i + 2]]
        else:
            q[info[i]] += [info[i + 1], info[i + 2]]
        #print("Sending message", [info[i + 1], info[i + 2]], "to", info[i])
    return q, n

commands = read_number_from_file("day22", split=",")

def solution():
    total_computers = 50
    intcode_computers = []
    queues = [[] for i in range(total_computers)]

    for adress in range(total_computers):
        intcode_computers.append(get_output(commands[:], adress, 0, 0)) # commands, adress, pointer, relative offset

    NAT = [0, 0]
    last_val = None
    while True:
        for i in range(total_computers):
            cmd, pnt, buffer, end, reloff, halt = intcode_computers[i]

            if queues[i] == []:
                inp = -1
            else:
                inp = queues[i]
                queues[i] = []

            intcode_computers[i] = get_output(cmd, inp, pnt, reloff)

            if intcode_computers[i][2] != []:
                queues, NAT = parse_packets(queues, intcode_computers[i][2], NAT)

        if sum(flatten_list(queues)) == 0:
            if NAT[1] == last_val:
                return NAT[1]
            queues[0] = NAT[:]
            last_val = NAT[1]


from timeit import timeit

print(timeit(solution, number=100)/100)
