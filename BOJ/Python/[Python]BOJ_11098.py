import sys
input = sys.stdin.readline

for _ in range(int(input())):
    cost, name = 0, ''

    for _ in range(int(input())):
        a, b = input().split()
        if cost < int(a):
            cost = int(a)
            name = b
    print(name)
