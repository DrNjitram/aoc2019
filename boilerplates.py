from codecs import open

def read_number_from_file(filepath, codec = "utf-8", split = None):
    if split == None:
        with open(filepath, "r", codec) as file:
            lines = [int(i) for i in file.readlines()]
    else:
        with open(filepath, "r", codec) as file:
            lines = [int(i) for i in file.readline().split(split)]
    return lines
