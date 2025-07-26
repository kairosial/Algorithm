import sys
N, M = map(int, sys.stdin.readline().split())

site_dict = {}
for _ in range(N):
    site, pw = sys.stdin.readline().strip().split()
    site_dict[site] = pw

site_list = []
for _ in range(M):
    search = sys.stdin.readline().strip()
    site_list.append(search)

for s in site_list:
    site_pw = site_dict[s]
    sys.stdout.write(f'{site_pw}\n')