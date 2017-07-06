
import random

person = input('Enter your name: ')
print('Hello', person)

field = [[1, 2, 3],[4, 5, 6],[7, 8, 9]]

def printField():
    counter = 0;

    for i in field[:2]:
        for j in i[:2]:
            print(" ", j, " | ", end="")
        print(" ", field[counter][2])
        counter += 1
        print ("------------------")
    print (" ", field[2][0], " |  ", field [2][1], " |  ", field[2][2])
counter = 0;

#print (field [1][1]) #is 5
#printField()
#move = input ('Choose your move: ')

def switch(x):
    return {
        '1': [0, 0],
        '2': [0, 1],
        '3': [0, 2],
        '4': [1, 0],
        '5': [1, 1],
        '6': [1, 2],
        '7': [2, 0],
        '8': [2, 1],
        '9': [2, 2]
    }[x]

def populate(x, side):
    nums = switch(x)
    field[nums[0]][nums[1]] = side

#populate(move, 'x')

winnerPos = [["1", "2", "3"], ["1", "4", "7"], ["1", "5", "9"], ["4", "5", "6"], ["7", "8", "9"], ["2", "5", "8"], ["3", "6", "9"], ["3", "5", "7"]]

firstAdvantage = ["5", "1", "3", "7", "9"]

secondAdvantage = [["5", "1"], ["5", "3"], ["5", "7"], ["5", "9"], ["1", "3"], ["3", "9"], ["7", "9"], ["1", "7"]]

thirdAdvantage = [["1", "3", "5"], ["3", "5", "9"], ["7", "5", "9"], ["1", "5", "7"], ["1", "3", "9"], ["1", "3", "7"], ["7", "9", "3"], ["2", "4", "1"], ["2", "3", "6"], ["6", "9", "8"], ["4", "7", "8"]]


def think():
  if moveCounter == 0:
    answer = "5"
  elif moveCounter == 1:
    if userMoves[-1] == "5":
      answer = "1"
    else:
      answer = "5"
  else:
    answer = anticipateWin()
    if answer == "0":
      answer = anticipateUserWin()
    if answer == "0":
      answer = anticipateAdvantage()
    if answer == "0":
      answer = anticipateUserAdvantage()
  if answer == "0":
    answer = random.choice(moves)
  myMoves.append(answer)
  return answer

def anticipateWin():
  answer = "0"
  for lis in winnerPos:
    commonEl = set(myMoves) & set(lis)

    #for i in myMoves:
     # print("my moves: ", i)

    #for i in lis:
     # print("list item #", i)

    #for i in commonEl:
     # print ("common: ", i)

    if len(commonEl) > 1 :
      for el in lis:
        if el not in commonEl:
          if el in moves:
            answer = el
            break
            break

  return answer

def anticipateUserWin():
  answer = "0"
  for lis in winnerPos:
    commonUser = set(userMoves) & set(lis)

    if len(commonUser) > 1 :
      for el in lis:
        if el not in commonUser:
          for i in moves:
          if el in moves:
            answer = el
            break
            break
  return answer

def anticipateUserAdvantage():
  answer = "0"
  if len(userMoves) < 2:
    for lis in secondAdvantage:
      commonUser = set(userMoves) & set(lis)
      if len(commonUser) > 0 :
        for el in lis:
          if el not in commonUser:
            if el in moves:
              answer = el
              break
              break
  else:
    for lis in thirdAdvantage:
      commonUser = set(userMoves) & set(lis)

      if len(commonUser) > 1 :
        for el in lis:
          if el not in commonUser:
            if el in moves:
              answer = el
              break
              break

  return answer

def anticipateAdvantage():
  answer = "0"
  if len(myMoves) < 2:
    for lis in secondAdvantage:
      commonEl = set(myMoves) & set(lis)
      if len(commonEl) > 0 :
        for el in lis:
          if el not in commonEl:
            if el in moves:
              answer = el
              break
              break
  else:
    for lis in thirdAdvantage:
      commonEl = set(myMoves) & set(lis)

      if len(commonEl) > 1 :
        for el in lis:
          if el not in commonEl:
            if el in moves:
              answer = el
              break
              break

  return answer

      #if ((userMoves[-2] in lis) & (userMoves[-1] in lis) & (myMoves[-1] not in lis)):
      #  for el in lis:
      #    if ((el != userMoves[-2]) | (el != userMoves[-1])):
      #      answer = el



