#-*- coding: utf-8 -*-

#17825 주사위 윷놀이.py

def check(h1_lst, h2_lst, h3_lst, h4_lst):
    h1, h1_ln = h1_lst
    h2, h2_ln = h2_lst
    h3, h3_ln = h3_lst
    h4, h4_ln = h4_lst

    # [1]
    # 시작과 끝이 아닐때 동일한 지점에 있으면 안된다.
    if ((h1_lst == h2_lst and lane[h1_ln][h1]) or (h2_lst == h3_lst and lane[h2_ln][h2]) or (h3_lst == h4_lst and lane[h3_ln][h3]) or
        (h1_lst == h3_lst and lane[h1_ln][h1]) or (h2_lst == h4_lst and lane[h2_ln][h2]) or (h1_lst == h4_lst and lane[h1_ln][h1])):
        return False
    
    # [2]
    # 40은 red, blue10, blue20, blue30에서 올 수 있으므로 체크해줘야함.
    # 왜냐하면 받아올 때 [idx, lane]로 받아오기 때문.
    # 25는 blue10, blue20, blue30에서 올 수 있으므로 체크해줘야함.
    if ((lane[h1_ln][h1] == lane[h2_ln][h2] and (lane[h1_ln][h1] == 25 or lane[h1_ln][h1] == 40)) or
        (lane[h1_ln][h1] == lane[h3_ln][h3] and (lane[h1_ln][h1] == 25 or lane[h1_ln][h1] == 40)) or
        (lane[h1_ln][h1] == lane[h4_ln][h4] and (lane[h1_ln][h1] == 25 or lane[h1_ln][h1] == 40)) or
        (lane[h2_ln][h2] == lane[h3_ln][h3] and (lane[h2_ln][h2] == 25 or lane[h2_ln][h2] == 40)) or
        (lane[h2_ln][h2] == lane[h4_ln][h4] and (lane[h2_ln][h2] == 25 or lane[h2_ln][h2] == 40)) or
        (lane[h3_ln][h3] == lane[h4_ln][h4] and (lane[h3_ln][h3] == 25 or lane[h3_ln][h3] == 40))):
        return False
    
    # [3]
    # 2번과 유사한 이유로 30, 35, 40을 체크해 줘야한다.
    # blue10, blue20, blue30에서 올 수 있으므로.
    if ((h1_ln != 'red' and h2_ln != 'red' and lane[h1_ln][h1] == lane[h2_ln][h2] and lane[h1_ln][h1]) or
        (h1_ln != 'red' and h3_ln != 'red' and lane[h1_ln][h1] == lane[h3_ln][h3] and lane[h1_ln][h1]) or
        (h1_ln != 'red' and h4_ln != 'red' and lane[h1_ln][h1] == lane[h4_ln][h4] and lane[h1_ln][h1]) or
        (h2_ln != 'red' and h3_ln != 'red' and lane[h2_ln][h2] == lane[h3_ln][h3] and lane[h2_ln][h2]) or
        (h2_ln != 'red' and h4_ln != 'red' and lane[h2_ln][h2] == lane[h4_ln][h4] and lane[h2_ln][h2]) or
        (h3_ln != 'red' and h4_ln != 'red' and lane[h3_ln][h3] == lane[h4_ln][h4] and lane[h3_ln][h3])):
        return False
    return True


