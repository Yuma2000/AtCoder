import statistics
from decimal import Decimal

N = int(input())
A = input().split()  # 空白区切りでリストに
dict = {}  # 数字が出できた回数を記録する辞書

for i, num in enumerate(A):
    A[i] = int(num)  # intにする
    if A[i] in dict:  # 辞書に存在したら
        dict[A[i]] += 1  # 出てきた回数を1プラスする
    else:  # 辞書に存在しなかったら
        dict[A[i]] = 1  # 辞書に1回で登録する

max_times = max(dict.values())  # 出てきた回数が最も多い数
max_times_num = max(dict, key=dict.get)  # 最頻値
median = statistics.median(A)  # 中央値

if max_times == dict[median]:
    print("a")
    maxtimes = dict[median]
    maxtimes_num = median
if max_times_num < median:
    if max_times < (Decimal(N) / Decimal(2) + Decimal(1)):
        print("Yes1")
    else:
        print("No")
elif max_times_num > median:
    if max_times < (Decimal(N) / Decimal(2)):
        print("Yes2")
    else:
        print("No")
else:
    if max_times < (Decimal(N) / Decimal(2) + Decimal(1)):
        if max_times_num == max(A):
            print("No")
        else:
            print("Yes3")
    else:
        print("No")
