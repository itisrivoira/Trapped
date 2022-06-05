import pygame, sys
import classi
import impostazioni, gioco, classifica
pygame.init()

MUL = 0.75

### carico immagini ##############################################
img_intro = pygame.image.load('./IMMAGINI/INTRO/sfondo.png').convert()
img_intro = pygame.transform.scale(img_intro, ( img_intro.get_width()*MUL, img_intro.get_height()*MUL ))
img_btn_gioca = pygame.image.load('./IMMAGINI/BUTTON/img_gioca.png')
img_btn_gioca_on = pygame.image.load('./IMMAGINI/BUTTON/img_gioca_on.png')
img_btn_impos = pygame.image.load('./IMMAGINI/BUTTON/img_impostazioni.png')
img_btn_impos_on = pygame.image.load('./IMMAGINI/BUTTON/img_impostazioni_on.png')
img_btn_class = pygame.image.load('./IMMAGINI/BUTTON/img_classifica.png')
img_btn_class_on = pygame.image.load('./IMMAGINI/BUTTON/img_classifica_on.png')
img_icon = pygame.image.load('./IMMAGINI/ICON/icon.png')

### settaggi #####################################################
SCHERMO = pygame.display.set_mode((600,600))
pygame.display.set_caption("Trapped")
pygame.display.set_icon(img_icon)
FPS = 60

### programma ####################################################
img_sfondo = classi.Immagini(img_intro, 0, 0)
txt_tit = classi.Testo("./font/04B_30__.TTF", 90, "Trapped", (255, 255, 255), 40, 150)
btn_impos = classi.Button(img_btn_impos, 50, 450)
btn_gioca = classi.Button(img_btn_gioca, 50, 380)
btn_class = classi.Button(img_btn_class, 165, 450)

def aggiorna():
	pygame.display.update()
	pygame.time.Clock().tick(FPS)

def disegna_main():
  SCHERMO.blit(img_sfondo.getImmagine(), ( img_sfondo.getCord_x(), img_sfondo.getCord_y() ))
  SCHERMO.blit(txt_tit.surf_text, ( txt_tit.getCord_x(), txt_tit.getCord_y() ))
  SCHERMO.blit(btn_impos.getImmagine(), ( btn_impos.getCord_x(), btn_impos.getCord_y() ))
  SCHERMO.blit(btn_gioca.getImmagine(), ( btn_gioca.getCord_x(), btn_gioca.getCord_y() ))
  SCHERMO.blit(btn_class.getImmagine(), ( btn_class.getCord_x(), btn_class.getCord_y() ))

def main_home():
  running = True
  while running:

    disegna_main()
    
    for event in pygame.event.get():
      if event.type == pygame.QUIT:
        pygame.quit()
        sys.exit()

      #ottengo cordiante mouse
      cordMouse_x, cordMouse_y = pygame.mouse.get_pos()

      #verifico se passo sopra ad un button
      btn_impos.on_button(cordMouse_x, cordMouse_y, img_btn_impos, img_btn_impos_on)
      btn_gioca.on_button(cordMouse_x, cordMouse_y, img_btn_gioca, img_btn_gioca_on)
      btn_class.on_button(cordMouse_x, cordMouse_y, img_btn_class, img_btn_class_on)
      
      #verifico se clicco un buttton
      if event.type == pygame.MOUSEBUTTONDOWN:

        stato_btnImp = btn_impos.pressed_button(cordMouse_x, cordMouse_y)
        if stato_btnImp == True:
          impostazioni.main_impostazioni()

        stato_btnGio = btn_gioca.pressed_button(cordMouse_x, cordMouse_y)
        if stato_btnGio == True:
          gioco.main_gioco()

        stato_btnCla = btn_class.pressed_button(cordMouse_x, cordMouse_y)
        if stato_btnCla == True:
          classifica.main_classifica()
    aggiorna()

if __name__ == "__main__":
	main_home()	