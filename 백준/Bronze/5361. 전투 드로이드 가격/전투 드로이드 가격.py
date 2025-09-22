n = int(input())
rifle = 350.34
vision_sensor = 230.90
hearing_sensor = 190.55
arm = 125.30
leg = 180.90
for _ in range(n):
    a, b, c, d, e = map(int, input().split())
    result = (a * rifle) + (b * vision_sensor) + (c * hearing_sensor) + (d * arm) + (e * leg)
    print(f'${result:.2f}')