while True:
    str_input = input()
    if str_input == '0':
        break
    elif str_input == str_input[::-1]:
        print('yes')
    else:
        print('no')