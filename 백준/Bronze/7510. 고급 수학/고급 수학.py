for i in range(int(input())):
    ls = sorted(map(int, input().split()))
    if ls[0]**2 + ls[1]**2 == ls[2]**2:
        print(f"Scenario #{i+1}:")
        print("yes\n")
    else:
        print(f"Scenario #{i+1}:")
        print("no\n")