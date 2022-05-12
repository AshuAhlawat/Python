def queensAttackPattern(n, k, r_q, c_q, obstacles):
    board = [[" " for i in range(n)] for j in range(n)]
    for obstacle in obstacles:
        x,y = obstacle
        board[x-1][y-1] = "X"
    x, y = r_q-1, c_q-1
    board[x][y] = "Q"
        
    left = 0 
    right = 0
    bot = 0
    top = 0

    t_r = 0
    t_l = 0
    b_r = 0
    b_l = 0
    # left
    for j in range(y-1,-1,-1):
        if board[x][j]=="X":
            break
        else:
            left+=1
            board[x][j]="o"

        
    # right
    for j in range(y+1,n):
        if board[x][j]=="X":
            break
        else:
            right+=1
            board[x][j]="o"
    # top
    for i in range(x-1,-1,-1):
        if board[i][y]=="X":
            break
        else:
            top+=1
            board[i][y]="o"
    # bottom
    for i in range(x+1,n):
        if board[i][y]=="X":
            break
        else:
            bot+=1
            board[i][y]="o"
    
    # top-right
    for i,j in zip(range(x-1,-1,-1), range(y+1,n)):
        if board[i][j]=="X":
            break
        else:
            t_r+=1
            board[i][j]="o"
    
    # top-left
    for i,j in zip(range(x-1,-1,-1), range(y-1,-1,-1)):
        if board[i][j]=="X":
            break
        else:
            t_l+=1
            board[i][j]="o"
            
    # bottom-right
    for i,j in zip(range(x+1,n), range(y+1,n)):
        if board[i][j]=="X":
            break
        else:
            b_r+=1
            board[i][j]="o"
            
    # bottom-left
    for i,j in zip(range(x+1,n), range(y-1,-1,-1)):
        if board[i][j]=="X":
            break
        else:
            b_l+=1
            board[i][j]="o"

    # for row in board:
    #     for cell in row:
    #         print(cell, end = " ")
    #     print("")

    print(t_l, top , t_r)
    print(left , " ", right)
    print(b_l, bot, b_r)

    moves = top + bot + left + right + t_l + t_r + b_l + b_r

    return moves

def queensAttackValue(n, k, q_x, q_y, obstacles):
    moves = 0
    
    x_diff = abs(n - q_x)
    y_diff = abs(n - q_y)
    
    min_left = q_y-1
    min_right = y_diff
    
    min_top = q_x-1
    min_bot = x_diff
    
    
    min_top_left = min(min_top, min_left)
    min_top_right = min(min_top, y_diff)
    
    min_bot_left = min(x_diff,min_left)
    min_bot_right = min(x_diff, y_diff)
    
    for obstacle in obstacles:
        x,y = obstacle
        
        x_diff = q_x - x
        y_diff = q_y - y
        
        if x_diff == 0:
            # left
            if y < q_y:
                temp = y_diff -1
                if temp<min_left:
                    min_left = temp
            # right
            else:
                temp = -1*y_diff - 1
                if temp<min_right:
                    min_right = temp
        elif y_diff == 0:
            # top
            if x < q_x:
                temp = x_diff - 1
                if temp<min_top:
                    min_top = temp
            # bottom
            else:
                temp = -1*x_diff - 1
                if temp<min_bot:
                    min_bot = temp
        elif abs(x_diff) == abs(y_diff):
            temp = abs(x_diff) - 1
            if x_diff>0:
                if y_diff>0:
                    # top left
                    if temp< min_top_left:
                        min_top_left = temp
                else:
                    # top right
                    if temp< min_top_right:
                        min_top_right = temp
            else:
                if y_diff > 0:
                    # bot left
                    if temp< min_bot_left:
                        min_bot_left = temp
                else:
                    # bot right
                    if temp< min_bot_right:
                        min_bot_right = temp
        else:
            pass
    
    left = min_left  
    right = min_right
    
    top = min_top
    bottom = min_bot
    
    top_left = min_top_left
    top_right = min_top_right
    
    bot_left = min_bot_left
    bot_right = min_bot_right

    print(top_left, top , top_right)
    print(left , " ", right)
    print(bot_left, bottom, bot_right)
    
    
    moves += left + right + top + bottom + top_left + top_right + bot_left + bot_right
    
    return moves

obs = '''48 36
38 46
60 24
70 14
54 36
54 24
60 30
48 30
71 50
14 97
47 31
29 68
90 10
36 85
63 24
32 13
64 57
45 57
86 19
43 86
68 72
29 25
48 59
38 78
45 16
40 92
76 85
40 10
65 16
71 18
90 40
65 45
10 37
19 82
42 56
46 60
94 14
34 36
95 49
78 67
86 23
28 12
95 57
38 19
61 49
67 42
28 25
38 28
91 20
90 86
81 19
18 43
29 69
36 20
72 75
39 50
17 92
48 25
20 79
82 57
58 50
94 70
17 19
73 20
45 12
19 89
45 12
59 74
63 71
32 23
67 85
24 25
18 61
97 50
70 37
30 10
39 90
75 58
58 34
47 62
28 28
79 34
73 80
93 36
25 45
48 75
42 13
18 69
35 21
18 87
57 19
26 92
94 34
84 48
61 95
62 89
59 74
50 40
36 37
95 62'''

obs = obs.split("\n")

for i in range(len(obs)):
    obs[i] = list(map(int,obs[i].split(" ")))

# x = queensAttackPattern(100, 100, 54, 30, obs)
# print(x)
x = queensAttackValue(100, 100, 54, 30, obs)
print(x)