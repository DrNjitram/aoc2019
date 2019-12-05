def check_number(str_no):
    if str_no[0] == str_no[1] != str_no[2] or str_no[0] != str_no[1] == str_no[2] != str_no[3] or str_no[1] != str_no[2] == str_no[3] != str_no[4] or str_no[2] != str_no[3] == str_no[4] != str_no[5] or str_no[3] !=  str_no[4] == str_no[5]:
        return 1, 1
    elif str_no[0] == str_no[1] or str_no[1] == str_no[2] or str_no[2] == str_no[3] or str_no[3] == str_no[4] or str_no[4] == str_no[5]:
        return 1, 0
    else:
        return 0, 0

def generate_arr(arr):
    arr_arr = [arr[0]] + [-1 if j < arr[i - 1] else j for i, j in enumerate(arr[1:])]
    arr_arr = [i for i in arr_arr if i > -1]
    arr_arr = arr_arr + [arr_arr[-1]]
    return arr_arr, len(arr_arr)

def solution():
    amounts_1, amounts_2 = 0, 0
    start = [1,2,5,7,3,0]
    end = [5,7,9,3,8,1]

    started = False

    start_arr, l_start_arr = generate_arr(start)
    end_arr, l_end_arr = generate_arr(end)

    for a in range(start[0], end[0] + 1):
        for b in range(a, 10):
            for c in range(b, 10):
                for d in range(c, 10):
                    for e in range(d, 10):
                        for f in range(e, 10):
                            numbers = [a, b, c, d, e, f]
                            if started or numbers[:l_start_arr] == start_arr:
                                started = True
                                result = check_number(numbers)
                                amounts_1 += result[0]
                                amounts_2 += result[1]

                                if numbers[:l_end_arr] == end_arr:
                                    #print("Part 1:", amounts_2)
                                    #print("Part 2:", amounts_1)
                                    return 0

#solution()
from timeit import timeit
print(timeit(solution, number=100)/100)