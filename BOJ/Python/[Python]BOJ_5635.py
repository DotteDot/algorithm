import sys
input = sys.stdin.readline

N = int(input())
lst = list(input().split())

max_lst, min_lst = lst, lst
for _ in range(N-1):
    input_lst = list(input().split())
    
    max_flag, min_flag = 0, 0
    for i in range(1,4):
        if max_flag == 0:
            if int(input_lst[-1*i]) > int(max_lst[-1*i]):
                max_lst = input_lst
                max_flag = 1
            elif int(input_lst[-1*i]) < int(max_lst[-1*i]):
                max_flag = 1
        if min_flag == 0:
            if int(input_lst[-1*i]) < int(min_lst[-1*i]):
                min_lst = input_lst
                min_flag = 1
            elif int(input_lst[-1*i]) > int(min_lst[-1*i]):
                min_flag = 1

print(max_lst[0])
print(min_lst[0])