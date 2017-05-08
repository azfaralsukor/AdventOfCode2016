# from pprint import pprint

with open(r"d1.txt", "r") as myfile:
    data = myfile.read()

arr = data.split(', ')

# pprint(arr)

# arr = ['R8', 'R4', 'R4', 'R8']

direction = '^'
xaxis = 0
yaxis = 0
x_b4 = 0
y_b4 = 0
counter = 1

# Creates a list containing 5 lists, each of 8 items, all set to 0
w, h = 999, 999
Matrix = [[0 for x in range(w)] for y in range(h)]

for cmd in arr:
    x_b4 = xaxis
    y_b4 = yaxis
    if cmd[0] == 'L' and direction == '^':
        xaxis -= int(cmd[1:])
        direction = '<'
        condition_number = 1
    elif cmd[0] == 'R' and direction == '^':
        xaxis += int(cmd[1:])
        direction = '>'
        condition_number = 2
        for k in range((x_b4 + 1), (xaxis + 1)):
            if Matrix[k][yaxis] == 0:
                Matrix[k][yaxis] = 1
            elif Matrix[k][yaxis] == 1:
                print("(" + str(k) + ", " + str(yaxis) + ")")
                print(abs(k) + abs(yaxis))
                exit()
        print("^")
    elif cmd[0] == 'L' and direction == 'v':
        xaxis += int(cmd[1:])
        direction = '>'
        condition_number = 3
    elif cmd[0] == 'R' and direction == 'v':
        xaxis -= int(cmd[1:])
        direction = '<'
        condition_number = 4
        for k in range((x_b4 - 1), (xaxis - 1), -1):
            if Matrix[k][yaxis] == 0:
                Matrix[k][yaxis] = 1
            elif Matrix[k][yaxis] == 1:
                print("(" + str(k) + ", " + str(yaxis) + ")")
                print(abs(k) + abs(yaxis))
                exit()
        print("v")
    elif cmd[0] == 'L' and direction == '>':
        yaxis += int(cmd[1:])
        direction = '^'
        condition_number = 5
    elif cmd[0] == 'R' and direction == '>':
        yaxis -= int(cmd[1:])
        direction = 'v'
        condition_number = 6
        for k in range((y_b4 - 1), (yaxis - 1), -1):
            if Matrix[xaxis][k] == 0:
                Matrix[xaxis][k] = 1
            elif Matrix[xaxis][k] == 1:
                print("(" + str(xaxis) + ", " + str(k) + ")")
                print(abs(xaxis) + abs(k))
                exit()
        print(">")
    elif cmd[0] == 'L' and direction == '<':
        yaxis -= int(cmd[1:])
        direction = 'v'
        condition_number = 7
    elif cmd[0] == 'R' and direction == '<':
        yaxis += int(cmd[1:])
        direction = '^'
        condition_number = 8
        for k in range((y_b4 + 1), (yaxis + 1)):
            if Matrix[xaxis][k] == 0:
                Matrix[xaxis][k] = 1
            elif Matrix[xaxis][k] == 1:
                print("(" + str(xaxis) + ", " + str(k) + ")")
                print(abs(xaxis) + abs(k))
                exit()
        print("<")

    print(str(counter) + ". Direction: " + direction + " Command: " + cmd[0] + cmd[1:] + " (" + str(xaxis) + ", " + str(yaxis) + ") -- " + str(condition_number))
    counter += 1

print(abs(xaxis) + abs(yaxis))
