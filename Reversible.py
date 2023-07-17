N = int(input())
strings = set()
for i in range(N):
    input_str = input()
    reverse_str = input_str[::-1]
    if input_str not in strings:
        strings.add(input_str)
        strings.add(reverse_str)
    if input_str == reverse_str:
        strings.add(input_str + "A")
print(len(strings) // 2)
