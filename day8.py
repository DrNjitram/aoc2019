from boilerplates import read_text_from_file

f = read_text_from_file(r"D:\AdventOfCode2019\probleminput\day8.txt")
f =f[0]
width = 25
tall = 6
length = width * tall
layers = [f[i * length:(i+1) * length] for i in range(0,len(f)//length)]

zeros = layers[0].count("0")
answer =  layers[0].count("1") * layers[0].count("2")
for layer in layers:
	if layer.count("0") < zeros:
		answer = layer.count("1") * layer.count("2")
		zeros = layer.count("0")

print(answer)

for i in range(tall):
	row = ""
	for j in range(width):
		row += [layer[i*width + j] for layer in layers if layer[i*width + j] != "2"][0]
	print(row.replace("0"," ").replace("1", "#"))