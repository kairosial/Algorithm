triangle = [int(input()) for _ in range(3)]

if sum(triangle) != 180:
    print('Error')
elif len(set(triangle)) == 1:
    print('Equilateral')
elif len(set(triangle)) == 2:
    print('Isosceles')
elif len(set(triangle)) == 3:
    print('Scalene')