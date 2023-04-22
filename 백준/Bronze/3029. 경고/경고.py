hour_1, min_1, sec_1 = map(int, input().split(':'))
hour_2, min_2, sec_2 = map(int, input().split(':'))
time_1 = hour_1*60*60 + min_1*60 + sec_1
time_2 = hour_2*60*60 + min_2*60 + sec_2
time = time_2 - time_1 if time_2 > time_1 else time_2-time_1+24*60*60
hour = time//60//60
minute = time//60 % 60
sec= time%60
print("%02d:%02d:%02d" % (hour, minute, sec))