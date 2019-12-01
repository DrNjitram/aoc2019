from codecs import open

def read_number_from_file(filepath, codec = "utf-8"):
    with open(filepath, "r", codec) as file:
        lines = [int(i) for i in file.readlines()]
    return lines
