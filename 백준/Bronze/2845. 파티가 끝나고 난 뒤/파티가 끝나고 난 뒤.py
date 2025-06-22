head, area = map(int, input().split())
actual = head * area
predict_list = list(map(int, input().split()))
diff_list = list(map(lambda x: x - actual, predict_list))
print(*diff_list)