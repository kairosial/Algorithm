import sys
n = int(input())
power_strip = [int(sys.stdin.readline()) for _ in range(n)]
print(sum(power_strip) - len(power_strip) + 1)