from asyncio import proactor_events
import pygame, sys
import classi, provaDomande, fine
import varGlobali as vg
pygame.init()

MUL = 1.50
global FPS

##settaggi #####################################################
SCHERMO = pygame.display.set_mode((600,600))
pygame.display.set_caption("Trapped")
img_icon = pygame.image.load('./IMMAGINI/ICON/icon.png')
pygame.display.set_icon(img_icon)
FPS = 60

img_cuore = pygame.image.load('./IMMAGINI/BUTTON/cuore.png')
img_cuore_u = pygame.image.load('./IMMAGINI/BUTTON/cuore_usato.png')

##carico immagini ##############################################
def carica_immagini(percorso):
  global img_classe
  img_classe = pygame.image.load('./IMMAGINI/MAPPA/'+percorso+'.png').convert()
  img_classe = pygame.transform.scale(img_classe, ( img_classe.get_width()*MUL, img_classe.get_height()*MUL ))

##programma ####################################################
txt_dialogo1 = classi.Testo("./font/Retro Gaming.ttf", 20, "Premi spazio", (0, 0, 0), 230, 530)
txt_dialogo2 = classi.Testo("./font/Retro Gaming.ttf", 20, "Premi g per interagire con il pc", (0, 0, 0), 230, 530)

c1 = classi.Immagini(img_cuore, 15, 15)
c2 = classi.Immagini(img_cuore, 55, 15)
c3 = classi.Immagini(img_cuore, 95, 15)

def allinea(ogg, allOri):
  if allOri == True:
    metaShermoW = SCHERMO.get_width()/2
    metaTestoW = ogg.surf_text.get_width()/2
    nuova_x = metaShermoW-metaTestoW
    ogg.setCord_x(nuova_x)

def inizializza():
  global stanza, per
  stanza = classi.Immagini(img_classe, 0, 0)
  if vg.character == 0:
    per = classi.Personaggio(vg.img_u_10, 550, 280)
  else:
    per = classi.Personaggio(vg.img_d_10, 550, 280)

def aggiorna():
	global clock
	clock = pygame.time.Clock()
	pygame.display.update()
	clock.tick(FPS)

def disegna_partita():
  SCHERMO.fill((0,0,0))
  SCHERMO.blit(stanza.getImmagine(), ( stanza.getCord_x(), stanza.getCord_y() ))
  SCHERMO.blit(per.getImmagine(), ( per.getCord_x(), per.getCord_y() ))

  if dialogo1 == True:
    pygame.draw.rect(SCHERMO, (255,255,255), (txt_dialogo1.getCord_x()-20, 490, (txt_dialogo1.lunT+40), 100),0, border_radius=10)
    pygame.draw.rect(SCHERMO, (0,0,0), (txt_dialogo1.getCord_x()-20, 490, (txt_dialogo1.lunT+40), 100),5, border_radius=10)
    allinea(txt_dialogo1, True)
    SCHERMO.blit(txt_dialogo1.surf_text, ( txt_dialogo1.getCord_x(), txt_dialogo1.getCord_y() ))
  
  if dialogo2 == True:
    pygame.draw.rect(SCHERMO, (255,255,255), (txt_dialogo2.getCord_x()-20, 490, (txt_dialogo2.lunT+40), 100),0, border_radius=10)
    pygame.draw.rect(SCHERMO, (0,0,0), (txt_dialogo2.getCord_x()-20, 490, (txt_dialogo2.lunT+40), 100),5, border_radius=10)
    allinea(txt_dialogo2, True)
    SCHERMO.blit(txt_dialogo2.surf_text, ( txt_dialogo2.getCord_x(), txt_dialogo2.getCord_y() ))
  
  pygame.draw.rect(SCHERMO, (255,255,255), (0, 0, 150, 70),0, border_bottom_right_radius=20)
  if vg.vite == 3:
    SCHERMO.blit(c1.getImmagine(), ( c1.getCord_x(), c1.getCord_y() ))
    SCHERMO.blit(c2.getImmagine(), ( c2.getCord_x(), c2.getCord_y() ))
    SCHERMO.blit(c3.getImmagine(), ( c3.getCord_x(), c3.getCord_y() ))
  elif vg.vite == 2:
    c3.setImmagine(img_cuore_u)
    SCHERMO.blit(c1.getImmagine(), ( c1.getCord_x(), c1.getCord_y() ))
    SCHERMO.blit(c2.getImmagine(), ( c2.getCord_x(), c2.getCord_y() ))
    SCHERMO.blit(c3.getImmagine(), ( c3.getCord_x(), c3.getCord_y() ))
  elif vg.vite == 1:
    c3.setImmagine(img_cuore_u)
    c2.setImmagine(img_cuore_u)
    SCHERMO.blit(c1.getImmagine(), ( c1.getCord_x(), c1.getCord_y() ))
    SCHERMO.blit(c2.getImmagine(), ( c2.getCord_x(), c2.getCord_y() ))
    SCHERMO.blit(c3.getImmagine(), ( c3.getCord_x(), c3.getCord_y() ))
  else:
    c3.setImmagine(img_cuore_u)
    c2.setImmagine(img_cuore_u)
    c1.setImmagine(img_cuore_u)
    SCHERMO.blit(c1.getImmagine(), ( c1.getCord_x(), c1.getCord_y() ))
    SCHERMO.blit(c2.getImmagine(), ( c2.getCord_x(), c2.getCord_y() ))
    SCHERMO.blit(c3.getImmagine(), ( c3.getCord_x(), c3.getCord_y() ))
  pygame.draw.rect(SCHERMO, (0,0,0), (-5, -5, 155, 75),5, border_bottom_right_radius=20)


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

