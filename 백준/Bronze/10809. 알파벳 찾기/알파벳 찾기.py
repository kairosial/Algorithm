S = input()
alphabet_dict = {chr(97+i): -1 for i in range(26)}
for i, s in enumerate(S):
    if s in alphabet_dict and alphabet_dict[s] == -1:
        alphabet_dict[s] = i
print(*list(alphabet_dict.values()))