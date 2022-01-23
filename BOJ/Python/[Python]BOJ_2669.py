#-*- coding: utf-8 -*-

#2669 직사각형 네개의 합집합의 면적 구하기.py

squares = [list(map(int, input().split())) for _ in range(4)]
matrix = [[False]*100 for _ in range(100)]

for square in squares:
    for y in range(square[1], square[3]):
        for x in range(square[0], square[2]):
            matrix[y][x] = True

result = 0
for line in matrix:
    result += line.count(True)
    
print(result)