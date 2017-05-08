with open(r"d2.txt", "r") as myfile:
    data = myfile.read()

arr = data.split('\n')

current = 5

# [1 2 3] [(0, 2) (1, 2), (2, 2)]
# [4 5 6] [(0, 1) (1, 1), (2, 1)]
# [7 8 9] [(0, 0) (1, 0), (2, 0)]

for input in range(0, 5):
    for x in range(0, len(arr[input])):
        if current == 1:
            if arr[input][x] == 'U':
                pass
            elif arr[input][x] == 'D':
                current = 4
            elif arr[input][x] == 'R':
                current = 2
            elif arr[input][x] == 'L':
                pass
        elif current == 2:
            if arr[input][x] == 'U':
                pass
            elif arr[input][x] == 'D':
                current = 5
            elif arr[input][x] == 'R':
                current = 3
            elif arr[input][x] == 'L':
                current = 1
        elif current == 3:
            if arr[input][x] == 'U':
                pass
            elif arr[input][x] == 'D':
                current = 6
            elif arr[input][x] == 'R':
                pass
            elif arr[input][x] == 'L':
                current = 2
        elif current == 4:
            if arr[input][x] == 'U':
                current = 1
            elif arr[input][x] == 'D':
                current = 7
            elif arr[input][x] == 'R':
                current = 5
            elif arr[input][x] == 'L':
                pass
        elif current == 5:
            if arr[input][x] == 'U':
                current = 2
            elif arr[input][x] == 'D':
                current = 8
            elif arr[input][x] == 'R':
                current = 6
            elif arr[input][x] == 'L':
                current = 4
        elif current == 6:
            if arr[input][x] == 'U':
                current = 3
            elif arr[input][x] == 'D':
                current = 9
            elif arr[input][x] == 'R':
                pass
            elif arr[input][x] == 'L':
                current = 5
        elif current == 7:
            if arr[input][x] == 'U':
                current = 4
            elif arr[input][x] == 'D':
                pass
            elif arr[input][x] == 'R':
                current = 8
            elif arr[input][x] == 'L':
                pass
        elif current == 8:
            if arr[input][x] == 'U':
                current = 5
            elif arr[input][x] == 'D':
                pass
            elif arr[input][x] == 'R':
                current = 9
            elif arr[input][x] == 'L':
                current = 7
        elif current == 9:
            if arr[input][x] == 'U':
                current = 6
            elif arr[input][x] == 'D':
                pass
            elif arr[input][x] == 'R':
                pass
            elif arr[input][x] == 'L':
                current = 8

        if (x + 1) == len(arr[input]):
            print(current, end='')
