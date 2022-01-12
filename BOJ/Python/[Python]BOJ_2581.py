a, b = int(input()), int(input())

lst = []
for i in range(a, b+1):
    flag = 0
    for j in range(2,i):
        if i % j == 0 and i != j:
            flag = 1
            break
    if flag == 0:
        lst.append(i)
if 1 in lst:
    del lst[0]
if lst:
    print(sum(lst))
    print(min(lst))
else:
    print(-1)