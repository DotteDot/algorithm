n = int(input())
for i in reversed(range(1,n+1)):
    for _ in range(n-i):
        print(' ', end='')
    for _ in reversed(range(1,i+1)):
        print('*', end='')
    print() 