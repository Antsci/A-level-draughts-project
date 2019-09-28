"""
Author: Isaac Antscherl
Description: A graphical implementation of english draughts(www.wikipedia.org/english_draughts) with a computer controlled opponent.
"""



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
        adjacent = [[value[0]+adj_mod,value[1]-1], [value[0]+adj_mod,value[1]+1]]
        possible_moves = adjacent
        removal_moves = []
        for i in adjacent:
            for j in i:
                if ((int(j)>7) or (int(j)<0)):
                    possible_moves.remove(i)
        removal_moves = [i for i in possible_moves if board[i[0]][i[1]].colour == colour]
        for i in removal_moves:
            possible_moves.remove(i)
        return {(value[0],value[1]):possible_moves}

def simple_piece_move(start, end):
    if board[start[0]][start[1]].colour == '0':
        return 
    board[end[0]][end[1]] = board[start[0]][start[1]]
    board[end[0]][end[1]].value = end
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
    font = pygame.font.Font(pygame.font.get_default_font(), 12)
    for y in board:
        for x in y:  
            loc = ((x.value[1]* 90) + 45,(x.value[0]* 90)+45)
            if x.colour == 'r':
                pygame.draw.circle(screen,(255,0,0),loc,45,0)
            if x.colour == 'w':
                pygame.draw.circle(screen,(0,0,255),loc,45,0)
            text_surface = font.render(str(x.value),True,(0, 255, 0))
            screen.blit(text_surface, loc)
    pygame.display.flip()

    dead=False
    while(dead==False):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                dead = True
            
    pygame.quit()

                                         
def possible_mover_finder(side):
    all_possible_moves = [x.possible_moves() for y in board for x in y if x.colour == side ]
    removal_moves = [i for i in all_possible_moves if [] in i.values()]          
    for i in removal_moves:
            all_possible_moves.remove(i)
    return all_possible_moves

def piece_taker_checker(end_pos, colour):
    #recursive search for potential moves
    if end_pos.colour != '0':
      if direction[1] == -1:
          if end_pos.value():
              pass
            
def move_evaluator(start, end, colour):
    end_pos = board[end[0]][end[1]]
    score = 0
    direction = [end[0]-start[0],end[1]-start[1]]
    print (direction)
    piece_taker_checker(position, colour)
          


#def move_ranker(moves):

def game_init(side):
    board_assemble()
    board_draw(board)
    #call the move funcs on each other
    
#testing area
count = 0
board_assemble()
print(possible_mover_finder('r'))
while True:
    board_draw(board)
    pygame.quit()
    simple_piece_move([2,3], [3,2])
    count += 1
    #move_evaluator((2,1),[3, 2],'w')
