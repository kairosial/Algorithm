t = int(input())
apartment = [list(i for i in range(1, 15))]
for i in range(1, 15):
    floor = []
    for j in range(14):
        floor.append(sum(apartment[i-1][:j+1]))
    apartment.append(floor)

for _ in range(t):
    k = int(input())
    n = int(input())
    print(apartment[k][n-1])