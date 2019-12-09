from codecs import open

def read_number_from_file(filepath, codec = "utf-8", split = None):
    if "C" not in filepath:
        filepath = "D:\\AdventOfCode2019\\probleminput\\" + filepath + ".txt"
    if split is None:
        with open(filepath, "r", codec) as file:
            lines = [int(i) for i in file.readlines()]
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