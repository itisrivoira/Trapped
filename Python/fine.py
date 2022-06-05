import pygame, sys
import classi
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
txt_cla = classi.Testo("./font/04B_30__.TTF", 80, "The End", (255, 255, 255), 170, 200)
btn_tornaIndietro3 = classi.Button(img_btn_tornaIndietro, 50, 500)

def aggiorna():
	pygame.display.update()
	pygame.time.Clock().tick(FPS)

def allinea(ogg, allOri):
  if allOri == True:
    metaShermoW = SCHERMO.get_width()/2
    metaTestoW = ogg.surf_text.get_width()/2
    nuova_x = metaShermoW-metaTestoW
    ogg.setCord_x(nuova_x)

def disegna_fine():
  vg.punti = 100
  if vg.vite == 3:
    vg.punti = 100
  elif vg.vite == 2:
    vg.punti -= 20
  elif vg.vite == 1:
    vg.punti -= 40
  else:
    vg.punti -= 60

  txt_punti1 = classi.Testo("./font/Retro Gaming.ttf", 30, "Hai totalizzato ", (255, 255, 255), 170, 300)
  txt_punti2 = classi.Testo("./font/Retro Gaming.ttf", 30, str(vg.punti)+" punti", (255, 255, 255), 170, 350)

  SCHERMO.blit(img_sfondo.getImmagine(), ( img_sfondo.getCord_x(), img_sfondo.getCord_y() ))
  allinea(txt_cla, True)
  SCHERMO.blit(txt_cla.surf_text, ( txt_cla.getCord_x(), txt_cla.getCord_y() ))
  allinea(txt_punti1, True)
  SCHERMO.blit(txt_punti1.surf_text, ( txt_punti1.getCord_x(), txt_punti1.getCord_y() ))
  allinea(txt_punti2, True)
  SCHERMO.blit(txt_punti2.surf_text, ( txt_punti2.getCord_x(), txt_punti2.getCord_y() ))
  SCHERMO.blit(btn_tornaIndietro3.getImmagine(), ( btn_tornaIndietro3.getCord_x(), btn_tornaIndietro3.getCord_y() ))

def main_fine():
  SCHERMO.fill((0,0,0))
  running_fine = True

  while running_fine:

    disegna_fine()

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
          with open('score.txt', 'r') as f:
            f_contest = f.readlines()
            r_contatore = f_contest[0]
          f.close()

          # Apri il file in modalita scrittura
          with open('score.txt', 'w') as f:
            nuovo = int(r_contatore)+1
            f.write(str(nuovo) + "\n")
            for i in range(len(f_contest)):
              if i > 0:
                f.write(f_contest[i])
            f.write(str(nuovo) + " " + str(vg.punti) + "\n")
          f.close()

          vg.character = 0
          vg.flag_fine = False
          vg.flag_corretta = False
          vg.flag_muoviti = False
          vg.vite = 3
          SCHERMO.fill((0,0,0))
          running_fine = False
    aggiorna()

if __name__ == "__main__":
	main_fine()	