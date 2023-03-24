ls = []
for _ in range(5) :
  ls.append(input())
f = 0
for i in range(len(ls)) :
  if 'FBI' in ls[i] :
    print(i+1, end=' ')
    f = 1
if f == 0 :
  print('HE GOT AWAY!')