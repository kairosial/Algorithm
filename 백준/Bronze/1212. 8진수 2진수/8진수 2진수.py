oct = input()
if oct == '0':
    print('0')
else:
    oct_to_bin = ['000', '001', '010', '011', '100', '101', '110', '111']
    binary_parts = []
    binary_parts.append(bin(int(oct[0]))[2:])
    for o in oct[1:]:
        binary_parts.append(oct_to_bin[int(o)])
    print(''.join(binary_parts))