from pprint import pprint

with open(r"d1.txt", "r") as myfile:
    data = myfile.read()

arr = data.split(', ')

# pprint(arr)

arr = ['R2', 'R2', 'R2']

direction = '^'
xaxis = 0
yaxis = 0

for cmd in arr:
    if cmd[0] == 'L' and direction == '^':
        xaxis -= int(cmd[1:])
        direction = '<'
    if cmd[0] == 'R' and direction == '^':
        xaxis += int(cmd[1:])
        direction = '>'
    if cmd[0] == 'L' and direction == 'v':
        xaxis += int(cmd[1:])
        direction = '>'
    if cmd[0] == 'R' and direction == 'v':
        xaxis -= int(cmd[1:])
        direction = '<'
    if cmd[0] == 'L' and direction == '>':
        yaxis += int(cmd[1:])
        direction = '^'
    if cmd[0] == 'R' and direction == '>':
        yaxis -= int(cmd[1:])
        direction = 'v'
    if cmd[0] == 'L' and direction == '<':
        yaxis -= int(cmd[1:])
        direction = 'v'
    if cmd[0] == 'R' and direction == '<':
        yaxis += int(cmd[1:])
        direction = '^'

print(xaxis)
print(yaxis)