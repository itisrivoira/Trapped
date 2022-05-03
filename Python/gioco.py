import pygame, sys
import classi
import partita
pygame.init()

### carico immagini ##############################################
img_sfondo = pygame.image.load('./IMMAGINI/INTRO/sfondo_page.png')
img_btn_tornaIndietro = pygame.image.load('./IMMAGINI/BUTTON//img_tornaIndietro.png')
img_icon = pygame.image.load('./IMMAGINI/ICON/icon.png')
img_scelta_s = pygame.image.load('./IMMAGINI/BUTTON/img_scelta_s.png')
img_scelta_d = pygame.image.load('./IMMAGINI/BUTTON/img_scelta_d.png')
img_uomo = pygame.image.load('./IMMAGINI/PERSONAGGI/UOMO/uomo_davanti_1.png')
img_donna = pygame.image.load('./IMMAGINI/PERSONAGGI/DONNA/donna_davanti_1.png')
img_inizia = pygame.image.load('./IMMAGINI/BUTTON/img_inizia.png')
img_inizia_on = pygame.image.load('./IMMAGINI/BUTTON/img_inizia_on.png')

### carico suoni ##############################################
pygame.mixer.music.load('./sound/sound.ogg')

### settaggi #####################################################
SCHERMO = pygame.display.set_mode((800,600))
pygame.display.set_caption("Trapped")
pygame.display.set_icon(img_icon)
FPS = 60

### programma ####################################################
img_sfondo = classi.Immagini(img_sfondo, 0, 0)
txt_sceG = classi.Testo("./font/Retro Gaming.ttf", 40, "Scegli personaggio", (255, 255, 255), 60, 50)
btn_scelta_s = classi.Button(img_scelta_s, 173, 300)
per = classi.Personaggio(img_uomo, 275, 300, SCHERMO)
btn_scelta_d = classi.Button(img_scelta_d, 382, 300)
btn_tornaIndietro2 = classi.Button(img_btn_tornaIndietro, 50, 500)
btn_inizia = classi.Button(img_inizia, 227.5, 450)

def aggiorna():
	pygame.display.update()
	pygame.time.Clock().tick(FPS)

def disegna_gioco():
  SCHERMO.fill((0,0,0))
  SCHERMO.blit(img_sfondo.getImmagine(), ( img_sfondo.getCord_x(), img_sfondo.getCord_y() ))
  SCHERMO.blit(txt_sceG.surf_text, ( txt_sceG.getCord_x(), txt_sceG.getCord_y() ))
  SCHERMO.blit(btn_scelta_s.getImmagine(), ( btn_scelta_s.getCord_x(), btn_scelta_s.getCord_y() ))
  SCHERMO.blit(per.getImmagine(), ( per.getCord_x(), per.getCord_y() ))
  SCHERMO.blit(btn_scelta_d.getImmagine(), ( btn_scelta_d.getCord_x(), btn_scelta_d.getCord_y() ))
  SCHERMO.blit(btn_tornaIndietro2.getImmagine(), ( btn_tornaIndietro2.getCord_x(), btn_tornaIndietro2.getCord_y() ))
  SCHERMO.blit(btn_inizia.getImmagine(), ( btn_inizia.getCord_x(), btn_inizia.getCord_y() ))


def main_gioco():
  running_gioco = True
  img_personaggio = "uomo"

  while running_gioco:

    disegna_gioco()

    for event in pygame.event.get():
      if event.type == pygame.QUIT:
        pygame.quit()
        sys.exit()
        
      #ottengo coordinate mouse
      cordMouse_x, cordMouse_y = pygame.mouse.get_pos()

      btn_inizia.on_button(cordMouse_x, cordMouse_y, img_inizia, img_inizia_on)

      #verifico se clicco un button
      if event.type == pygame.MOUSEBUTTONDOWN:

        stato_btnInd = btn_tornaIndietro2.pressed_button(cordMouse_x, cordMouse_y)
        if stato_btnInd == True:
          SCHERMO.fill((0,0,0))
          running_gioco = False
        
        stato_btn_scelta_s = btn_scelta_s.pressed_button(cordMouse_x, cordMouse_y)
        if stato_btn_scelta_s == True:
          if img_personaggio == "uomo":
            per.setImmagine(img_donna)
            img_personaggio = "donna"
          elif img_personaggio == "donna":
            per.setImmagine(img_uomo)
            img_personaggio = "uomo"

        stato_btn_scelta_d = btn_scelta_d.pressed_button(cordMouse_x, cordMouse_y)
        if stato_btn_scelta_d == True:
          if img_personaggio == "uomo":
            per.setImmagine(img_donna)
            img_personaggio = "donna"
          elif img_personaggio == "donna":
            per.setImmagine(img_uomo)
            img_personaggio = "uomo"
        
        stato_btnInizia = btn_inizia.pressed_button(cordMouse_x, cordMouse_y)
        if stato_btnInizia == True:
          SCHERMO.fill((0,0,0))
          running_gioco = False
          partita.main_partita()
    aggiorna()

if __name__ == "__main__":
	main_gioco()	