while True:
    input_str = input()
    if input_str == '.':
        break
    stack = []
    result = 'yes'
    for c in input_str:
        if c == '(' or c == '[':
            stack.append(c)
        if c == ')':
            if not stack or stack[-1] != '(':
                result = 'no'
                break
            stack.pop()
        if c == ']':
            if not stack or stack[-1] != '[':
                result = 'no'
                break
            stack.pop()
    if stack:
        result = 'no'
    print(result)