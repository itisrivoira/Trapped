import pygame, sys
import classi
pygame.init()

### carico immagini ##############################################
img_btn_tornaIndietro = pygame.image.load('./IMMAGINI/BUTTON/img_tornaIndietro.png')
img_icon = pygame.image.load('./IMMAGINI/ICON/icon.png')

### carico suoni ##############################################
pygame.mixer.music.load('./sound/sound.ogg')

### settaggi #####################################################
SCHERMO = pygame.display.set_mode((600,600))
pygame.display.set_caption("Trapped")
pygame.display.set_icon(img_icon)
FPS = 60

### programma ####################################################
txt_sceG = classi.Testo("./font/Retro Gaming.ttf", 60, "Scegli personaggio", (255, 255, 255), 0, 50)
btn_tornaIndietro2 = classi.Button(img_btn_tornaIndietro, 50, 500)

def aggiorna():
	pygame.display.update()
	pygame.time.Clock().tick(FPS)

def disegna_gioco():
  SCHERMO.blit(txt_sceG.surf_text, ( txt_sceG.getCord_x(), txt_sceG.getCord_y() ))
  SCHERMO.blit(btn_tornaIndietro2.getImmagine(), ( btn_tornaIndietro2.getCord_x(), btn_tornaIndietro2.getCord_y() ))

def main_gioco():
  SCHERMO.fill((0,0,0))
  running_gioco = True

  while running_gioco:

    disegna_gioco()

    for event in pygame.event.get():
      if event.type == pygame.QUIT:
        pygame.quit()
        sys.exit()
        
      #ottengo coordinate mouse
      cordMouse_x, cordMouse_y = pygame.mouse.get_pos()

      #verifico se clicco un button
      if event.type == pygame.MOUSEBUTTONDOWN:

        stato_btnInd = btn_tornaIndietro2.pressed_button(cordMouse_x, cordMouse_y)
        if stato_btnInd == True:
          SCHERMO.fill((0,0,0))
          running_gioco = False
    aggiorna()

if __name__ == "__main__":
	main_gioco()	