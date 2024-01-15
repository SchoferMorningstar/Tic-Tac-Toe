import pygame
from sys import exit


pygame.font.init() 
font = pygame.font.SysFont('Verdana', 30)
pygame.init()
screen = pygame.display.set_mode((600, 600))
clock = pygame.time.Clock()
state = "start"

'''START SCREEN'''
logo_text = font.render("Tic Tac Toe", False, "Black")
logo_rect = logo_text.get_rect(center = (300, 50))

button_text = font.render("START", False, "Black")
button_rect = button_text.get_rect(center = (300, 300))

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

def end(screen):
  screen.fill("#5374e0")

  if win(board):
    result = "Wygrywa O" if turn else "Wygrywa X"
  elif draw(board):
    result = "Remis"

  score_text = font.render(result, False, "Black")
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
      if e.type == pygame.MOUSEBUTTONUP and button_rect.collidepoint(e.pos):
        state = "game"
    if state == "game":
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
    if state == "end":
      if e.type == pygame.MOUSEBUTTONUP:
        if quit_rect.collidepoint(e.pos):
          pygame.quit()
          exit()
        elif playAgain_rect.collidepoint(e.pos):
          state = "new game"

  if state == "start":
    start(screen)
  elif state == "game":
    game(screen)
  elif state == "end":
    end(screen)
  elif state == "new game":
    board = [
    ["-", "-", "-"],
    ["-", "-", "-"],
    ["-", "-", "-"]]
    turn = True
    state = "game"
    

  pygame.display.update()
  clock.tick(15)
