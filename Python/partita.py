import pygame, sys
import classi
import varGlobali as vg
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
  img_classe = pygame.image.load('./IMMAGINI/MAPPA/classe.png').convert()
  img_classe = pygame.transform.scale(img_classe, ( img_classe.get_width()*MUL, img_classe.get_height()*MUL ))

##programma ####################################################
def inizializza():
  global stanza, per
  stanza = classi.Immagini(img_classe, 0, 0)
  if vg.character == 0:
    per = classi.Personaggio(vg.img_u_10, 550, 280)
  else:
    per = classi.Personaggio(vg.img_d_10, 550, 280)

  txt_dialog1 = classi.Testo("./font/Retro Gaming.ttf", 20, "Premi spazio", (255, 255, 255), 140, 50)

def aggiorna():
	global clock
	clock = pygame.time.Clock()
	pygame.display.update()
	clock.tick(FPS)

def disegna_partita():
  SCHERMO.fill((0,0,0))
  SCHERMO.blit(stanza.getImmagine(), ( stanza.getCord_x(), stanza.getCord_y() ))
  SCHERMO.blit(per.getImmagine(), ( per.getCord_x(), per.getCord_y() ))
  pygame.draw.rect(SCHERMO, (255,255,255), (150,490,300,100),0)
  #SCHERMO.blit(txt_dialog1.surf_text, ( txt_dialog1.getCord_x(), txt_dialog1.getCord_y() ))

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

def muoviti(flag):
  global flag_x, flag_y
  per.setIsWalking(False)

  if flag == True:
    per.setIsWalking(True)

    #da porta al centro stanza
    if per.getCord_x() >= 280 and not flag_x:
      per.setLeftPressed(True)
    else:
      per.setLeftPressed(False)

      #da centro stanza alla cattedra
      if per.getCord_y() >= 130 and not flag_y:
        per.setUpPressed(True)
      else:
        per.setUpPressed(False)
        flag_x = True

        #da cattedra va verso destra
        if per.getCord_x() <= 470:
          per.setRightPressed(True)
        else:
          per.setRightPressed(False)
          flag_y = True

          #da destra va verso il pc in alto
          if per.getCord_y() >= 110:
            per.setUpPressed(True)
          else:
            per.setUpPressed(False)
            flag_x = True
            per.setImmagine(pygame.image.load(per.animazione_up[0]))
            return True
  else:
    return False

def muoviti2(flag):
  global flag_x, flag_y
  per.setIsWalking(False)

  if flag == True:
    per.setIsWalking(True)

    #da pc va verso il basso
    if per.getCord_y() <= 130:
      per.setDownPressed(True)
    else:
      per.setDownPressed(False)

      #da pc va verso sinistra
      if per.getCord_x() >= 170:
        per.setLeftPressed(True)
      else:
        per.setLeftPressed(False)
        flag_y = True

        #verso armadio
        if per.getCord_y() <= 10:
          per.setUpPressed(True)
        else:
          per.setUpPressed(False)
          per.setImmagine(pygame.image.load(per.animazione_up[0]))

def main_partita():
  global clock, flag_x, flag_y
  running_partita = True
  flag_muoviti = False
  flag_x, flag_y = False, False
  flag_muoviti2 = False

  carica_immagini()
  inizializza()

  while running_partita:
    disegna_partita()
    for event in pygame.event.get():
      if event.type == pygame.QUIT:
        pygame.quit()
        sys.exit()

      if event.type == pygame.KEYDOWN:
          
        if event.key == pygame.K_ESCAPE:
            running_partita = False
        
        if event.key == pygame.K_SPACE:
            flag_muoviti = True

    if muoviti(flag_muoviti):
      flag_muoviti = False
      flag_muoviti2 = True #modifico poi quando a finito enigma
    
    if flag_muoviti2 == True:
      #muoviti2(flag_muoviti2)
      pass
    per.update()
    aggiorna()

if __name__ == "__main__":
	main_partita()