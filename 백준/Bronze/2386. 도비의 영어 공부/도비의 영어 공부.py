import sys
while True:
    line = sys.stdin.readline().strip()
    if line == '#':
        break
    alphabet, sentence = line[:1], line[2:]
    result = 0
    for s in sentence:
        if (alphabet == s) or (alphabet.upper() == s):
            result += 1
    sys.stdout.write(f'{alphabet} {result}\n')