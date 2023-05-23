N = int(input())
num = list(map(int, input().split()))
t = int(input())

num.append(0)
num.sort()

a = 0
for i in range(len(num)-1) :
    if num[i] == t or num[i+1] == t:
        a = 0
        break
    elif num[i] < t and t < num[i+1]:
        a = (t - num[i]) * (num[i+1] - t) - 1
        break

print(a)