import pygame, sys
import classi, main
import varGlobali as vg
pygame.init()

### carico immagini ##############################################
img_sfondo = pygame.image.load('./IMMAGINI/INTRO/sfondo_page.png')
img_btn_tornaIndietro = pygame.image.load('./IMMAGINI/BUTTON//img_tornaIndietro.png')
img_icon = pygame.image.load('./IMMAGINI/ICON/icon.png')

### settaggi #####################################################
SCHERMO = pygame.display.set_mode((800,600))
FPS = 60

### programma ####################################################
img_sfondo = classi.Immagini(img_sfondo, 0, 0)
txt_gameO = classi.Testo("./font/04B_30__.TTF", 70, "Game Over", (255, 255, 255), 170, 200)
btn_ind = classi.Button(img_btn_tornaIndietro, 50, 500)

def aggiorna():
	pygame.display.update()
	pygame.time.Clock().tick(FPS)

def allinea(ogg, allOri):
  if allOri == True:
    metaShermoW = SCHERMO.get_width()/2
    metaTestoW = ogg.surf_text.get_width()/2
    nuova_x = metaShermoW-metaTestoW
    ogg.setCord_x(nuova_x)

def disegna_gameOver():
  SCHERMO.blit(img_sfondo.getImmagine(), ( img_sfondo.getCord_x(), img_sfondo.getCord_y() ))
  allinea(txt_gameO, True)
  SCHERMO.blit(txt_gameO.surf_text, ( txt_gameO.getCord_x(), txt_gameO.getCord_y() ))
  SCHERMO.blit(btn_ind.getImmagine(), ( btn_ind.getCord_x(), btn_ind.getCord_y() ))

def main_gameOver():
  SCHERMO.fill((0,0,0))
  running_gameOver = True

  while running_gameOver:

    disegna_gameOver()

    for event in pygame.event.get():
      if event.type == pygame.QUIT:
        pygame.quit()
        sys.exit()
        
      #ottengo coordinate mouse
      cordMouse_x, cordMouse_y = pygame.mouse.get_pos()

      #verifico se clicco un button
      if event.type == pygame.MOUSEBUTTONDOWN:

        stato_btnInd = btn_ind.pressed_button(cordMouse_x, cordMouse_y)
        if stato_btnInd == True:
          vg.character = 0
          vg.flag_fine = False
          vg.flag_corretta = False
          vg.flag_muoviti = False
          vg.vite = 3

          SCHERMO.fill((0,0,0))
          running_fine = False
          main.main_home()
    aggiorna()

if __name__ == "__main__":
	main_gameOver()	