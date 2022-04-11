import pygame, sys
import classi
pygame.init()

MUL = 1.50

### settaggi #####################################################
SCHERMO = pygame.display.set_mode((600,600))
pygame.display.set_caption("Trapped")
img_icon = pygame.image.load('./IMMAGINI/ICON/icon.png')
pygame.display.set_icon(img_icon)
FPS = 60

### carico immagini ##############################################
img_classe = pygame.image.load('./IMMAGINI/STANZE/classe.png').convert()
img_classe = pygame.transform.scale(img_classe, ( img_classe.get_width()*MUL, img_classe.get_height()*MUL ))

img_u_1 = pygame.image.load('./IMMAGINI/PERSONAGGI/uomo/uomo_davanti_1.png')
img_u_2 = pygame.image.load('./IMMAGINI/PERSONAGGI/uomo/uomo_davanti_2.png')
img_u_3 = pygame.image.load('./IMMAGINI/PERSONAGGI/uomo/uomo_davanti_3.png')
img_u_4 = pygame.image.load('./IMMAGINI/PERSONAGGI/uomo/uomo_destra_1.png')
img_u_5 = pygame.image.load('./IMMAGINI/PERSONAGGI/uomo/uomo_destra_2.png')
img_u_6 = pygame.image.load('./IMMAGINI/PERSONAGGI/uomo/uomo_destra_2.png')
img_u_7 = pygame.image.load('./IMMAGINI/PERSONAGGI/uomo/uomo_dietro_1.png')
img_u_8 = pygame.image.load('./IMMAGINI/PERSONAGGI/uomo/uomo_dietro_2.png')
img_u_9 = pygame.image.load('./IMMAGINI/PERSONAGGI/uomo/uomo_dietro_3.png')
img_u_10 = pygame.image.load('./IMMAGINI/PERSONAGGI/uomo/uomo_sinistra_1.png')
img_u_11 = pygame.image.load('./IMMAGINI/PERSONAGGI/uomo/uomo_sinistra_2.png')
img_u_12 = pygame.image.load('./IMMAGINI/PERSONAGGI/uomo/uomo_sinistra_3.png')

### programma ####################################################
stanza = classi.Immagini(img_classe, 0, 0)
per = classi.Personaggio(img_u_1, 50, 400)


def inizializza():
	global persx, persy
	persx, persy = 50,50

def aggiorna():
	pygame.display.update()
	pygame.time.Clock().tick(FPS)

def disegna_partita():
  SCHERMO.blit(stanza.getImmagine(), (stanza.getCord_x(), stanza.getCord_y() ))
  SCHERMO.blit(per.getImmagine(), (persx, persy))

def main_partita():
  SCHERMO.fill((0,0,0))
  inizializza()
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
          pygame.quit()
          sys.exit()
        if event.key == pygame.K_UP:	#KEYDOWN -> tasto premuto, key == pygame.K_UP -> freccia su
          global persy 
          persy = persy-10 #sale
        if event.key == pygame.K_DOWN:
          persy = persy+10 #scende
        if event.key == pygame.K_LEFT:
          global persx
          persx = persx-10 #sinistra
        if event.key == pygame.K_RIGHT:
          persx = persx+10 #destra
      #ottengo coordinate mouse
      #cordMouse_x, cordMouse_y = pygame.mouse.get_pos()
    aggiorna()

main_partita()

if __name__ == "__main__":
	main_partita()