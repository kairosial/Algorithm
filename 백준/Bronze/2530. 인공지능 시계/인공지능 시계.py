fh, fm, fs = map(int, input().split())
cooking_time = int(input())

ns = cooking_time % 60
nm = (cooking_time // 60) % 60
nh = (cooking_time // 60) // 60

es = fs + ns
em = fm + nm
eh = fh + nh

if es >= 60:
    em += es // 60
    es = es % 60
if em >= 60:
    eh += em // 60
    em = em % 60
if eh >= 24:
    eh = eh % 24

print(eh, em, es)