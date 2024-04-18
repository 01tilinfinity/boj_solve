N, M, x, y, K = map(int, input().split()) 
board = [list(map(int, input().split())) for _ in range(N)]  
commands = list(map(int, input().split()))  


dice = [0, 0, 0, 0, 0, 0]  

dx = [0, 0, -1, 1]
dy = [1, -1, 0, 0]

dice_x, dice_y = x, y


def roll_dice(direction):
    if direction == 1:  # 동쪽 이동
        dice[0], dice[2], dice[5], dice[3] = dice[3], dice[0], dice[2], dice[5]
    elif direction == 2:  # 서쪽 이동
        dice[0], dice[2], dice[5], dice[3] = dice[2], dice[5], dice[3], dice[0]
    elif direction == 3:  # 북쪽 이동
        dice[0], dice[1], dice[4], dice[5] = dice[4], dice[0], dice[5], dice[1]
    elif direction == 4:  # 남쪽 이동
        dice[0], dice[1], dice[4], dice[5] = dice[1], dice[5], dice[0], dice[4]


def move_dice(x, y, direction):
    global dice_x, dice_y

    nx, ny = x + dx[direction-1], y + dy[direction-1]  

    if 0 <= nx < N and 0 <= ny < M:  
        roll_dice(direction)
        if board[nx][ny] == 0:  
            board[nx][ny] = dice[5]  
        else:  
            dice[5] = board[nx][ny]  
            board[nx][ny] = 0  
        dice_x, dice_y = nx, ny  
        print(dice[0])  

for command in commands:
    move_dice(dice_x, dice_y, command)
