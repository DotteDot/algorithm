#-*- coding: utf-8 -*-

#15684 사다리 조작.py

def make_map():
    result = [[0]*(x+1) for _ in range(y+2)]
    for _ in range(M):
        i, j = map(int, input().split())
        result[i][j] = j
        result[i][j+1] = j
    return result


def find():
    result = []
    for i in range(1, x):
        for j in range(1, y+1):
            if matrix[j][i] == 0 and matrix[j][i+1] == 0:
                result.append([i, j])
    return result


def down():
    for i in range(1, x):
        sx = i
        for j in range(1, y + 1):
            if matrix[j][sx]:
                if sx + 1 <= x and matrix[j][sx + 1] == matrix[j][sx]:
                    sx += 1
                elif matrix[j][sx - 1] == matrix[j][sx]:
                    sx -= 1

        if sx != i: return False
    return True


def dfs(cnt, idx, MIN):
    if cnt == MIN:
        return down()

    for i in range(idx, len(put_list)):
        nx, ny = put_list[i]
        if matrix[ny][nx] == 0 and matrix[ny][nx+1] == 0:
            matrix[ny][nx] = matrix[ny][nx+1] = nx
            if dfs(cnt + 1, idx + 1, MIN): return True
            matrix[ny][nx] = matrix[ny][nx+1] = 0


if __name__ == '__main__':
    x, M, y = map(int, input().split())
    if M == 0: print(0); exit()
    matrix = make_map()
    put_list = find()
    result = -1

    for i in range(4):
        if dfs(0, 0, i):
            result = i
            break

    print(result)