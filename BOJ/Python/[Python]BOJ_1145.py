#-*- coding: utf-8 -*-

#1145 적어도 대부분의 배수.py

def gcd(x, y):
    if not x % y: return y
    else: return gcd(y, x % y)

a, b, c, d, e = map(int, input().split())
min_lcm = 9000000000
lst = [[a,b,c],[a,b,d],[a,b,e],[a,c,d],[a,c,e],[a,d,e],
        [b,c,d],[b,c,e],[b,d,e],[c,d,e]]

for i in lst:
    fi, se, th = i
    lcm = fi * se // gcd(fi, se)
    lcm = lcm * th // gcd(lcm, th)
    min_lcm = min(lcm, min_lcm)
print(min_lcm)