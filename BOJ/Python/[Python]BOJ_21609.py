#-*- coding: utf-8 -*-

#21609 상어중학교.py

from collections import deque

# MAX: 부분의 최대 크기 (필요 없음)
# max_list: 최대가 되는 부분의 좌표 리스트
# mx_min: 기준블록의 행(x) -> 기준블록의 열
# my_min: 기준블록의 열(x) -> 기준블록의 행
# max_rainbow: 최대가 되는 부분의 rainbow개수
def find_bk_gp(n) -> int:
    check = [[False]*n for _ in range(n)]
    queue = deque()
    MAX = 0
    max_lst = []
    mx_min = my_min = n + 1
    max_rainbow = 0

    for i in range(n):
        for j in range(n):
            tmp = []
            rainbow = 0
            start = 0

            if (type(matrix[i][j]) == int and 
                matrix[i][j] > 0 and 
                check[i][j] == False):
                tmp.append((matrix[i][j], j, i))
                queue.append((j, i))
                check[i][j] = True
                start = matrix[i][j]

            # bfs
            while queue:
                x, y = queue.popleft()
                for d in range(4):
                    nx, ny = x + dx[d], y + dy[d]
                    if (0 <= nx < n and 0 <= ny < n and not check[ny][nx] and 
                        (matrix[ny][nx] == start or matrix[ny][nx] == 0)):
                        if matrix[ny][nx] == 0: rainbow += 1
                        tmp.append((matrix[ny][nx], nx, ny))
                        queue.append((nx, ny))
                        check[ny][nx] = True

            # 1
            # 무조건 새로들어오는애가 선택되는 경우
            # 1. 부분의 크기가 2 이상이면서 저장 되어있는 애보다 클때
            # 2. 길이가 같은데 rainbow가 저장 되어있는 애보다 더 많을때
            if (MAX < len(tmp) and len(tmp) >= 2) or (MAX == len(tmp) and max_rainbow < rainbow):
                tx_min = ty_min = n + 1
                for t in tmp:
                    if t[0] and tx_min > t[1]: tx_min = t[1]
                    if t[0] and ty_min > t[2]: ty_min = t[2]
                    # rainbow를 반환
                    if not t[0]: check[t[2]][t[1]] = False
                MAX, max_lst = len(tmp), tmp
                mx_min, my_min, max_rainbow = tx_min, ty_min, rainbow

            # 2
            # 새 부분의 크기와 rainbow가 같을때
            elif MAX == len(tmp) and len(tmp) >= 2 and max_rainbow == rainbow:
                tx_min = ty_min = n + 1
                for t in tmp:
                    if t[0] and tx_min > t[1]: tx_min = t[1]
                    if t[0] and ty_min > t[2]: ty_min = t[2]
                    # rainbow를 반환
                    if not t[0]: check[t[2]][t[1]] = False
                
                # 기준블록의 행이 제일 큰것을 찾아야함
                if ty_min > my_min:
                    MAX, max_lst = len(tmp), tmp
                    mx_min, my_min, max_rainbow = tx_min, ty_min, rainbow
                # 같다면 기준블록의 열이 제일 큰 것을 찾음
                elif ty_min == my_min:
                    if tx_min > mx_min:
                        MAX, max_lst = len(tmp), tmp
                        mx_min, my_min, max_rainbow = tx_min, ty_min, rainbow

            # 3
            # 위의 두 과정을 만족하지 않을 때 rainbow를 다시 반환하는 곳.
            # 최종적으로 여기를 안만들어줘서 틀렸다고 나왔음.
            elif tmp:
                for t in tmp:
                    # rainbow를 반환
                    if not t[0]: check[t[2]][t[1]] = False
    
    for _, x, y in max_lst:
        matrix[y][x] = '*'

    return len(max_lst) ** 2


def num_down(n):
    for x in range(n):
        qlist = [deque()]
        for y in range(n):
            if matrix[y][x] == '*':
                qlist[-1].appendleft('*')
            elif matrix[y][x] != '*' and matrix[y][x] > -1:
                qlist[-1].append(matrix[y][x])
            elif matrix[y][x] == -1:
                qlist[-1].append(-1)
                qlist.append(deque())
        y = 0
        for i in range(len(qlist)):
            while qlist[i]:
                matrix[y][x] = qlist[i].popleft()
                y += 1


def rotate_270():
   return list(reversed(list(map(list,zip(*matrix)))))


if __name__=="__main__":
    N, M = map(int, input().split())
    matrix = [list(map(int, input().split())) for _ in range(N)]
    dx, dy = [0,0,1,-1], [1,-1,0,0]
    result = 0
    
    while True:
        score = find_bk_gp(N)
        result += score
        if not score: print(result); break

        num_down(N)
        matrix = rotate_270()
        num_down(N)
