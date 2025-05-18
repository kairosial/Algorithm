while True:
    name, age, weight = input().split()
    age = int(age)
    weight = int(weight)
    group = 'Junior'
    if name == '#' and age == 0 and weight == 0:
        break
    if age > 17 or weight >= 80:
        group = 'Senior'
    print(name, group)