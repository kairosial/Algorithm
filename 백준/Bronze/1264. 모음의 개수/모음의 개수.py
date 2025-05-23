while True:
    s = input()
    if s == '#':
        break
    result = 0
    vowel = ['a', 'e', 'i', 'o', 'u', 'A', 'E', 'I', 'O', 'U']
    for i in s:
        if i in vowel:
            result += 1
    print(result)