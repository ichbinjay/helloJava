import os

board = [['-' for i in range(10)] for j in range(10)]
snake = [(0,0)]
food = [(1,1),(0,5),(1,4)]
for i in food:
    board[i[0]][i[1]] = 'F'

board[0][0] = 'S'
print(*board,sep="\n")

print("To move the snake, enter a direction (w, a, s, d) and press enter.")
while True:
    choice = input("Enter a direction: ")
    os.system('cls')
    if choice == 'w':
        snakehead = (snakehead[0]-1,snakehead[1])
        snake.pop()
        snake.insert(0,snakehead)
    elif choice == 'a':
        snakehead = (snakehead[0],snakehead[1]-1)
        snake.pop()
        snake.insert(0,snakehead)
    elif choice == 's':
        snakehead = (snakehead[0]+1,snakehead[1])
        snake.pop()
        snake.insert(0,snakehead)
    elif choice == 'd':
        snakehead = (snakehead[0],snakehead[1]+1)
        snake.pop()
        snake.insert(0,snakehead)

    if snake[0] in food:
        food.remove(snake[0])
        new = (snake[-1][0],snake[-1][1])


    print(*board, sep='\n')




