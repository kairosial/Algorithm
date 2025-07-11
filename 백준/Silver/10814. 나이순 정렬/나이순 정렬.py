import sys
n = int(sys.stdin.readline())
members = []
for i in range(n):
    age, name = sys.stdin.readline().split()
    member = [int(age), name, i]
    members.append(member)
members.sort(key=lambda member: (member[0], member[2]))
for age, name, _ in members:
    sys.stdout.write(f'{age} {name}\n')