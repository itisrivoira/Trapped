import pygame, sys
import classi
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
txt_cla = classi.Testo("./font/Retro Gaming.ttf", 40, "Classifica", (255, 255, 255), 170, 50)
btn_tornaIndietro3 = classi.Button(img_btn_tornaIndietro, 50, 500)

def aggiorna():
	pygame.display.update()
	pygame.time.Clock().tick(FPS)

def allinea(ogg, cont, allOri, var):
  if allOri == True:
    metaShermoW = cont.w/2
    metaTestoW = ogg.surf_text.get_width()/2
    nuova_x = var+metaShermoW-metaTestoW
    ogg.setCord_x(nuova_x)

def disegna_cla():
  SCHERMO.blit(img_sfondo.getImmagine(), ( img_sfondo.getCord_x(), img_sfondo.getCord_y() ))
  SCHERMO.blit(txt_cla.surf_text, ( txt_cla.getCord_x(), txt_cla.getCord_y() ))
  SCHERMO.blit(txt_cla.surf_text, ( txt_cla.getCord_x(), txt_cla.getCord_y() ))
  SCHERMO.blit(btn_tornaIndietro3.getImmagine(), ( btn_tornaIndietro3.getCord_x(), btn_tornaIndietro3.getCord_y() ))

  with open('score.txt', 'r') as f:
    f_contest = f.readlines()
    r_contatore = f_contest[0]
  f.close()

  partite = classi.Testo("./font/Retro Gaming.ttf", 20, "Partite", (255, 255, 255), 250, 170)
  punti = classi.Testo("./font/Retro Gaming.ttf", 20, "Punti", (255, 255, 255), 250, 170)

  h = 200
  for i in range(len(f_contest)):
    if i > 0:
      my_str = f_contest[i]
      final_str = my_str[:-1]

      parola = final_str.split()

      ogg1 = "s_txt_par"+str(i)
      ogg1 = classi.Testo("./font/Retro Gaming.ttf", 20, parola[0], (0, 0, 0), 250, h)

      ogg2 = "d_txt_par"+str(i)
      ogg2 = classi.Testo("./font/Retro Gaming.ttf", 20, parola[1], (0, 0, 0), 350, h)

      cont1 = "s_c"+str(i)
      cont1 = classi.Rettangolo(200, h, 100, ogg1.altT, (0, 0, 0), (255, 255, 255))

      cont2 = "d_c"+str(i)
      cont2 = classi.Rettangolo(300, h, 100, ogg2.altT, (0, 0, 0), (255, 255, 255))

      pygame.draw.rect(SCHERMO, cont1.colB, (cont1.x, cont1.y, 100, cont1.h), 0)
      pygame.draw.rect(SCHERMO, cont2.colB, (cont2.x, cont2.y, 100, cont2.h), 0)

      allinea(partite, cont1, True, 200)
      SCHERMO.blit(partite.surf_text, ( partite.getCord_x(), partite.getCord_y() ))

      allinea(punti, cont2, True, 300)
      SCHERMO.blit(punti.surf_text, ( punti.getCord_x(), punti.getCord_y() ))

      allinea(ogg1, cont1, True, 200)
      SCHERMO.blit(ogg1.surf_text, ( ogg1.getCord_x(), ogg1.getCord_y() ))

      allinea(ogg2, cont2, True, 300)
      SCHERMO.blit(ogg2.surf_text, ( ogg2.getCord_x(), ogg2.getCord_y() ))
      h += 30

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