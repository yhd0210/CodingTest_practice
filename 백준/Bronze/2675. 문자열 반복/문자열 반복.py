for i in range(int(input())):
    cnt, string=input().split()
    s=list(string)
    result=[]
    for j in s:
        result.append(j * int(cnt))
    for k in result:
        print(k, end="")
    print()