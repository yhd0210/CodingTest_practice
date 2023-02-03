w = input().upper()
ls = list(set(w))
cnt = []
for i in ls:
  count = w.count
  cnt.append(count(i))

if cnt.count(max(cnt)) > 1:
  print("?")

else:
  print(ls[(cnt.index(max(cnt)))])