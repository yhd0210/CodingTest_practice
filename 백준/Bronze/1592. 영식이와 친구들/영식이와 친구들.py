N, M, L = map(int, input().split())
ls = [0] * N
cnt = 0; i =0

while ls[i] < M-1:
    ls[i] += 1
    cnt += 1
    i = (i+L)%N if ls[i]%2 == 1 else (i-L)%N
    
print(cnt)