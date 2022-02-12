#-*- coding: utf-8 -*-

#20061 모노미노도미노 2.py

def green_move(t, x, y_min):
    if t == 1:
        for i in range(10):
            if green[i][x]:
                green[i-1][x] = 1
                return i-1, min(y_min, i-1)
        else:
            green[9][x] = 1
            return 9, min(y_min, 9)
    
    if t == 2:
        for i in range(10):
            if green[i][x] or green[i][x+1]:
                green[i-1][x] = green[i-1][x+1] = 1
                return i-1, min(y_min, i-1)
        else:
            green[9][x] = green[9][x+1] = 1
            return 9, min(y_min, 9)
    
    if t == 3:
        for i in range(10):
            if green[i][x]:
                green[i-1][x] = green[i-2][x] = 1
                return i-2, min(y_min, i-2)
        else:
            green[9][x] = green[8][x] = 1
            return 8, min(y_min, 8)


# flag : 0 -> 가득찬 줄이 없다
# flag : 1 -> 가득찬 줄이 한칸이고, 한칸 위를 당겨온다
# flag : 2 -> 가득찬 줄이 한칸이고, 두칸 위를 당겨온다
# flag : 3 -> 가득찬 줄이 두줄이고, 두칸 위를 당겨온다
def green_full(t, y):
    global score
    idx_len = 2 if t == 3 else 1
    flag = 0
    for i in range(idx_len):
        if 0 not in green[y+i]:
            flag += 1+i
            score += 1
            for j in range(4):
                green[y+i][j] = 0
    return flag


# flag : 0 -> 가득찬 줄이 없다
# flag : 1 -> 가득찬 줄이 한칸이고, 한칸 위를 당겨온다
# flag : 2 -> 가득찬 줄이 한칸이고, 두칸 위를 당겨온다
# flag : 3 -> 가득찬 줄이 두줄이고, 두칸 위를 당겨온다
def green_down(flag, y):
    # print(flag, y)
    for u in range(1, y):
        if flag == 1 or flag == 2:
            up = y - u + flag - 1
            put = y + 1 - u + flag - 1
        elif flag == 3:
            up = y - u
            put = y + 2 - u
        else:
            return

        cnt = 0
        for x in range(4):
            if green[up][x] == 0:
                cnt += 1
            green[put][x] = green[up][x]
            green[up][x]  = 0
        if cnt == 4:
            break


def blue_move(t, y, x_min):
    if t == 1:
        for i in range(10):
            if blue[y][i]:
                blue[y][i-1] = 1
                return i-1, min(x_min, i-1)
        else:
            blue[y][9] = 1
            return 9, min(x_min, 9)
    
    if t == 2:
        for i in range(10):
            if blue[y][i]:
                blue[y][i-1] = blue[y][i-2] = 1
                return i-2, min(x_min, i-2)
        else:
            blue[y][9] = blue[y][8] = 1
            return 8, min(x_min, 8)
    
    if t == 3:
        for i in range(10):
            if blue[y][i] or blue[y+1][i]:
                blue[y][i-1] = blue[y+1][i-1] = 1
                return i-1, min(x_min, i-1)
        else:
            blue[y][9] = blue[y+1][9] = 1
            return 9, min(x_min, 9)


def blue_full(t, x):
    global score
    idx_len = 2 if t == 2 else 1
    flag = 0
    for i in range(idx_len):
        for j in range(4):
            if not blue[j][x+i]:
                break
        else:
            flag += 1+i
            score += 1
            for j in range(4):
                blue[j][x+i] = 0

    return flag


def blue_down(flag, x):
    for u in range(1, x):
        if flag == 1 or flag == 2:
            up = x - u + flag - 1
            put = x + 1 - u + flag - 1
        elif flag == 3:
            up = x - u
            put = x + 2 - u
        else:
            return

        cnt = 0
        for y in range(4):
            if blue[y][up] == 0:
                cnt += 1
            blue[y][put] = blue[y][up]
            blue[y][up]  = 0
        if cnt == 4:
            break


def board_count():
    result = 0
    for i in range(6,10):
        for j in range(4):
            if blue[j][i] == 1:
                result += 1
            if green[i][j] == 1:
                result += 1
    return result


if __name__=="__main__":
    global score
    score = 0
    green = [[0]*4 for _ in range(10)]
    blue = [[0]*10 for _ in range(4)]

    for _ in range(int(input())):
        t, y, x = map(int, input().split())
        y_min, x_min = 9, 9
        
        # GREEN START
        idx_y, y_min = green_move(t, x, y_min)
        flag_y = green_full(t, idx_y)
        green_down(flag_y, idx_y)

        if flag_y == 1 or flag_y == 2: y_min += 1
        elif flag_y == 3: y_min += 2

        if y_min == 4: green_down(3, 8)
        elif y_min == 5: green_down(1, 9)
        # for m in range(10):
        #     print(green[m])

        #=========    BLUE START   =========
        idx_x, x_min = blue_move(t, y, x_min)
        flag_x = blue_full(t, idx_x)
        blue_down(flag_x, idx_x)

        if flag_x == 1 or flag_x == 3: x_min += 1
        elif flag_x == 2: x_min += 2

        if x_min == 4: blue_down(3, 8)
        elif x_min == 5: blue_down(1, 9)
        # for m in range(4):
        #     print(blue[m])

    print(score)
    print(board_count())