len_log = int(input())
str_log = input()
stack = []
result = 1

for log in str_log:
    try:
        if log.islower():
            stack.append(log)
        else:
            if log.lower() == stack.pop():
                continue
            else:
                result = 0
                break
    except:
        result = 0
        break
if stack:
    result = 0

print(result)