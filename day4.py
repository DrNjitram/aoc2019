def check_number(no):
    str_no = str(no)
    if str_no[0] <= str_no[1] <= str_no[2] <= str_no[3] <= str_no[4] <= str_no[5]:
        if str_no[0] == str_no[1] or str_no[1] == str_no[2] or str_no[2] == str_no[3] or str_no[3] == str_no[4] or str_no[4] == str_no[5]:
            return 1
    return 0

def check_number_2(no):
    str_no = str(no)
    if str_no[0] <= str_no[1] <= str_no[2] <= str_no[3] <= str_no[4] <= str_no[5]:
        if str_no[0] == str_no[1] != str_no[2] or str_no[0] != str_no[1] == str_no[2] != str_no[3] or str_no[1] != str_no[2] == str_no[3] != str_no[4] or str_no[2] != str_no[3] == str_no[4] != str_no[5] or str_no[3] !=  str_no[4] == str_no[5]:
            return 1
    return 0

amount = 0
for i in range(125730, 579381 + 1):
    amount += check_number_2(i)

print(amount)