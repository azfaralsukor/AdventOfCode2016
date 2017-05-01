# from pprint import pprint

with open(r"d1.txt", "r") as myfile:
    data = myfile.read()

arr = data.split(', ')

# pprint(arr)

# arr = ['R5', 'L5', 'R5', 'R3']

direction = '^'
xaxis = 0
yaxis = 0
counter = 1

# Creates a list containing 5 lists, each of 8 items, all set to 0
w, h = 999, 999
Matrix = [[0 for x in range(w)] for y in range(h)]

for cmd in arr:
    if cmd[0] == 'L' and direction == '^':
        xaxis -= int(cmd[1:])
        direction = '<'
        condition_number = 1
    elif cmd[0] == 'R' and direction == '^':
        xaxis += int(cmd[1:])
        direction = '>'
        condition_number = 2
    elif cmd[0] == 'L' and direction == 'v':
        xaxis += int(cmd[1:])
        direction = '>'
        condition_number = 3
    elif cmd[0] == 'R' and direction == 'v':
        xaxis -= int(cmd[1:])
        direction = '<'
        condition_number = 4
    elif cmd[0] == 'L' and direction == '>':
        yaxis += int(cmd[1:])
        direction = '^'
        condition_number = 5
    elif cmd[0] == 'R' and direction == '>':
        yaxis -= int(cmd[1:])
        direction = 'v'
        condition_number = 6
    elif cmd[0] == 'L' and direction == '<':
        yaxis -= int(cmd[1:])
        direction = 'v'
        condition_number = 7
    elif cmd[0] == 'R' and direction == '<':
        yaxis += int(cmd[1:])
        direction = '^'
        condition_number = 8
    print(str(counter) + ". Direction: " + direction + " Command: " + cmd[0] + cmd[1:] + " (" + str(xaxis) + ", " + str(yaxis) + ") -- " + str(condition_number))
    counter += 1

# print(xaxis)
# print(yaxis)

print(abs(xaxis) + abs(yaxis))
