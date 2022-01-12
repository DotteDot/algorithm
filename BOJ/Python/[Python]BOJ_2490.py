lst = ['E','A','B','C','D']
for _ in range(3):print(lst[list(map(int,input().split())).count(0)])