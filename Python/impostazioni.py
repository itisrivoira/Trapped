import pygame, sys
import classi
pygame.init()

### carico immagini ##############################################
img_btn_acceso = pygame.image.load('./IMMAGINI/BUTTON/img_acceso.png')
img_btn_acceso_on = pygame.image.load('./IMMAGINI/BUTTON/img_acceso_on.png')
img_btn_spento = pygame.image.load('./IMMAGINI/BUTTON/img_spento.png')
img_btn_spento_on = pygame.image.load('./IMMAGINI/BUTTON/img_spento_on.png')
img_btn_tornaIndietro = pygame.image.load('./IMMAGINI/BUTTON/img_tornaIndietro.png')
img_icon = pygame.image.load('./IMMAGINI/ICON/icon.png')

### carico suoni ##############################################
musica = pygame.mixer.Sound('./sound/sound.ogg')

### settaggi #####################################################
SCHERMO = pygame.display.set_mode((600,600))
pygame.display.set_caption("Trapped")
pygame.display.set_icon(img_icon)
FPS = 60

### programma ####################################################
txt_impo = classi.Testo("./font/Retro Gaming.ttf", 60, "Impostazioni", (255, 255, 255), 150, 50)
txt_musica = classi.Testo("./font/Retro Gaming.ttf", 40, "Musica", (255, 255, 255), 125, 200)
txt_suoni = classi.Testo("./font/Retro Gaming.ttf", 40, "Suoni", (255, 255, 255), 125, 350)
btn_musica_acceso = classi.Button(img_btn_acceso, 400, 200)
btn_musica_spento = classi.Button(img_btn_spento_on, 500, 200)
btn_suoni_acceso = classi.Button(img_btn_acceso, 400, 350)
btn_suoni_spento = classi.Button(img_btn_spento_on, 500, 350)
btn_tornaIndietro = classi.Button(img_btn_tornaIndietro, 100, 500)

def aggiorna():
	pygame.display.update()
	pygame.time.Clock().tick(FPS)

def disegna_impo():
  SCHERMO.blit(txt_impo.surf_text, ( txt_impo.getCord_x(), txt_impo.getCord_y() ))
  SCHERMO.blit(txt_musica.surf_text, ( txt_musica.getCord_x(), txt_musica.getCord_y() ))
  SCHERMO.blit(txt_suoni.surf_text, ( txt_suoni.getCord_x(), txt_suoni.getCord_y() ))
  SCHERMO.blit(btn_musica_acceso.getImmagine(), ( btn_musica_acceso.getCord_x(), btn_musica_acceso.getCord_y() ))
  SCHERMO.blit(btn_musica_spento.getImmagine(), ( btn_musica_spento.getCord_x(), btn_musica_spento.getCord_y() ))
  SCHERMO.blit(btn_suoni_acceso.getImmagine(), ( btn_suoni_acceso.getCord_x(), btn_suoni_acceso.getCord_y() ))
  SCHERMO.blit(btn_suoni_spento.getImmagine(), ( btn_suoni_spento.getCord_x(), btn_suoni_spento.getCord_y() ))
  SCHERMO.blit(btn_tornaIndietro.getImmagine(), ( btn_tornaIndietro.getCord_x(), btn_tornaIndietro.getCord_y() ))

def main_impostazioni():
  SCHERMO.fill((0,0,0))
  running_impostazioni = True

  while running_impostazioni:

    disegna_impo()

    for event in pygame.event.get():
      if event.type == pygame.QUIT:
        pygame.quit()
        sys.exit()
        
      #ottengo coordinate mouse
      cordMouse_x, cordMouse_y = pygame.mouse.get_pos()

      #verifico se passo sopra ad un button
      #btn_musica_acceso.on_button(cordMouse_x, cordMouse_y, img_btn_acceso, img_btn_acceso_on)
      #btn_musica_spento.on_button(cordMouse_x, cordMouse_y, img_btn_spento, img_btn_spento_on)
      #btn_suoni_acceso.on_button(cordMouse_x, cordMouse_y, img_btn_acceso, img_btn_acceso_on)
      #btn_suoni_spento.on_button(cordMouse_x, cordMouse_y, img_btn_spento, img_btn_spento_on)

      #verifico se clicco un button
      if event.type == pygame.MOUSEBUTTONDOWN:
        f=False
        stato_bntMusOn = btn_musica_acceso.pressed_button(cordMouse_x, cordMouse_y)
        if stato_bntMusOn == True  and f == False:
          musica.play()
          f=True
          btn_musica_acceso.setImmagine(img_btn_acceso_on)
          btn_musica_spento.setImmagine(img_btn_spento)

        stato_btnMusOff = btn_musica_spento.pressed_button(cordMouse_x, cordMouse_y)
        if stato_btnMusOff == True:
          musica.stop()
          btn_musica_acceso.setImmagine(img_btn_acceso)
          btn_musica_spento.setImmagine(img_btn_spento_on)
        
        #da finire mettere suoni per quando premi i tasti
        #bug da correggiere se clicco pulsante già acceso
        stato_btnSonOn = btn_suoni_acceso.pressed_button(cordMouse_x, cordMouse_y)
        if stato_btnSonOn == True:
          btn_suoni_acceso.setImmagine(img_btn_acceso_on)
          btn_suoni_spento.setImmagine(img_btn_spento)

        stato_btnSonOff = btn_suoni_spento.pressed_button(cordMouse_x, cordMouse_y)
        if stato_btnSonOff == True:
          btn_suoni_acceso.setImmagine(img_btn_acceso)
          btn_suoni_spento.setImmagine(img_btn_spento_on)

        stato_btnInd = btn_tornaIndietro.pressed_button(cordMouse_x, cordMouse_y)
        if stato_btnInd == True:
          SCHERMO.fill((0,0,0))
          running_impostazioni = False
    aggiorna()

if __name__ == "__main__":
  main_impostazioni()	
		
