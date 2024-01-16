import pygame
from sys import exit
from random import seed
from random import randint


pygame.font.init() 
font = pygame.font.SysFont('Verdana', 30)
pygame.init()
screen = pygame.display.set_mode((600, 600))
clock = pygame.time.Clock()
state = "start"

'''START SCREEN'''
logo_text = font.render("Tic Tac Toe", False, "Black")
logo_rect = logo_text.get_rect(center = (300, 50))

button_text = font.render("PvP", False, "Black")
button_rect = button_text.get_rect(center = (300, 300))

button2_text = font.render("PvAI", False, "Black")
button2_rect = button2_text.get_rect(center = (300, 450))

'''GAME SCREEN'''
board = [
  ["-", "-", "-"],
  ["-", "-", "-"],
  ["-", "-", "-"]
]
turn = True #True - O turn, False - X turn

def win(board):
  if (board[0][0] == board[0][1] == board[0][2] != "-") or (board[1][0] == board[1][1] == board[1][2] != "-") or (board[2][0] == board[2][1] == board[2][2] != "-") or (board[0][0] == board[1][0] == board[2][0] != "-") or (board[0][1] == board[1][1] == board[2][1] != "-") or (board[0][2] == board[1][2] == board[2][2] != "-") or (board[0][0] == board[1][1] == board[2][2] != "-") or (board[0][2] == board[1][1] == board[2][0] != "-"):
    return True
  else:
    return False
  
def draw(board):
  free_sqs = 0
  for i in range(3):
    for j in range(3):
      if board[i][j] == "-": free_sqs += 1
  
  if not win(board) and free_sqs == 0:
    return True
  else:
    return False
  

'''GAME SCREEN AI'''

choose_O = font.render("Graj jako O", False, "Black")
O_rect = choose_O.get_rect(center = (300, 200))

choose_X = font.render("Graj jako X", False, "Black")
X_rect = choose_X.get_rect(center = (300, 400))

you = ""
ai = ""
ai_turn = None

def getPossibleMoves(board):
  moves = []
  for i in range(3):
    for j in range(3):
      if board[i][j] == "-":
        moves.append((i, j))
  return moves 

def getComputerMove():
  corners = [(0, 0), (0, 2), (2, 0), (2, 2)]
  possible_moves = getPossibleMoves(board)
  c_free = 0
  for m in possible_moves:
    board[m[0]][m[1]] = ai
    if win(board):
      return m
    elif draw(board):
      return m
    board[m[0]][m[1]] = you
    if win(board):
      return m
    board[m[0]][m[1]] =  "-"

  for c in corners:
    if board[c[0]][c[1]] == you:
      if (1, 1) in possible_moves:
        return (1, 1)
    elif board[c[0]][c[1]] == "-":
      c_free += 1
    elif board[c[0]][c[1]] == ai:
      if c == (0, 0) and board[0][2] == "-":
        return (0, 2)
      elif c == (0, 2)  and board[0][0] == "-":
        return (0, 0)
      elif c == (2, 0) and board[2][2] == "-":
        return (2, 2)
      elif c == (2, 2)  and board[2][0] == "-":
        return (2, 0)
    elif c_free == 4:
      return (0, 0)
  seed(1)
  return possible_moves[randint(0, len(possible_moves))]
'''END SCREEN'''

playAgain_text = font.render("OD NOWA", False, "Black")
playAgain_rect = playAgain_text.get_rect(center = (300, 300))

quit_text = font.render("WYJDŹ", False, "Black")
quit_rect = quit_text.get_rect(center = (300, 450))



def start(screen):
  screen.fill("#5374e0")

  screen.blit(logo_text, logo_rect)
  pygame.draw.rect(screen, "#46e37d", button_rect)
  screen.blit(button_text, button_rect)
  pygame.draw.rect(screen, "#46e37d", button2_rect)
  screen.blit(button2_text, button2_rect)

