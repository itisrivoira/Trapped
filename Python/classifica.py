import pygame, sys
import classi
pygame.init()

### carico immagini ##############################################
img_btn_tornaIndietro = pygame.image.load('./IMMAGINI/BUTTON//img_tornaIndietro.png')
img_icon = pygame.image.load('./IMMAGINI/ICON/icon.png')

### settaggi #####################################################
SCHERMO = pygame.display.set_mode((800,600))
FPS = 60

### programma ####################################################
txt_cla = classi.Testo("./font/Retro Gaming.ttf", 70, "Classifica", (255, 255, 255), 0, 50)
btn_tornaIndietro3 = classi.Button(img_btn_tornaIndietro, 50, 500)

def aggiorna():
	pygame.display.update()
	pygame.time.Clock().tick(FPS)

def disegna_cla():
  SCHERMO.blit(txt_cla.surf_text, ( txt_cla.getCord_x(), txt_cla.getCord_y() ))
  SCHERMO.blit(btn_tornaIndietro3.getImmagine(), ( btn_tornaIndietro3.getCord_x(), btn_tornaIndietro3.getCord_y() ))

def main_classifica():
  SCHERMO.fill((0,0,0))
  running_classifica = True

  while running_classifica:

    disegna_cla()

    for event in pygame.event.get():
      if event.type == pygame.QUIT:
        pygame.quit()
        sys.exit()
        
      #ottengo coordinate mouse
      cordMouse_x, cordMouse_y = pygame.mouse.get_pos()

      #verifico se clicco un button
      if event.type == pygame.MOUSEBUTTONDOWN:

        stato_btnInd = btn_tornaIndietro3.pressed_button(cordMouse_x, cordMouse_y)
        if stato_btnInd == True:
          SCHERMO.fill((0,0,0))
          running_classifica = False
    aggiorna()

if __name__ == "__main__":
	main_classifica()	