for _ in range(int(input())):
	n = list(input())
	k = len(n)//2-1
	if n[k]==n[-k-1]:
		print('Do-it')
	else: print('Do-it-Not')