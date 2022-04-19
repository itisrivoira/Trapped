import pygame, sys
import classi
#from gioco import per
pygame.init()

MUL = 1.50

### settaggi #####################################################
SCHERMO = pygame.display.set_mode((600,600))
pygame.display.set_caption("Trapped")
img_icon = pygame.image.load('./IMMAGINI/ICON/icon.png')
pygame.display.set_icon(img_icon)
FPS = 60
vel = 10

### carico immagini ##############################################
img_classe = pygame.image.load('./IMMAGINI/MAPPA/classe.png').convert()
img_classe = pygame.transform.scale(img_classe, ( img_classe.get_width()*MUL, img_classe.get_height()*MUL ))

img_u_1 = pygame.image.load('./IMMAGINI/PERSONAGGI/UOMO/uomo_davanti_1.png')
img_u_2 = pygame.image.load('./IMMAGINI/PERSONAGGI/UOMO/uomo_davanti_2.png')
img_u_3 = pygame.image.load('./IMMAGINI/PERSONAGGI/UOMO/uomo_davanti_3.png')
img_u_4 = pygame.image.load('./IMMAGINI/PERSONAGGI/UOMO/uomo_destra_1.png')
img_u_5 = pygame.image.load('./IMMAGINI/PERSONAGGI/UOMO/uomo_destra_2.png')
img_u_6 = pygame.image.load('./IMMAGINI/PERSONAGGI/UOMO/uomo_destra_3.png')
img_u_7 = pygame.image.load('./IMMAGINI/PERSONAGGI/UOMO/uomo_dietro_1.png')
img_u_8 = pygame.image.load('./IMMAGINI/PERSONAGGI/UOMO/uomo_dietro_2.png')
img_u_9 = pygame.image.load('./IMMAGINI/PERSONAGGI/UOMO/uomo_dietro_3.png')
img_u_10 = pygame.image.load('./IMMAGINI/PERSONAGGI/UOMO/uomo_sinistra_1.png')
img_u_11 = pygame.image.load('./IMMAGINI/PERSONAGGI/UOMO/uomo_sinistra_2.png')
img_u_12 = pygame.image.load('./IMMAGINI/PERSONAGGI/UOMO/uomo_sinistra_3.png')

### programma ####################################################
stanza = classi.Immagini(img_classe, 0, 0)
per = classi.Personaggio(img_u_10, 550, 290)

def aggiorna():
	pygame.display.update()
	pygame.time.Clock().tick(FPS)

def disegna_partita():
  SCHERMO.blit(stanza.getImmagine(), ( stanza.getCord_x(), stanza.getCord_y() ))
  SCHERMO.blit(per.getImmagine(), ( per.getCord_x(), per.getCord_y() ))

def main_partita():
  SCHERMO.fill((0,0,0))
  running_partita = True

  while running_partita:
    disegna_partita()
    for event in pygame.event.get():
      if event.type == pygame.QUIT:
        pygame.quit()
        sys.exit()

      #con esc torna al main menu
      if event.type == pygame.KEYDOWN:
        if event.key == pygame.K_ESCAPE:
          running_partita = False

        if event.key == pygame.K_a:
          statoCol1 = per.collidStanza(SCHERMO.get_width(), SCHERMO.get_height())
          if statoCol1 == True:
            SCHERMO.fill((0,0,0))
            per.setImmagine(img_u_10)
            per.setCord_x( per.getCord_x()-vel )

        if event.key == pygame.K_d:
          statoCol2 = per.collidStanza(SCHERMO.get_width(), SCHERMO.get_height())
          if statoCol2 == True:
            SCHERMO.fill((0,0,0))
            per.setImmagine(img_u_4)
            per.setCord_x( per.getCord_x()+vel )
        
        if event.key == pygame.K_w:
          statoCol3 = per.collidStanza(SCHERMO.get_width(), SCHERMO.get_height())
          if statoCol3 == True:
            SCHERMO.fill((0,0,0))
            per.setImmagine(img_u_7)
            per.setCord_y( per.getCord_y()-vel )
        
        if event.key == pygame.K_s:
          statoCol4 = per.collidStanza(SCHERMO.get_width(), SCHERMO.get_height())
          if statoCol4 == True:
            SCHERMO.fill((0,0,0))
            per.setImmagine(img_u_1)
            per.setCord_y( per.getCord_y()+vel )
    aggiorna()

if __name__ == "__main__":
	main_partita()
