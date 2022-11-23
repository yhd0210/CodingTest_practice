import sys
n, s = sys.stdin.readline().split()

for i in range(2,int(s)):
    if(int(n) % i == 0):
        print("BAD", i)
        exit()
        
print("GOOD")