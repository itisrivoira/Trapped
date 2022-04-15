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
img_classe = pygame.image.load('./IMMAGINI/MAPPA/classe.png').convert()
img_classe = pygame.transform.scale(img_classe, ( img_classe.get_width()*MUL, img_classe.get_height()*MUL ))

img_u_1 = pygame.image.load('./IMMAGINI/PERSONAGGI/UOMO/uomo_davanti_1.png')
img_u_2 = pygame.image.load('./IMMAGINI/PERSONAGGI/UOMO/uomo_davanti_2.png')
img_u_3 = pygame.image.load('./IMMAGINI/PERSONAGGI/UOMO/uomo_davanti_3.png')
img_u_4 = pygame.image.load('./IMMAGINI/PERSONAGGI/UOMO/uomo_destra_1.png')
img_u_5 = pygame.image.load('./IMMAGINI/PERSONAGGI/UOMO/uomo_destra_2.png')
img_u_6 = pygame.image.load('./IMMAGINI/PERSONAGGI/UOMO/uomo_destra_2.png')
img_u_7 = pygame.image.load('./IMMAGINI/PERSONAGGI/UOMO/uomo_dietro_1.png')
img_u_8 = pygame.image.load('./IMMAGINI/PERSONAGGI/UOMO/uomo_dietro_2.png')
img_u_9 = pygame.image.load('./IMMAGINI/PERSONAGGI/UOMO/uomo_dietro_3.png')
img_u_10 = pygame.image.load('./IMMAGINI/PERSONAGGI/UOMO/uomo_sinistra_1.png')
img_u_11 = pygame.image.load('./IMMAGINI/PERSONAGGI/UOMO/uomo_sinistra_2.png')
img_u_12 = pygame.image.load('./IMMAGINI/PERSONAGGI/UOMO/uomo_sinistra_3.png')

### programma ####################################################
stanza = classi.Immagini(img_classe, 0, 0)
per = classi.Personaggio(img_u_1, 50, 400, 0, 0)


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
        if event.key == pygame.K_LEFT:
          classi.Personaggio.left_pressed = True
        if event.key == pygame.K_RIGHT:
          classi.Personaggio.right_pressed = True
        if event.key == pygame.K_UP:
          classi.Personaggio.up_pressed = True
        if event.key == pygame.K_DOWN:
          classi.Personaggio.down_pressed = True
      if event.type == pygame.KEYUP:
        if event.key == pygame.K_LEFT:
          classi.Personaggio.left_pressed = False
        if event.key == pygame.K_RIGHT:
          classi.Personaggio.right_pressed = False
        if event.key == pygame.K_UP:
          classi.Personaggio.up_pressed = False
        if event.key == pygame.K_DOWN:
          classi.Personaggio.down_pressed = False
    per.aggiorna()
    #aggiorna()
    pygame.time.Clock().tick(120)

main_partita()

if __name__ == "__main__":
	main_partita()