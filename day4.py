def check_number(str_no):
    if str_no[0] <= str_no[1] <= str_no[2] <= str_no[3] <= str_no[4] <= str_no[5]:
        if str_no[0] == str_no[1] != str_no[2] or str_no[0] != str_no[1] == str_no[2] != str_no[3] or str_no[1] != str_no[2] == str_no[3] != str_no[4] or str_no[2] != str_no[3] == str_no[4] != str_no[5] or str_no[3] !=  str_no[4] == str_no[5]:
            return 0, 1
        elif str_no[0] == str_no[1] or str_no[1] == str_no[2] or str_no[2] == str_no[3] or str_no[3] == str_no[4] or str_no[4] == str_no[5]:
            return 1, 0
    return 0, 0

amount_1, amount_2 = 0, 0
for i in range(125730, 579381 + 1):
    result = check_number(str(i))
    amount_1 += result[0]
    amount_2 += result[1]

print("Part 1:", amount_2)
print("Part 2:", amount_2 + amount_1)


