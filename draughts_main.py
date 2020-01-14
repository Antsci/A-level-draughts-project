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
                text_surface = font.render(str(x.value),True,(0, 255, 0))
                screen.blit(text_surface, loc)
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
    all_possible_moves = [x.possible_moves() for y in board for x in y if x.colour == side]
    removal_moves = [i for i in all_possible_moves if [] in i.values()]          
    for i in removal_moves:
            all_possible_moves.remove(i)
    return all_possible_moves



def move_evaluator(start, end, colour):
    end_pos = board[end[0]][end[1]]
    score = 0
    direction = [end[0]-start[0],end[1]-start[1]]
    print (direction)
    taken = take_in_direction(end_pos, direction)
    score = taken
    if colour == 'r' and end[0] == 7 and end_pos.colour == '0':
        score[0] += 4
    if colour == 'w' and end[0] == 0 and end_pos.colour == '0':
        score[0] += 4
    return score

def take_in_direction(end_pos, direction):
    final = board[end_pos.value[0] + direction[0]][ end_pos.value[1] + direction[1]]
    pieces_taken =[0,[],final]
    #check if any pieces can be taken from this position, in this direction
    if final.colour == '0' and end_pos.colour != '0':
        pieces_taken[0] += 1
        pieces_taken[1] = end_pos.value
    else:
        return 0
    return pieces_taken

def sorter(moves):
    #merge sort
    if len(moves) > 1:
        mid_point = len(moves) // 2
        left_half = moves[:mid_point]
        right_half = moves[mid_point:]
        sorter(left_half)
        sorter(right_half)
        i,j,k = 0,0,0
        while (i < len(left_half)) and (j < len(right_half)):
            if left_half[i][0] < right_half[j][0]:
                moves[k] = left_half[i]
                i += 1
            else:
                moves[k] = right_half[j]
                j += 1
            k += 1
        while i < len(left_half):
            moves[k] = left_half[i]
            i += 1
            k += 1
        while j < len(right_half):
            moves[k] = right_half[j]
            j += 1
            k += 1
    return moves


    
def game_init(side):
    board_assemble()
    board_draw(board)
    #call the move funcs on each other
    moves = possible_mover_finder(side)
    #loop through moves calling move_eval on each
    scores = []
    for i in moves:
        for x in i:
            for y in i[x]:
                scores.append(move_evaluator(x,y,side))
    #sort list made with sorter and return highest scoring move
    scores = sorter(scores)
    
    
    
#testing area
count = 0
board_assemble()
print(possible_mover_finder('r'))
moves = possible_mover_finder('r')
#loop through moves calling move_eval on each
scores = []
for i in moves:
    for x in i:
        for y in i[x]:
            print(x,y)
            scores.append(move_evaluator(x,y,'r'))
#sort list made with sorter and return highest scoring move

print(scores)
scores = sorter([[5,0,0],[6,0,0],[4,0,0],[3,0,0]])
print(scores)
while True:
    board_draw(board)
    pygame.quit()
    simple_piece_move([2,3], [3,2])
    simple_piece_move([3,2], [4,3])
    count += 1
    #move_evaluator((2,1),[3, 2],'w')
