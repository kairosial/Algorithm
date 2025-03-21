A = int(input())
B = int(input())
C = int(input())
num = A * B * C
num_list = [int(i) for i in str(num)]
num_dict = {0:0,
            1:0,
            2:0,
            3:0,
            4:0,
            5:0,
            6:0,
            7:0,
            8:0,
            9:0}
for i in num_list:
    num_dict[i] += 1
for c in num_dict.values():
    print(c)