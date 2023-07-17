H_W = input().split()
H = int(H_W[0])
W = int(H_W[1])

cookie_numDict = {}
cookie_hight_list = []
for h in range(W):
    cookie_hight_list.append(0)
for i in range(H):
    line = input()

    if '#' not in line:
        continue

    cookie_counter = 0
    for h, grid in enumerate(line):
        if grid == '#':
            cookie_counter += 1
            cookie_hight_list[h] += 1

    cookie_numDict[i] = cookie_counter

ansH = min(cookie_numDict, key=cookie_numDict.get) + 1
ansW = 0
max_num = max(cookie_hight_list)
for i, num in enumerate(cookie_hight_list):
    if num != 0 and num != max_num:
        ansW = i + 1
print(str(ansH) + ' ' + str(ansW))
