dict = {'A': 0, 'B': 3, 'C': 4, 'D': 8, 'E': 9, 'F': 14, 'G': 23}

p_q = input().split()
p = p_q[0]
q = p_q[1]
print(abs(dict[p] - dict[q]))
