word = input()
new_word = ''
for s in word:
    if s.isupper():
        new_word += s.lower()
    else:
        new_word += s.upper()
print(new_word)