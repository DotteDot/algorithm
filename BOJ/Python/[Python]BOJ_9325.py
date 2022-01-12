import sys
input = sys.stdin.readline

for _ in range(int(input())):
    price = int(input())
    for _ in range(int(input())):
        a, b = map(int, input().split())
        price += a * b
    print(price)