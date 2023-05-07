a = {'A', 'B', 'C', 'D', 'E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z'}

n = int(input())

for _ in range(n):
  ss = set(input()) 
  b = a-ss 
  hap = 0 
  for i in b: 
    hap += ord(i)
  print(hap)