# [1] check해서 통과하지 못하면 반환
# [2] round가 10이면 MAX 구하기
# [3] horse1, horse2, horse3, horse4에 각각 전진시키기 위해 dfs를 돌림
# [3-1] horse1을 예로 들면 우선 끝지점에 없을때 전진시킨다.
# [3-2] 10일때, 20일때, 30일때 blue로 가도록 처리해준다
# [3-3] 각 lane의 값을 초과하면 도착에 가도록 처리
def dfs(h1_lst, h2_lst, h3_lst, h4_lst, round, score):
    global MAX

    # [1]
    if not check(h1_lst, h2_lst, h3_lst, h4_lst):
        return
    else:
        h1, h1_ln = h1_lst
        h2, h2_ln = h2_lst
        h3, h3_ln = h3_lst
        h4, h4_ln = h4_lst

    # [2]
    if round == 10:
        MAX = max(MAX, score)
        return 
    
    move = lst[round]

    # [3]
    # [3-1]
    if (h1_ln == 'red' and h1 == 21) or (h1_ln == 'blue10' and h1 == 8) or (h1_ln == 'blue30' and h1 == 8) or (h1_ln == 'blue20' and h1 == 7):pass
    else:
        # [3-2]
        if lane[h1_ln][h1] == 10 and h1_ln == 'red': l1 = 'blue10'; h1 = 0
        elif lane[h1_ln][h1] == 30 and h1_ln == 'red': l1 = 'blue30'; h1 = 0
        elif lane[h1_ln][h1] == 20 and h1_ln == 'red': l1 = 'blue20'; h1 = 0
        else: l1 = h1_ln
        # [3-3]
        if h1+move < len(lane[h1_ln]): 
            dfs([h1+move, l1], h2_lst, h3_lst, h4_lst, round+1, score + lane[l1][h1+move])
        else: 
            dfs([len(lane[h1_ln])-1, l1], h2_lst, h3_lst, h4_lst, round+1, score)
    
    if (h2_ln == 'red' and h2 == 21) or (h2_ln == 'blue10' and h2 == 8) or (h2_ln == 'blue30' and h2 == 8) or (h2_ln == 'blue20' and h2 == 7):pass
    else:
        pass
        if lane[h2_ln][h2] == 10 and h2_ln == 'red': l2 = 'blue10'; h2 = 0
        elif lane[h2_ln][h2] == 20 and h2_ln == 'red': l2 = 'blue20'; h2 = 0
        elif lane[h2_ln][h2] == 30 and h2_ln == 'red': l2 = 'blue30'; h2 = 0
        else: l2 = h2_ln
        if h2+move < len(lane[h2_ln]): 
            dfs(h1_lst, [h2+move, l2], h3_lst, h4_lst, round+1, score + lane[l2][h2+move])
        else: 
            dfs(h1_lst, [len(lane[h2_ln])-1, l2], h3_lst, h4_lst, round+1, score)
    
    if (h3_ln == 'red' and h3 == 21) or (h3_ln == 'blue10' and h3 == 8) or (h3_ln == 'blue30' and h3 == 8) or (h3_ln == 'blue20' and h3 == 7):pass
    else:
        pass
        if lane[h3_ln][h3] == 10 and h3_ln == 'red': l3 = 'blue10'; h3 = 0
        elif lane[h3_ln][h3] == 20 and h3_ln == 'red': l3 = 'blue20'; h3 = 0
        elif lane[h3_ln][h3] == 30 and h3_ln == 'red': l3 = 'blue30'; h3 = 0
        else: l3 = h3_ln
        if h3+move < len(lane[h3_ln]): 
            dfs(h1_lst, h2_lst, [h3+move, l3], h4_lst, round+1, score + lane[l3][h3+move])
        else: 
            dfs(h1_lst, h2_lst, [len(lane[h3_ln])-1, l3], h4_lst, round+1, score)
    
    if (h4_ln == 'red' and h4 == 21) or (h4_ln == 'blue10' and h4 == 8) or (h4_ln == 'blue30' and h4 == 8) or (h4_ln == 'blue20' and h4 == 7):pass
    else:
        pass
        if lane[h4_ln][h4] == 10 and h4_ln == 'red': l4 = 'blue10'; h4 = 0
        elif lane[h4_ln][h4] == 20 and h4_ln == 'red': l4 = 'blue20'; h4 = 0
        elif lane[h4_ln][h4] == 30 and h4_ln == 'red': l4 = 'blue30'; h4 = 0
        else: l4 = h4_ln
        if h4+move < len(lane[h4_ln]): 
            dfs(h1_lst, h2_lst, h3_lst, [h4+move, l4], round+1, score + lane[l4][h4+move])
        else: 
            dfs(h1_lst, h2_lst, h3_lst, [len(lane[h4_ln])-1, l4], round+1, score)
    

# 외곽으로 도는게 red ,  10에서 꺽이면 blue10
# 20에서 꺽이면 blue20 ,  30에서 꺽이면 blue30
if __name__=="__main__":
    global MAX
    MAX = 0
    lane = {
    'red' : [0, 2, 4, 6, 8, 10, 12, 14, 16, 18,
        20, 22, 24, 26, 28, 30, 32, 34, 36, 38,
        40, 0],
    'blue10' : [10, 13, 16, 19, 25, 30, 35, 40, 0],
    'blue20' : [20, 22, 24, 25, 30, 35, 40, 0],
    'blue30' : [30, 28, 27, 26, 25, 30, 35, 40, 0]
    }
    lst = list(map(int, input().split()))
    
    # 처음에 첫번째 말을 전진시켜서 경우를 조금 감소시킴
    if lst[0] == 5: dfs([5, 'red'], [0, 'red'], [0, 'red'], [0, 'red'], 1, 10)
    else: dfs([lst[0], 'red'], [0, 'red'], [0, 'red'], [0, 'red'], 1, lane['red'][lst[0]])

    print(MAX)