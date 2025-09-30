import sys
scores_str = sys.stdin.read()
scores = list(map(int, scores_str.split()))
science = scores[:4]
science.remove(min(science))

society = scores[4:]
society.remove(min(society))

print(sum(science) + sum(society))