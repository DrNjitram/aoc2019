from codecs import open

def read_number_from_file(filepath, codec = "utf-8", split = None):
    if "C" not in filepath:
        filepath = "D:\\AdventOfCode2019\\probleminput\\" + filepath + ".txt"
    if split is None:
        with open(filepath, "r", codec) as file:
            file = file.readlines()
            try:
                lines = [int(i) for i in file]
            except ValueError:
                split = [i for i in file[0] if i not in "0123456789"][0]
                print("Did you mean to specify an seperator? Trying:", split)
                lines = [int(i) for i in file[0].split(split)]
    else:
        with open(filepath, "r", codec) as file:
            lines = [int(i) for i in file.readline().split(split)]
    return lines

def read_text_from_file(filepath, codec = "utf-8", split = None):
    if "C" not in filepath:
        filepath = "D:\\AdventOfCode2019\\probleminput\\" + filepath + ".txt"
    if split is None:
        with open(filepath, "r", codec) as file:
            lines = [line.strip() for line in file.readlines()]
    else:
        with open(filepath, "r", codec) as file:
            lines = [[j.strip() for j in i.split(",")] for i in file.readlines()]
    return lines

def flatten_list(n):
    nested_list = n[:]
    while nested_list:
        sublist = nested_list.pop(0)
        if isinstance(sublist, list):
            nested_list = sublist + nested_list
        else:
            yield sublist