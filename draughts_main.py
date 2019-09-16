import pygame, time
board = [
        ['0','r','0','r','0','r','0','r',],
        ['r','0','r','0','r','0','r','0',],
        ['0','r','0','r','0','r','0','r',],
        ['0','0','0','0','0','0','0','0',],
        ['0','0','0','0','0','0','0','0',],
        ['w','0','w','0','w','0','w','0',],
        ['0','w','0','w','0','w','0','w',],
        ['w','0','w','0','w','0','w','0',]
        ]

class counter:
    def __init__(counter, colour, value, rank):
        counter.colour = colour
        counter.value = value
        counter.rank = rank

    def possible_moves(piece):
        value = piece.value
        colour = piece.colour
        if colour == 'r':
            adj_mod = 1
        if colour == 'w':
            adj_mod = -1
        if colour == '0':
            return "no piece on this square"
        adjacent = [[value[0]+adj_mod,value[1]+1],[value[0]+adj_mod,value[1]-1]]
        possible_moves = adjacent
        for i in adjacent:
            for j in i:
                if ((int(j)>7) or (int(j)<0)):
                    possible_moves.remove(i)
        for i in possible_moves:
            if board[i[0]][i[1]].colour !='0':
                possible_moves.remove(i)
        return possible_moves

def piece_move(start, end):
    board[end[0]][end[1]] = board[start[0]][start[1]]
    board[start[0]][start[1]].value = end
    board[start[0]][start[1]] = counter('0',start,'p')
    
def board_assemble():
    for y in range(8):
        for x in range(8):
            board[y][x]= counter(board[y][x],[y,x],'p')

def board_draw(board):
    pygame.init()
    window_h = 722
    window_w = 722
    size = (window_w, window_h)
    screen = pygame.display.set_mode(size)
    pygame.display.set_caption("Draughts")
    background_image = pygame.image.load("draughts_board.gif").convert()
    screen.blit(background_image, [0, 0])
    for y in board:
        for x in y:
            if x.colour == 'r':
                pygame.draw.circle(screen,(255,0,0),((x.value[1]* 90) + 45,(x.value[0]* 90)+45),45,0)
            if x.colour == 'w':
                pygame.draw.circle(screen,(255,255,255),((x.value[1]* 90)+45,(x.value[0]* 90)+45),45,0)
    pygame.display.flip()

    dead=False
    while(dead==False):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                dead = True
            
    pygame.quit()

                                         
def possible_mover_finder(side):
    all_possible_moves = []                                         
    for y in board:
        for x in y:
           if x.colour == side:
               
              all_possible_moves.append(x.possible_moves())
              print(x)
              print(x.possible_moves())
    #print(all_possible_moves)
#def move_evaluator(move):

#def move_ranker(moves):

def game_init(side):
    board_assemble()
    board_draw(board)
    #call the move funcs on each other                                

count = 0
board_assemble()
#print(board[2][1].possible_moves())
possible_mover_finder('r')
#board_draw(board)
##while True:
##    board_draw(board, count)
##    if(count == 1):
##        piece_move([2,1], [3,0])
##    count += 1
##    time.sleep(1)
