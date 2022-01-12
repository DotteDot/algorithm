result = 0
for i in range(1,int(input())+1):
    for j in range(1,i+1):
        result += j
print(result*3)