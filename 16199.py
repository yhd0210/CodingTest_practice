y1, m1, d1 = map(int, input().split())
y2, m2, d2 = map(int, input().split())
if m1 < m2:
    year1 = y2 - y1
elif m1 == m2 and d1 <= d2:
        year1 = y2-y1
else:
    year1 = y2-y1-1
year2 = y2-y1+1
year3 = y2-y1
print(year1, year2, year3, sep="\n")