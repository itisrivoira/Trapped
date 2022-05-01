import pygame, sys
import classi
pygame.init()

MUL = 1.50

##settaggi #####################################################
SCHERMO = pygame.display.set_mode((600,600))
pygame.display.set_caption("Trapped")
img_icon = pygame.image.load('./IMMAGINI/ICON/icon.png')
pygame.display.set_icon(img_icon)
FPS = 60

##carico immagini ##############################################
def carica_immagini():
  global img_classe
  global img_u_1, img_u_2, img_u_2, img_u_4, img_u_5, img_u_6, img_u_7, img_u_8, img_u_9, img_u_10, img_u_11, img_u_12
  global img_d_1, img_d_2, img_d_4, img_d_5, img_d_6, img_d_7, img_d_8, img_d_10, img_d_11, img_d_12
  
  img_classe = pygame.image.load('./IMMAGINI/MAPPA/classe.png').convert()
  img_classe = pygame.transform.scale(img_classe, ( img_classe.get_width()*MUL, img_classe.get_height()*MUL ))

  img_u_1 = pygame.image.load('./IMMAGINI/PERSONAGGI/UOMO/uomo_davanti_1.png')
  img_u_2 = pygame.image.load('./IMMAGINI/PERSONAGGI/UOMO/uomo_davanti_2.png')
  img_u_2 = pygame.image.load('./IMMAGINI/PERSONAGGI/UOMO/uomo_davanti_3.png')
  img_u_4 = pygame.image.load('./IMMAGINI/PERSONAGGI/UOMO/uomo_destra_1.png')
  img_u_5 = pygame.image.load('./IMMAGINI/PERSONAGGI/UOMO/uomo_destra_2.png')
  img_u_6 = pygame.image.load('./IMMAGINI/PERSONAGGI/UOMO/uomo_destra_3.png')
  img_u_7 = pygame.image.load('./IMMAGINI/PERSONAGGI/UOMO/uomo_dietro_1.png')
  img_u_8 = pygame.image.load('./IMMAGINI/PERSONAGGI/UOMO/uomo_dietro_2.png')
  img_u_9 = pygame.image.load('./IMMAGINI/PERSONAGGI/UOMO/uomo_dietro_3.png')
  img_u_10 = pygame.image.load('./IMMAGINI/PERSONAGGI/UOMO/uomo_sinistra_1.png')
  img_u_11 = pygame.image.load('./IMMAGINI/PERSONAGGI/UOMO/uomo_sinistra_2.png')
  img_u_12 = pygame.image.load('./IMMAGINI/PERSONAGGI/UOMO/uomo_sinistra_3.png')
  img_d_1 = pygame.image.load('./IMMAGINI/PERSONAGGI/DONNA/donna_davanti_1.png')
  img_d_2 = pygame.image.load('./IMMAGINI/PERSONAGGI/DONNA/donna_davanti_2.png')
  img_d_4 = pygame.image.load('./IMMAGINI/PERSONAGGI/DONNA/donna_destra_1.png')
  img_d_5 = pygame.image.load('./IMMAGINI/PERSONAGGI/DONNA/donna_destra_2.png')
  img_d_6 = pygame.image.load('./IMMAGINI/PERSONAGGI/DONNA/donna_destra_3.png')
  img_d_7 = pygame.image.load('./IMMAGINI/PERSONAGGI/DONNA/donna_dietro_1.png')
  img_d_8 = pygame.image.load('./IMMAGINI/PERSONAGGI/DONNA/donna_dietro_2.png')
  img_d_10 = pygame.image.load('./IMMAGINI/PERSONAGGI/DONNA/donna_sinistra_1.png')
  img_d_11 = pygame.image.load('./IMMAGINI/PERSONAGGI/DONNA/donna_sinistra_2.png')
  img_d_12 = pygame.image.load('./IMMAGINI/PERSONAGGI/DONNA/donna_sinistra_3.png')

##programma ####################################################
def inizializza():
  global stanza, per
  stanza = classi.Immagini(img_classe, 0, 0)
  per = classi.Personaggio(img_u_10, 550, 290)

def aggiorna():
	global clock
	clock = pygame.time.Clock()
	pygame.display.update()
	clock.tick(FPS)

def disegna_partita():
  SCHERMO.fill((0,0,0))
  SCHERMO.blit(stanza.getImmagine(), ( stanza.getCord_x(), stanza.getCord_y() ))
  SCHERMO.blit(per.getImmagine(), ( per.getCord_x(), per.getCord_y() ))


def clicca(pulsante, flag):
  if pulsante.key == pygame.K_a or pulsante.key == pygame.K_LEFT:
    per.setLeftPressed(flag)
    per.setIsWalking(flag)
  
  if pulsante.key == pygame.K_d or pulsante.key == pygame.K_RIGHT:
    per.setRightPressed(flag)
    per.setIsWalking(flag)

  if pulsante.key == pygame.K_w or pulsante.key == pygame.K_UP:
    per.setUpPressed(flag)
    per.setIsWalking(flag)

  if pulsante.key == pygame.K_s or pulsante.key == pygame.K_DOWN:
    per.setDownPressed(flag)
    per.setIsWalking(flag)

def main_partita():
  global clock
  running_partita = True

  carica_immagini()
  inizializza()

  while running_partita:
    disegna_partita()
    for event in pygame.event.get():
      if event.type == pygame.QUIT:
        pygame.quit()
        sys.exit()

      #con esc torna al main menu
        
      if event.type == pygame.KEYDOWN:
        clicca(event, True)

        if event.key == pygame.K_ESCAPE:
            running_partita = False

      if event.type == pygame.KEYUP:
        clicca(event, False)

    per.update()
    aggiorna()

if __name__ == "__main__":
	main_partita()