import calendar
ls = ["MON", "TUE", "WED", "THU", "FRI", "SAT", "SUN"]
x, y = map(int,input().split())
D = calendar.weekday(2007, x, y)
print(ls[D])