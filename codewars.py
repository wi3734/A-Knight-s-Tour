def knights_tour(start, size):
    chess_board = [[0 for num in range(size)] for each_row in range(size)] # generate a chess board
    chess_board[start[0]][start[1]] = 1 # start point
    current_pos = start 
    
    pos_moves_from_cur = []  # possible moves from the point
    
    history = [current_pos] # all the history in subsequent order
    
    while True:
        pos_moves_from_cur = find_the_moves(chess_board, current_pos)
        current_pos, chess_board = make_a_move(pos_moves_from_cur, chess_board)
        history.append(current_pos)

        if not 0 in [elem for row in chess_board for elem in row]: # check if the knight toured all the squares 
            break
    
    return history

def find_the_moves(chess_board, current_pos): # find the moves
    
    knight_moves = [(-2,1),(-1,2),(1,2),(2,1),(-2,-1),(-1,-2),(1,-2),(2,-1)] # all the possible moves
    number_moves = [] 
    
    for each_move in range(len(knight_moves)):
        check = tuple(map(sum, zip(knight_moves[each_move], current_pos)))
         
        if (check[0] >= 0 and check[1] >= 0) and (check[0] <= len(chess_board)-1 and check[1] <= len(chess_board)-1): # make sure the knight stays on the board
            if chess_board[check[0]][check[1]] == 0:
                number_moves.append((find_onward_moves(chess_board, check), check, each_move)) # each_move for set-ordering {1,2,3,4,5,6,7,8} for tie-breakers
                
            elif chess_board[check[0]][check[1]] == 1:
                pass

    number_moves.sort() 
    candidates = []
     
    for move in range(len(number_moves)): # adjacent numbers for the candidates with the fewest onward moves
        if number_moves[move][0] == number_moves[0][0]:
           candidates.append((find_the_adj(chess_board, number_moves[move][1]), number_moves[move]))
  
    candidates.sort()
    candidates = [cand for cand in candidates if cand[0] == candidates[0][0]]
    output = sorted(candidates, key=lambda x: x[-1]) # sort by the last element, set-ordering
    
    return output

def find_onward_moves(chess_board, possible_pos): # find the number of possible onward moves for each move

    knight_moves = [(-2,-1),(-1,-2),(1,-2),(2,-1),(2,1),(1,2),(-1,2),(-2,1)] # all the possible moves
    pos_moves = [] 

    for each_move in knight_moves:
        check = list(map(sum, zip(each_move, possible_pos)))
        
        if (check[0] >= 0 and check[1] >= 0) and (check[0] <= len(chess_board)-1 and check[1] <= len(chess_board)-1): # make sure the knight stays on the board
            if chess_board[check[0]][check[1]] != 1:
                pos_moves.append(check)

    return len(pos_moves)
    
def find_the_adj(chess_board, candidate): # adjacent numbers for tie-breakers
    candidates = [] 
    pos_num = list(range(len(chess_board))) 
    
    for cand in [(candidate[0], candidate[1]+1), (candidate[0], candidate[1]-1), (candidate[0]-1, candidate[1]), (candidate[0]+1, candidate[1])]:            
        if not cand[0] in pos_num:
            continue
        elif not cand[1] in pos_num:
            continue
        candidates.append(cand)
            
    candidates = list(set(candidates))        
    
    return len(['a' for each_cand in candidates if chess_board[each_cand[0]][each_cand[1]] == 0])

def make_a_move(pos_moves, chess_board):
    chess_board[pos_moves[0][1][1][0]][pos_moves[0][1][1][1]] = 1
    return pos_moves[0][1][1], chess_board


