import sys

N_M = input().split()
N = int(N_M[0])
M = int(N_M[1])
items = []
for i in range(N):
    item = list(map(int, input().split()))
    items.append(item)

for item_i in items:
    for item_j in items:
        if item_i == item_j:
            continue
        elif item_i[0] >= item_j[0]:
            i_func = item_i[2:]
            j_func = item_j[2:]
            if (set(i_func) < set(j_func)) or (set(i_func) == set(j_func) and item_i[0] > item_j[0]):
                print("Yes")
                sys.exit()

print("No")
