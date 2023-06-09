from collections import Counter

a, b = Counter(input()), Counter(input())
result = sum((a - b).values()) + sum((b - a).values())

print(result)