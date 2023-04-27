import sys

s = sys.stdin.read()
ls = [0]*26
for i in s:
    if i.islower():
        ls[ord(i)-97] += 1
for i in range(26):
    if ls[i] == max(ls):
        print(chr(97+i), end='')