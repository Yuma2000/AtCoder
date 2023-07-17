N_D = input().split()
N = int(N_D[0])
D = int(N_D[1])
D = D * D
x1 = 0
y1 = 0
for i in range(N):
  x_y = input().split()
  x = int(x_y[0])
  y = int(x_y[1])
  if i == 0:
    x1 = x
    y1 = y
    print("Yes")
  else:
    distance = (x1-x) ** 2 + (y1-y) ** 2
    if distance <= D:
      print("Yes")
    else:
      print("No")
