input_str = input()
input_int = int(input())

for idx, str in enumerate(input_str):
    if idx == input_int-1:
        print(str)