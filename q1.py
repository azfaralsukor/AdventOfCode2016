from pprint import pprint

with open (r"d1.txt", "r") as myfile:
    data=myfile.read()

arr = data.split(', ')

pprint(arr)

xaxis=0
yaxis=0

for cmd in arr:
	print(cmd[1:])
	if cmd[0] == 'L':
		xaxis +=1

print(xaxis)