import numpy as np


def calculate_sum(pattern, power_of_three):
    return np.sum(power_of_three * pattern)


T = int(input())
for _ in range(T):
    N, K = map(int, input().split())

    max_three_power = int(np.log(N) / np.log(3)) + 1
    power_of_three = np.power(3, np.arange(max_three_power))

    yes_flag = False
    pattern = np.zeros(K, dtype=int)
    for _ in range(3 ** K):
        if calculate_sum(pattern, power_of_three) == N:
            yes_flag = True
            break
        pattern[0] += 1
        for i in range(K - 1):
            if pattern[i] == 3:
                pattern[i] = 0
                pattern[i + 1] += 1

    if yes_flag:
        print("Yes")
    else:
        print("No")
