start_h, start_m = map(int, input().split())
run_h, run_m = 0, int(input())

end_h = start_h + run_h
end_m = start_m + run_m

if end_m >= 60:
    run_h = end_m // 60
    end_h = start_h + run_h
    end_m = end_m % 60

if end_h >= 24:
    end_h = end_h % 24

print(end_h, end_m)