size = 3
win = False
length = pow(size,2)
emptySlotLeft = length
squares = []
depth = 3

SQUARE_EMPTY = "_"
PLAYER_PAWN = "X"
COMPUTER_PAWN = "O"

def initBoard(): #procedure
  "initiate board value"
  for i in range(length): 
    squares.append(SQUARE_EMPTY)

def getPawn( pawn_player ): #return a pawn (string)
  "make sure pawn AI is not the same character as player"
  global PLAYER_PAWN, COMPUTER_PAWN
  switcher = {
      PLAYER_PAWN : COMPUTER_PAWN,
      COMPUTER_PAWN : PLAYER_PAWN,
  }

  tmp = switcher.get(pawn_player, COMPUTER_PAWN)
  PLAYER_PAWN = pawn_player
  COMPUTER_PAWN = tmp

  return tmp

def drawMap(): #procedure
  "draw squares (map in the game)"
  drawTargetBoard(squares)

def drawTargetBoard(source): #procedure
  "draw the tic tac toe map based on source"
  ctr = 0 #index of the board
  for i in range(size): 
    for j in range(size):
      print(source[ctr], end=' ') 
      ctr+=1
    print("\n")

def isEmptySlot(index): #return bool
  "check if the selected slot in the board is empty "
  return (squares[index] == SQUARE_EMPTY)

def gameOver(): #return bool
  "game will be over based on these conditions"
  return win or (emptySlotLeft == 0)

def getWinStatus(): #return string
  "get string of winning status"
  if(isWinning(squares, PLAYER_PAWN)):
    return PLAYER_PAWN + " WIN"
  elif(emptySlotLeft == 0):
    return "TIE !"
  elif(isWinning(squares, COMPUTER_PAWN)):
    return COMPUTER_PAWN + " WIN"


def addPawnToSquare(index, pawn): #procedure
  "add the pawn to the board, and the check is any winning"
  global emptySlotLeft, win, squares
  squares[index] = pawn
  emptySlotLeft -= 1
  win = isWinning(squares, pawn)

def getIndicesEmptySquare(board): #return array
  "get list of empty slot (it will return list of indices not the values)"
  arr = []
  for i in range(length):
    if board[i] == SQUARE_EMPTY:
      arr.append(i)
  return arr

def findBestPosition(player): #procedure
  "find the best position using minimax"
  listPossibleMoves = getIndicesEmptySquare(squares)

  if len(listPossibleMoves) > 0:
    best_score = -1000
    best_move = listPossibleMoves[0]

    for index in listPossibleMoves:
      #clone the board, so changes to the copied variable will not affect the original variable
      current_board = squares.copy()
      current_board[index] = player

      score = minimax(current_board, False, 1, COMPUTER_PAWN, PLAYER_PAWN)

      #make sure the best move is based on the maximum score of all possible moves
      if best_score < score:
        best_score = score
        best_move = index

    #for the display, +1 so it's match with the game that start from 1-length not 0-(length-1)
    print(player," choose ", (best_move+1))
    addPawnToSquare(best_move, player)
  else:
    print("No moves found")

def minimax(board, isMaximize, current_depth, player, opponent):
  #TERMINAL STATE 1
  if isWinning(board, opponent):
    return -10 #OPPONENT WIN

  #TERMINAL STATE 2
  elif isWinning(board, player):
    return 10 #AI WIN
  
  listPossibleMoves = getIndicesEmptySquare(board)

  #TERMINAL STATE 3
  if len(listPossibleMoves) < 1:
    return 0 #DRAW

  #TERMINAL STATE 4
  if current_depth == depth:
    #calculate the evaluation function value
    opponent_cpw = countPossibleWins(board, player)
    player_cpw = countPossibleWins(board, opponent)
    eval_func = player_cpw - opponent_cpw
    
    return eval_func
  else:
    if isMaximize: #maximizing level
      best_score = -1000
      for index in listPossibleMoves:
        #clone the board, so changes to the copied variable will not affect the original variable
        current_board = board.copy() 
        current_board[index] = player
        
        #calculate the score for this move and compare it, so we can get the maximum value
        score = minimax(current_board, False, current_depth+1, player, opponent )
        best_score = max(best_score, score)
      
      return best_score
    else: #minimizing level
      best_score = 1000
      for index in listPossibleMoves:
        #clone the board, so changes to the copied variable will not affect the original variable
        current_board = board.copy()
        current_board[index] = opponent
        
        #calculate the score for this move and compare it, so we can get the minimum value
        score = minimax(current_board, True, current_depth+1, player, opponent )
        best_score = min(best_score, score)

      return best_score
    


def isWinning(board, player):
  "check is anybody win in this current state"
  #horizontal
  num = 0
  for i in range(size):
    j=0
    num = size*i
    status = True
    while(j<size and status):
      status = status and (board[num] == player)
      num+=1
      j+=1
    if status:
      return status
  
  #vertical
  for i in range(size):
    j=0
    num = i
    status = True
    while(j<size and status):
      status = status and (board[num] == player)
      num+=size
      j+=1
    if status:
      return status
  
  #left diagonal
  num = 0
  status = True
  for i in range(size):
    status = status and (board[num] == player)
    num = num + size + 1
  if status:
      return status

  #right diagonal
  num = size-1
  status = True
  for i in range(size):
    status = status and (board[num] == player)
    num = num + size - 1
  if status:
      return status
  
  return False

def countPossibleWins(board, opponent):
  "count how many possible wins for opponents' opponent"
  counter = 0
  #horizontal
  num = 0
  for i in range(size):
    j=0
    status = True
    while(j<size and status):
      status = status and (board[num] != opponent)
      num+=1
      j+=1
    if status:
      counter+=1
  
  #vertical
  for i in range(size):
    j=0
    num = i
    status = True
    while(j<size and status):
      status = status and (board[num] != opponent)
      num+=size
      j+=1
    if status:
      counter+=1
  
  #left diagonal
  num = 0
  status = True
  for i in range(size):
    status = status and (board[num] != opponent)
    num = num + size + 1
  if status:
      counter+=1

  #right diagonal
  num = size-1
  status = True
  for i in range(size):
    status = status and (board[num] != opponent)
    num = num + size - 1
  if status:
      counter+=1
  
  return counter
  