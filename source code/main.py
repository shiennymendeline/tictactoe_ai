import tictactoe as tao
import random

def main():

  tao.initBoard()

  print("\nTIC TAC TOE")
  print("created By Shienny Mendeline Hadi")
  print("===========")
  #ask input character
  player = input("choose your character (X, O or other character): ").upper()[0]

  #set pawn AI
  ai = tao.getPawn(player)

  print("You : ", player, "\nAI : ", ai)

  #show loading progress
  print("randoming who will be the first..")

  #random the turn
  turn =random.choice([ai, player])

  #show who is the first
  print("it's {n}'s turn".format( n=turn ))

  print("\nGAME START NOW")
  print("================")
  #for the first time I add random position, so user can have a chance win at some case
  if turn == ai:
    selected_square = int(random.random()*(tao.length-1))
    print(ai," choose ", (selected_square+1))

    tao.addPawnToSquare(selected_square, ai)
    turn = player

  #game stops when somebody wins or all squares are filled
  while(not tao.gameOver()):
    tao.drawMap()

    if turn == ai:
      tao.findBestPosition(ai)
      turn = player
    else:
      while True:
        try:
          #ask for user input, and then -1 so match with indexing array that starts from 0
          selected_square = input("choose slot (1-{last}): ".format(last=tao.length))
          selected_square = int( selected_square ) - 1

          #make sure the input is not out of range
          if selected_square >= 0 and selected_square < tao.length: 
            #make sure the selected square is empty, and add the pawn to the square
            if tao.isEmptySlot(selected_square):
              break
            else:
              print("this slot already filled")
          else:
              print("Invalid Number, Please Type Numeric only (1-{last})".format(last=tao.length))
        except ValueError:
          print("Invalid input, Please Type Numeric only (1-{last})".format(last=tao.length))
      
      tao.addPawnToSquare(selected_square, player)
      turn = ai
  
  #the display for game over
  print("\nGAME OVER")
  print("=========")
  tao.drawMap()
  print("=========")
  print(tao.getWinStatus())
  print("created By Shienny Mendeline Hadi")

main()