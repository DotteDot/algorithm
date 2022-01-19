#-*- coding: utf-8 -*-

#23291 어항 정리.py


# fish 가 min 인 곳에 + 1
def _put_fish_min(lst) -> list:
    f_min = min(lst)

    for i in range(len(lst)):
        if lst[i] == f_min:
            lst[i] += 1
            # print(f'[LOG]\tdict[{i}] plus [1]')
    
    return lst


# bowl 을 균형에 맞게 쌓아올린다
# x, y 계산을 먼저 하고
# matrix에 fish를 분배한다.
# matrix를 반환한다.
def _make_bowl_matrix(f_list, row, col, cil) -> list:
    ewsn = {
        0 : (-1, 0), 1 : (0, -1),
        2 : (1, 0), 3 : (0, 1)
        }

    matrix = [[False] * row for _ in range(col)]            # 빈 matrix 만들기
    sx, sy = row - 1, col - 1
    now_ewsn = 0

    for i in reversed(range(N)):
        # print(f'[{now_ewsn}] now ({sx}, {sy}) put list[{i}] : {f_list[i]}')
        matrix[sy][sx] = f_list[i]

        for _ in range(2):
            nx = sx + ewsn[now_ewsn][0]
            ny = sy + ewsn[now_ewsn][1]
            # print(nx, ny)
            if now_ewsn == 2:
                if (0 <= nx < cil and 0 <= ny < col
                    and matrix[ny][nx] == False):
                    sx, sy = nx, ny
                    break
                else:
                    now_ewsn = (now_ewsn + 5) % 4

            else:
                if (0 <= nx < row and 0 <= ny < col
                    and matrix[ny][nx] == False):
                    sx, sy = nx, ny
                    break
                else:
                    now_ewsn = (now_ewsn + 5) % 4

    return matrix


# bowl 을 4층으로 쌓아올린다
# 반띵해서 올리고, 반띵해서 올린다
def _make_hhalfbowl_matrix(n, fishbowl_list) -> list:
    hhalf = n // 4
    matrix = []

    matrix.append(fishbowl_list[2 * hhalf:3 * hhalf][::-1])     # y = 0
    matrix.append(fishbowl_list[hhalf:2 * hhalf])               # y = 1
    matrix.append(fishbowl_list[:hhalf][::-1])                  # y = 2
    matrix.append(fishbowl_list[3 * hhalf:])                    # y = 3
    
    return matrix


# 주변 어항을 체크해서 알맞게 분배한다.
def _put_fish_balance(matrix, row, col) -> list:
    dx, dy = [0, 0, 1, -1], [1, -1, 0, 0]
    fish_temp = []

    for y in range(col):                                        # 내 주변을 비교해서
        for x in range(row):                                    # fish_temp에 저장
            for i in range(4):                                  #  .
                nx, ny = x + dx[i], y + dy[i]                   #  .
                if 0 <= nx < row and 0 <= ny < col:             #  .
                    # print(row, col, nx, ny, x, y)
                    # print(len(matrix))
                    # print(len(matrix[0]))
                    if matrix[ny][nx] != False and matrix[y][x] != False:
                        if matrix[y][x] > matrix[ny][nx]:       #  .
                            plus = (matrix[y][x] - matrix[ny][nx]) // 5
                            if plus > 0:
                                fish_temp.append([(x, y), -1 * plus])
                                fish_temp.append([(nx, ny), plus])


    for temp in fish_temp:                                      # 주변에 더해준다
        loc, plus = temp                                        #  .
        matrix[loc[1]][loc[0]] += plus                          # 여기까지

        # print(f'[LOG]\t({loc[0]}, {loc[1]}) give [{plus}]')

    return matrix


# 어항을 일렬로 내린다
def _make_bowl_line(matrix, row, col) -> list:
    lst = []
    # print(row, col)
    num = 0
    for x in range(row):
        for y in reversed(range(col)):
            if matrix[y][x] != False:
                lst.append(matrix[y][x])
                num += 1
    # print(lst)
    return lst




### ===  Strat  === ###
xy_dic = {
    4 : (2,2,2), 8 : (4,3,2), 12 : (3,4,3), 16 : (4,4,4), 20 : (4,5,4),
    24 : (8,5,4), 28 : (8,5,5), 32 : (7,6,5), 36 : (6,6,6), 40 : (10,6,6),
    44 : (8,7,6), 48 : (12,7,6), 52 : (10,7,7), 56 : (7,8,7), 60 : (11,8,7),
    64 : (8,8,8), 68 : (12,8,8), 72 : (8,9,8), 76 : (12,9,8), 80 : (16,9,8),
    84 : (12,9,9), 88 : (16,9,9), 92 : (11,10,9), 96 : (15,10,9), 100 : (10,10,10)
}
N, K = map(int, input().split())
fishbowl_list = list(map(int, input().split()))
cnt = 0
x, y, x1 = xy_dic[N][0], xy_dic[N][1], xy_dic[N][2]

# print(x, y)
# while 10 > cnt:
while max(fishbowl_list) - min(fishbowl_list) > K:
    cnt += 1
    # print(f'\n[{cnt}]')
    # fish 가 min 인 곳에 + 1
    fishbowl_list = _put_fish_min(fishbowl_list)
    # print('start : ', fishbowl_list)

    # bowl 을 균형에 맞게 쌓아올린다 = x, y를 구한다
    bowl_matrix = _make_bowl_matrix(fishbowl_list, x, y, x1)
    # print(x, y)
    # for i in range(y):
    #     print(bowl_matrix[i])

    # 내 주변 어항 체크해서 물고기를 분배한다
    bowl_matrix = _put_fish_balance(bowl_matrix, x, y)
    # for i in range(y):
    #     print(bowl_matrix[i])

    # 어항을 일렬로 내린다
    fishbowl_list = _make_bowl_line(bowl_matrix, x, y)
    # print('make bowl line')
    # print(fishbowl_list)

    # 반 반 해서 다시 쌓아 올린다.
    bowl_matrix = _make_hhalfbowl_matrix(N, fishbowl_list)
    # for i in range(4):
    #     print(bowl_matrix[i])

    # 내 주변 어항 체크해서 물고기를 분배한다
    bowl_matrix = _put_fish_balance(bowl_matrix, N // 4, 4)
    # for i in range(4):
    #     print(bowl_matrix[i])

    # 어항을 일렬로 내린다
    fishbowl_list = _make_bowl_line(bowl_matrix, N // 4, 4)
    # print('end : ', fishbowl_list)

    # break
    # print('Subtract : ',max(fishbowl_list) , min(fishbowl_list))
    # print()
print(cnt)