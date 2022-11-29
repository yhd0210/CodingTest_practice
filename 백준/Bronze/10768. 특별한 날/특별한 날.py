n1 = int(input())
n2 = int(input())
if n1 < 2:
    print("Before")    
elif n1 == 2:
    if n2 == 18: 
        print("Special")
    elif n2 > 18: 
        print("After")
    else: 
        print("Before")        
else: 
    print("After")
