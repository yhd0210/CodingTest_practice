def solution(number, k):
    ls = []
    for i in number:
        while k > 0 and ls and ls[-1] < i:
            ls.pop()
            k -= 1
        ls.append(i)
    return ''.join(ls[:len(ls) - k]) 