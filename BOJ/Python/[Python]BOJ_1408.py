#-*- coding: utf-8 -*-

#1408.py

import sys
input = sys.stdin.readline

now, end = input(), input()
now = int(now[:2])*3600 + int(now[3:5])*60 + int(now[6:])
end = int(end[:2])*3600 + int(end[3:5])*60 + int(end[6:])

result = end-now
if result < 0:
    result += 60*60*24
print('{0:02d}:{1:02d}:{2:02d}'.format(result // 3600, (result % 3600 // 60), result % 60))