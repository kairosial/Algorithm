unit_price_list = []
for _ in range(5):
    price = int(input())
    unit_price_list.append(price)

set_price_list = []
for burger in unit_price_list[0:3]:
    for beverage in unit_price_list[3:5]:
        set_price_list.append(burger + beverage - 50)

print(min(set_price_list))