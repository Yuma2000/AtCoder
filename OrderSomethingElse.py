N_P_Q = input().split()
D = map(int, input().split())
N = int(N_P_Q[0])
P = int(N_P_Q[1])
Q = int(N_P_Q[2])
minimam = P - Q
for num in D:
    if num < minimam:
        minimam = num
print(Q + minimam)