def game(screen):
  screen.fill("#5374e0")

  for i in range(3):
    for j in range(3):
      if board[i][j] == "O":
        pygame.draw.rect(screen, "Black", pygame.Rect(i * 200, j * 200, 200, 200), 10, 100)
      elif board[i][j] == "X":
        pygame.draw.line(screen, "Black", (i*200, j*200), ((i+1)*200, (j+1)* 200), 10)
        pygame.draw.line(screen, "Black", ((i+1)*200, j*200), (i*200, (j+1) * 200), 10)
  pygame.draw.line(screen, "Black", (200, 0), (200, 600))
  pygame.draw.line(screen, "Black", (400, 0), (400, 600))
  pygame.draw.line(screen, "Black", (0, 200), (600, 200))
  pygame.draw.line(screen, "Black", (0, 400), (600, 400))

def game_ai_choose(screen):
  screen.fill("#5374e0")

  pygame.draw.rect(screen, "#46e37d", O_rect)
  screen.blit(choose_O, O_rect)

  pygame.draw.rect(screen, "#46e37d", X_rect)
  screen.blit(choose_X, X_rect)


def end(screen):
  screen.fill("#5374e0")
  game(screen)

  if ai_turn != None:
    if win(board):
      result = "Przegrałeś" if ai_turn else "Wygrałeś"
    elif draw(board):
      result = "Remis"
  else:   
    if win(board):
      result = "Wygrywa O" if turn else "Wygrywa X"
    elif draw(board):
      result = "Remis"

  score_text = font.render(result, False, "White")
  score_rect = score_text.get_rect(center = (300, 50))
  screen.blit(score_text, score_rect)
  pygame.draw.rect(screen, "#46e37d", playAgain_rect)
  screen.blit(playAgain_text, playAgain_rect)
  pygame.draw.rect(screen, "Red", quit_rect)
  screen.blit(quit_text, quit_rect)

while True:
  for e in pygame.event.get():
    if e.type == pygame.QUIT:
      pygame.quit()
      exit()
    if state == "start":
      if e.type == pygame.MOUSEBUTTONUP:
        if button_rect.collidepoint(e.pos):
          state = "game_pvp"
        elif button2_rect.collidepoint(e.pos):
          state = "game_ai_choose"
    if state == "game_pvp":
      if e.type == pygame.MOUSEBUTTONDOWN:
        pos = e.pos
        r = pos[0] // 200
        c = pos[1] // 200
        if board[r][c] == "-":
          board[r][c] = "O" if turn else "X"
          if win(board) or draw(board):
            game(screen)
            state = "end"
          else:
            turn = not turn
    if state == "game_ai_choose":
      if e.type == pygame.MOUSEBUTTONUP:
        if X_rect.collidepoint(e.pos):
          you = "X"
          ai = "O"
          ai_turn = True
          state = "game_ai"
        elif O_rect.collidepoint(e.pos):
          you = "O"
          ai = "X"
          ai_turn = False
          state = "game_ai"
    if state == "game_ai":
      if not ai_turn:
        if e.type == pygame.MOUSEBUTTONDOWN:
          pos = e.pos
          r = pos[0] // 200
          c = pos[1] // 200
          if board[r][c] == "-":
            board[r][c] = you
          if win(board) or draw(board):
            game(screen)
            state = "end"
          else:
            ai_turn = not ai_turn
      else:
        move = getComputerMove()
        board[move[0]][move[1]] = ai
        print(board)
        if win(board) or draw(board):
            game(screen)
            state = "end"
        else:
          ai_turn = not ai_turn
      
      
    if state == "end":
      if e.type == pygame.MOUSEBUTTONUP:
        if quit_rect.collidepoint(e.pos):
          pygame.quit()
          exit()
        elif playAgain_rect.collidepoint(e.pos):
          state = "new game"

  if state == "start":
    start(screen)
  elif state == "game_pvp":
    game(screen)
  elif state == "game_ai_choose":
    game_ai_choose(screen)
  elif state == "game_ai":
    game(screen)
  elif state == "end":
    end(screen)
  elif state == "new game":
    board = [
    ["-", "-", "-"],
    ["-", "-", "-"],
    ["-", "-", "-"]]
    turn = True
    ai_turn = None
    state = "start"
    

  pygame.display.update()
  clock.tick(15)