def muovi_alto():
  per.setUpPressed(False)
  print("alto")

def muovi_basso():
  per.setDownPressed(False)
  print("basso")

def muovi_destra():
  per.setRightPressed(False)
  print("destra")

def muovi_sinistra():
  per.setLeftPressed(False)
  print("sinistra")

def level0():
  global d0, d1, d2, d3, d4, d5, d6, dialogo1, dialogo2

  if vg.flag_lvl0:
    dialogo1 = False
    d0 = classi.Delay(1.5, muovi_sinistra)
    d1 = classi.Delay(0.8, muovi_alto)
    d2 = classi.Delay(1.1, muovi_destra)
    d3 = classi.Delay(0.2, muovi_alto)

    d4 = classi.Delay(0.25, muovi_destra)
    d5 = classi.Delay(1, muovi_basso)
    d6 = classi.Delay(0.2, muovi_destra)

    vg.flag_lvl0 = False

  per.setIsWalking(True)

  if not d0.iFinished:
    per.setLeftPressed(True)
    d0.Start()

  if d0.iFinished and not d1.iFinished:
    per.setUpPressed(True)
    d1.Start()

  if d0.iFinished and d1.iFinished and not d2.iFinished:
    per.setRightPressed(True)
    d2.Start()

  if d0.iFinished and d1.iFinished and d2.iFinished and not d3.iFinished:
    per.setUpPressed(True)
    d3.Start()
    dialogo2 = True

  #da qui torna indietro
  a = d0.iFinished and d1.iFinished and d2.iFinished and d3.iFinished and vg.flag_corretta

  if a and not d4.iFinished:
    per.setRightPressed(True)
    d4.Start()

  if a and d4.iFinished and not d5.iFinished:
    per.setDownPressed(True)
    d5.Start()

  if a and d4.iFinished and d5.iFinished and not d6.iFinished:
    per.setRightPressed(True)
    d6.Start()
    vg.flag_muoviti = False
    vg.lvl0= False
    vg.flag_fine = True

def ActualLevel():
  if vg.lvl0:
    level0()

def main_partita():
  global clock, flag_x, flag_y, dialogo1, dialogo2

  running_partita = True
  flag_x, flag_y = False, False
  dialogo1 = True
  dialogo2 = False

  carica_immagini("classe")
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
            vg.flag_muoviti = True
        
        if event.key == pygame.K_g:
            provaDomande.main_domande()
            dialogo2 = False

    if vg.flag_muoviti:
      ActualLevel()

    if vg.flag_fine == True:
      running_partita = False
      fine.main_fine()

    per.update()
    aggiorna()

if __name__ == "__main__":
	main_partita()