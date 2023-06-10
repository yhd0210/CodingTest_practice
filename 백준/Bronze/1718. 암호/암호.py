txt, k = input(), input()
a = ''
for i in range(len(txt)):
    if txt[i] == ' ': a += ' '
    else: a += chr((ord(txt[i]) - ord(k[i%len(k)]) - 1) % 26 + ord('a'))
print(a)