#switch (move)
printField()

#print (switch(move))
moveCounter = 0
matchOver = False

moves = ['1', '2', '3', '4', '5', '6', '7', '8', '9']

userMoves = [];
myMoves = [];

moveFirst = input("Who moves first... you or me?: ")

if (moveFirst == "you"):
  print ("My turn: ")

  if (len(moves) > 0):
    myMove = think()

  if (myMove in moves):
      moves.remove(myMove)
  else:
      print ("not in list")

  populate(myMove, 'o')

  printField()


  moveCounter += 1

catsGame = True

while (moveCounter < 9):

    move = input ("Choose your move: ")

    userMoves.append(move)

    if (len(moves) >= 0):
        moves.remove(move)
    else:
        break

    populate(move, 'x')

    printField()


    moveCounter += 1

    if ((field[0][0] == 'x') and (field[0][1] == 'x') and (field[0][2] == 'x')):
        print("you win.")
        catsGame = False
        break
    elif ((field[1][0] == 'x') and (field[1][1] == 'x') and (field[1][2] == 'x')):
      print("you win.")
      catsGame = False
      break
    elif ((field[2][0] == 'x') and (field[2][1] == 'x') and (field[2][2] == 'x')):
      print("you win.")
      catsGame = False
      break
    elif ((field[0][0] == 'x') and (field[1][0] == 'x') and (field[2][0] == 'x')):
      print("you win.")
      catsGame = False
      break
    elif ((field[0][1] == 'x') and (field[1][1] == 'x') and (field[2][1] == 'x')):
      print("you win.")
      catsGame = False
      break
    elif ((field[0][2] == 'x') and (field[1][2] == 'x') and (field[2][2] == 'x')):
      print("you win.")
      catsGame = False
      break
    elif ((field[0][0] == 'x') and (field[1][1] == 'x') and (field[2][2] == 'x')):
      print("you win.")
      catsGame = False
      break
    elif ((field[0][2] == 'x') and (field[1][1] == 'x') and (field[2][0] == 'x')):
      print("you win.")
      catsGame = False
      break

    print ("My turn: ")

    if len(moves) > 0:
      myMove = think()
    #myMove = '2'

    if (myMove in moves):
        moves.remove(myMove)
    else:
        print ("not in list")
        break


    populate(myMove, 'o')

    printField()


    moveCounter += 1

    if ((field[0][0] == 'o') and (field[0][1] == 'o') and (field[0][2] == 'o')):
        print("I win.")
        catsGame = False
        break
    else:
        if ((field[1][0] == 'o') and (field[1][1] == 'o') and (field[1][2] == 'o')):
            print("I win.")
            catsGame = False
            break
        else:
            if ((field[2][0] == 'o') and (field[2][1] == 'o') and (field[2][2] == 'o')):
                print("I win.")
                catsGame = False
                break
            else:
                if ((field[0][0] == 'o') and (field[1][0] == 'o') and (field[2][0] == 'o')):
                    print("I win.")
                    catsGame = False
                    break
                else:
                    if ((field[0][1] == 'o') and (field[1][1] == 'o') and (field[2][1] == 'o')):
                        print("I win.")
                        catsGame = False
                        break
                    else:
                        if ((field[0][2] == 'o') and (field[1][2] == 'o') and (field[2][2] == 'o')):
                            print("I win.")
                            catsGame = False
                            break
                        else:
                            if ((field[0][0] == 'o') and (field[1][1] == 'o') and (field[2][2] == 'o')):
                                print("I win.")
                                catsGame = False
                                break
                            else:
                                if ((field[0][2] == 'o') and (field[1][1] == 'o') and (field[2][0] == 'o')):
                                    print("I win.")
                                    catsGame = False
                                    break
if catsGame:
  print ("cats game...")
else:
  print("...")
