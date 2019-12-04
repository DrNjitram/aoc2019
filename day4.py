def check_number(str_no):
    if str_no[0] == str_no[1] != str_no[2] or str_no[0] != str_no[1] == str_no[2] != str_no[3] or str_no[1] != str_no[2] == str_no[3] != str_no[4] or str_no[2] != str_no[3] == str_no[4] != str_no[5] or str_no[3] !=  str_no[4] == str_no[5]:
        return 1, 1
    elif str_no[0] == str_no[1] or str_no[1] == str_no[2] or str_no[2] == str_no[3] or str_no[3] == str_no[4] or str_no[4] == str_no[5]:
        return 1, 0
    else:
        return 0, 0

def solution():
    amounts_1, amounts_2 = 0, 0
    start = [1,2,5,7,3,0]
    end = [5,7,9,3,8,1]
    start_no = 125730
    end_no = 579381
    started = False


    start_arr = [start[0]] + [-1 if j < start[i - 1] else j for i, j in enumerate(start[1:])]
    start_arr = [i for i in start_arr if i > -1]
    start_arr = start_arr + [start_arr[-1]]

    end_arr = [end[0]] + [-1 if j < end[i - 1] else j for i, j in enumerate(end[1:])]
    end_arr = [i for i in end_arr if i > -1]
    end_arr = end_arr + [end_arr[-1]]



    for a in range(start[0], end[0] + 1):
        for b in range(a, 10):
            for c in range(b, 10):
                for d in range(c, 10):
                    for e in range(d, 10):
                        for f in range(e, 10):
                            if started or [a, b, c, d, e] == start_arr:
                                started = True
                                result = check_number([a, b, c, d, e, f])
                                amounts_1 += result[0]
                                amounts_2 += result[1]

                                if [a, b, c, d] == end_arr:
                                    #print("Part 1:", amounts_2)
                                    #print("Part 2:", amounts_1)
                                    return 0

#solution()
from timeit import timeit
print(timeit(solution, number=10000)/10000)
