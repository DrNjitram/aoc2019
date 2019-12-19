from boilerplates import read_number_from_file

def fuel_needed(number):
    return (number // 3) - 2

def calculate_fuel(weight):
    total_fuel = 0
    fuel = fuel_needed(weight)
    while fuel > 0:
        total_fuel += fuel
        fuel = fuel_needed(fuel)
    return total_fuel


filename = r"D:\AdventOfCode2019\probleminput\day1.txt"

from codecs import open

numbers = [int(i) for i in open(filename).readlines()]

#numbers = read_number_from_file(filename)

answer = sum([calculate_fuel(module) for module in numbers])

print(answer)