# from collections import deque

# dx, dy = [0,0,1,-1,1,1,-1,-1], [1,-1,0,0,1,-1,1,-1]
# N, M, K = map(int, input().split())
# matrix = [[5]*N for _ in range(N)]
# fertilizer = [list(map(int, input().split())) for _ in range(N)]
# trees = [[deque() for _ in range(N)] for _ in range(N)]

# for i in range(M):
#     x, y, age = map(int, input().split())
#     trees[y-1][x-1].append(age)

# for y in range(K):
#     tree_idx = []
#     for i in range(N):
#         for j in range(N):
#             dead = 0
#             for idx in reversed(range(len(trees[i][j]))):
#                 tree = trees[i][j][idx]
#                 if matrix[i][j] >= tree:
#                     matrix[i][j] -= tree
#                     trees[i][j][idx] += 1
#                     if [j,i] not in tree_idx: tree_idx.append([j,i])
#                 else:
#                     dead += trees[i][j].popleft() // 2
#             matrix[i][j] += fertilizer[i][j] + dead

#     if not len(tree_idx):
#         break

#     for tree in tree_idx:
#         j, i = tree
#         for t in range(len(trees[i][j])):
#             if trees[i][j][t] % 5 == 0:
#                 for d in range(8):
#                     nx, ny = j + dx[d], i + dy[d]
#                     if 0 <= nx < N and 0 <= ny < N:
#                         trees[ny][nx].append(1)
# cnt = 0
# for i in range(N):
#     for j in range(N):
#         cnt += len(trees[i][j])
# print(cnt)


#-*- coding: utf-8 -*-

#16235 나무 재테크.py

from collections import deque

N, M, K = map(int, input().split())
matrix = []
fertilizer = []
trees = []

for _ in range(N):
    matrix.append([5]*N)
    fertilizer.append(list(map(int, input().split())))
    trees.append([deque() for _ in range(N)])

for i in range(M):
    x, y, age = map(int, input().split())
    trees[y-1][x-1].append(age)
    trees[y-1][x-1] = deque(sorted(trees[y-1][x-1]))


for y in range(K):

    # Spring
    tree_idx = []
    flag = True
    for i in range(N):
        for j in range(N):
            dead = 0
            for idx in range(len(trees[i][j]))[::-1]:
                if matrix[i][j] >= trees[i][j][idx]:
                    matrix[i][j] -= trees[i][j][idx]
                    trees[i][j][idx] += 1
                    flag = False
                    if trees[i][j][idx] % 5 == 0:
                        tree_idx.append([j,i])
                else:
                    for dd in range(idx+1):
                        dddd = trees[i][j].popleft()
                        dead += dddd // 2
                    break
            matrix[i][j] += fertilizer[j][i] + dead
    # print('SPRING END')

    if flag: break

    # Autumn
    # print('AUTUMN')
    for j, i in tree_idx:
        for dx, dy in [[0,1],[0,-1],[1,0],[-1,0],[1,1],[1,-1],[-1,1],[-1,-1]]:
            nx, ny = j + dx, i + dy
            if 0 <= nx < N and 0 <= ny < N:
                trees[ny][nx].append(1)
    # print('AUTUMN END')
    

cnt = 0
for i in range(N):
    for j in range(N):
        cnt += len(trees[i][j])
print(cnt)