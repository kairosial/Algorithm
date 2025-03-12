import sys
# sys.stdin.readline() 대신 readlines() 이용하여 입력을 한번에 읽어와서 처리
input = sys.stdin.readlines()
N = int(input[0].strip())
card_list = list(map(int, input[1].strip().split()))
M = int(input[2].strip())
target_list = list(map(int, input[3].strip().split()))

count_dict = {}
for num in card_list:
    # 이전 코드에서는 list.count()를 이용했지만, 이 방식은 리스트를 순회하며 요소를 세기 때문에 리스트의 길이에 비례하여 시간이 소요됨
    # 수정 코드에서는 딕셔너리 값을 증가시키는 방식을 사용하므로, 리스트를 한 번만 순회함
    if num in count_dict:
        count_dict[num] += 1 # 기존 딕셔너리 값 증가
    else:
        count_dict[num] = 1 # 새로운 값 초기화

# 이전 코드에서는 딕셔너리에 특정 키가 없는 상황에 대응하기 위해 try-except 구문을 적용했었지만
# 수정 코드에서는 dict.get(num, 0)을 사용하여 키가 존재하지 않으면 0을 반환하도록 처리
result = [count_dict.get(num, 0) for num in target_list]

print(*result)