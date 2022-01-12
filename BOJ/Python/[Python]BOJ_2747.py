lst = [0,1]
for _ in range(45):lst.append(lst[-1]+lst[-2])
print(lst[int(input())])