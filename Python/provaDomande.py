import pygame, sys, random
import classi, domande, gameOver
from PIL import Image, ImageFont, ImageDraw
import copy
import varGlobali as vg

pygame.init()

img_pc = pygame.image.load('./IMMAGINI/INTRO/pc.webp')
img_vuota = Image.open('./prova/img_vuota.png')
img_ris = Image.open('./prova/img_vuota.png')
img_vuota_on = Image.open('./prova/img_vuota_on.png')
img_cuore = pygame.image.load('./IMMAGINI/BUTTON/cuore.png')
img_cuore_u = pygame.image.load('./IMMAGINI/BUTTON/cuore_usato.png')
img_btn_tornaIndietro = pygame.image.load('./IMMAGINI/BUTTON//img_tornaIndietro.png')
pygame.display.set_caption("Trapped")
SCHERMO = pygame.display.set_mode((600,600))
FPS = 60
img_pc = classi.Immagini(img_pc, 0, 0)

def aggiorna():
	pygame.display.update()
	pygame.time.Clock().tick(FPS)

def blit_text(surface, text, pos, font, color=pygame.Color('black')):
  words = [word.split(' ') for word in text.splitlines()]
  space = font.size(' ')[0]
  max_width, max_height = surface.get_size()
  max_width = 570
  x, y = pos
  pygame.draw.rect(SCHERMO, (255,255,255), (30, 80, 540, 120),0, border_radius=10)
  for line in words:
      for word in line:
          word_surface = font.render(word, 0, color)
          word_width, word_height = word_surface.get_size()
          if x + word_width >= max_width:
              x = pos[0]
              y += word_height
          surface.blit(word_surface, (x, y))
          x += word_width + space
      x = pos[0]
      y += word_height
  pygame.draw.rect(SCHERMO, (0,0,0), (30, 80, 540, 120),5, border_radius=10)

def allinea(ogg, allOri):
  if allOri == True:
    metaShermoW = SCHERMO.get_width()/2
    metaTestoW = ogg.surf_text.get_width()/2
    nuova_x = metaShermoW-metaTestoW
    ogg.setCord_x(nuova_x)

def disegna_domanda():
  global d, ris, ris_A, ris_B, ris_C, ris_D, r1, r2, r3, r4, giusta, sbagliata, cuore_1, cuore_2, cuore_3, btn_tornaIndietro4
  d = domande.domande[1][0][0]
  ris = [domande.domande[0][1][0], domande.domande[0][2][0], domande.domande[0][3][0], domande.domande[0][4][0]]
  random.shuffle(ris)
  
  ris_A = classi.Testo("./font/Retro Gaming.ttf", 20, ris[0], (0, 0, 0), 200, 250)
  ris_B = classi.Testo("./font/Retro Gaming.ttf", 20, ris[1], (0, 0, 0), 200, 320)
  ris_C = classi.Testo("./font/Retro Gaming.ttf", 20, ris[2], (0, 0, 0), 200, 390)
  ris_D = classi.Testo("./font/Retro Gaming.ttf", 20, ris[3], (0, 0, 0), 200, 460)

  r1 = classi.Rettangolo(110, 250, 400, ris_A.altT, (0, 0, 0), (255, 255, 255))
  r2 = classi.Rettangolo(110, 320, 400, ris_B.altT, (0, 0, 0), (255, 255, 255))
  r3 = classi.Rettangolo(110, 390, 400, ris_C.altT, (0, 0, 0), (255, 255, 255))
  r4 = classi.Rettangolo(110, 460, 400, ris_D.altT, (0, 0, 0), (255, 255, 255))

  giusta = classi.Testo("./font/Retro Gaming.ttf", 30, "Corretta!", (0, 255, 0), 300, 530)

  cuore_1 = classi.Immagini(img_cuore, 15, 15)
  cuore_2 = classi.Immagini(img_cuore, 55, 15)
  cuore_3 = classi.Immagini(img_cuore, 95, 15)

  btn_tornaIndietro4 = classi.Button(img_btn_tornaIndietro, 50, 500)

def controlla_risp(r):
  global cuore_1, cuore_2, cuore_3
  corr = domande.domande[0][1][0]
  if (str(r)==corr):
    vg.flag_corretta = True
    print(vg.flag_corretta)
  else:
    vg.flag_corretta = False
    vg.vite = vg.vite - 1
    print(vg.flag_corretta)

def disegna_main():
  global ris_A, ris_B, ris_C, ris_D, r1, r2, r3, r4, giusta, sbagliata, cuore_1, cuore_2, cuore_3, btn_tornaIndietro4

  SCHERMO.blit(img_pc.getImmagine(), ( img_pc.getCord_x(), img_pc.getCord_y() ))
  
  #stampo domanda
  font = pygame.font.Font("./font/Retro Gaming.ttf", 20)

  blit_text(SCHERMO, d, (60, 100), font)

  #stampo rispota A
  pygame.draw.rect(SCHERMO, r1.colB, (r1.x-10, r1.y-10, 400, r1.h+20), 0, border_radius=10)
  pygame.draw.rect(SCHERMO, r1.c, (r1.x-10, r1.y-10, 400, r1.h+20), 5, border_radius=10)
  allinea(ris_A, True)
  SCHERMO.blit(ris_A.surf_text, ( ris_A.getCord_x(), ris_A.getCord_y() ))

  #stampo rispota B
  pygame.draw.rect(SCHERMO, r2.colB, (r2.x-10, r2.y-10, 400, r2.h+20), 0, border_radius=10)
  pygame.draw.rect(SCHERMO, r2.c, (r2.x-10, r2.y-10, 400, r2.h+20), 5, border_radius=10)
  allinea(ris_B, True)
  SCHERMO.blit(ris_B.surf_text, ( ris_B.getCord_x(), ris_B.getCord_y() ))

  #stampo rispota C
  pygame.draw.rect(SCHERMO, r3.colB, (r3.x-10, r3.y-10, 400, r3.h+20), 0, border_radius=10)
  pygame.draw.rect(SCHERMO, r3.c, (r3.x-10, r3.y-10, 400, r3.h+20), 5, border_radius=10)
  allinea(ris_C, True)
  SCHERMO.blit(ris_C.surf_text, ( ris_C.getCord_x(), ris_C.getCord_y() ))

  #stampo rispota D
  pygame.draw.rect(SCHERMO, r4.colB, (r4.x-10, r4.y-10, 400, r4.h+20), 0, border_radius=10)
  pygame.draw.rect(SCHERMO, r4.c, (r4.x-10, r4.y-10, 400, r4.h+20), 5, border_radius=10)
  allinea(ris_D, True)
  SCHERMO.blit(ris_D.surf_text, ( ris_D.getCord_x(), ris_D.getCord_y() ))

  if vg.flag_corretta == True:
    SCHERMO.blit(btn_tornaIndietro4.getImmagine(), ( btn_tornaIndietro4.getCord_x(), btn_tornaIndietro4.getCord_y() ))
    allinea(giusta, True)
    SCHERMO.blit(giusta.surf_text, ( giusta.getCord_x(), giusta.getCord_y() ))
  
  pygame.draw.rect(SCHERMO, (255,255,255), (0, 0, 150, 70),0, border_bottom_right_radius=20)
  if vg.vite == 3:
    SCHERMO.blit(cuore_1.getImmagine(), ( cuore_1.getCord_x(), cuore_1.getCord_y() ))
    SCHERMO.blit(cuore_2.getImmagine(), ( cuore_2.getCord_x(), cuore_2.getCord_y() ))
    SCHERMO.blit(cuore_3.getImmagine(), ( cuore_3.getCord_x(), cuore_3.getCord_y() ))
  elif vg.vite == 2:
    cuore_3.setImmagine(img_cuore_u)
    SCHERMO.blit(cuore_1.getImmagine(), ( cuore_1.getCord_x(), cuore_1.getCord_y() ))
    SCHERMO.blit(cuore_2.getImmagine(), ( cuore_2.getCord_x(), cuore_2.getCord_y() ))
    SCHERMO.blit(cuore_3.getImmagine(), ( cuore_3.getCord_x(), cuore_3.getCord_y() ))
  elif vg.vite == 1:
    cuore_3.setImmagine(img_cuore_u)
    cuore_2.setImmagine(img_cuore_u)
    SCHERMO.blit(cuore_1.getImmagine(), ( cuore_1.getCord_x(), cuore_1.getCord_y() ))
    SCHERMO.blit(cuore_2.getImmagine(), ( cuore_2.getCord_x(), cuore_2.getCord_y() ))
    SCHERMO.blit(cuore_3.getImmagine(), ( cuore_3.getCord_x(), cuore_3.getCord_y() ))
  elif vg.vite == 0:
    vg.flag_gameOver = True
    cuore_3.setImmagine(img_cuore_u)
    cuore_2.setImmagine(img_cuore_u)
    cuore_1.setImmagine(img_cuore_u)
    SCHERMO.blit(cuore_1.getImmagine(), ( cuore_1.getCord_x(), cuore_1.getCord_y() ))
    SCHERMO.blit(cuore_2.getImmagine(), ( cuore_2.getCord_x(), cuore_2.getCord_y() ))
    SCHERMO.blit(cuore_3.getImmagine(), ( cuore_3.getCord_x(), cuore_3.getCord_y() ))
  pygame.draw.rect(SCHERMO, (0,0,0), (-5, -5, 155, 75),5, border_bottom_right_radius=20)

def main_domande():
  global ris_A, ris_B, ris_C, ris_D, r1, r2, r3, r4, cuore_1, cuore_2, cuore_3, btn_tornaIndietro4
  running = True
  disegna_domanda()
  while running:
      disegna_main()
      for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

        #ottengo cordiante mouse
        cordMouse_x, cordMouse_y = pygame.mouse.get_pos()

        #verifico se passo sopra ad un button
        on_out_r1 = r1.on_button(cordMouse_x, cordMouse_y)

        coloreB = (255, 255, 255)
        coloreN = (0, 0, 0)

        if on_out_r1 == True:
          ris_A.aggiorna_colore(coloreB)
        else:
          ris_A.aggiorna_colore(coloreN)
          
        on_out_r2 = r2.on_button(cordMouse_x, cordMouse_y)
        if on_out_r2 == True:
          ris_B.aggiorna_colore(coloreB)
        else:
          ris_B.aggiorna_colore(coloreN)
        
        on_out_r3 = r3.on_button(cordMouse_x, cordMouse_y)
        if on_out_r3 == True:
          ris_C.aggiorna_colore(coloreB)
        else:
          ris_C.aggiorna_colore(coloreN)
        
        on_out_r4 = r4.on_button(cordMouse_x, cordMouse_y)
        if on_out_r4 == True:
          ris_D.aggiorna_colore(coloreB)
        else:
          ris_D.aggiorna_colore(coloreN)
        
        #verifico se clicco un buttton
        if event.type == pygame.MOUSEBUTTONDOWN:

          stato_risp_A = r1.pressed_button(cordMouse_x, cordMouse_y)
          if stato_risp_A == True:
            controlla_risp(ris[0])
          
          stato_risp_B = r2.pressed_button(cordMouse_x, cordMouse_y)
          if stato_risp_B == True:
            controlla_risp(ris[1])

          stato_risp_C = r3.pressed_button(cordMouse_x, cordMouse_y)
          if stato_risp_C == True:
            controlla_risp(ris[2])
          
          stato_risp_D = r4.pressed_button(cordMouse_x, cordMouse_y)
          if stato_risp_D == True:
            controlla_risp(ris[3])
          
          stato = btn_tornaIndietro4.pressed_button(cordMouse_x, cordMouse_y)
          if stato == True:
            running = False
            
        if vg.flag_gameOver == True:
          running = False
          gameOver.main_gameOver()
      aggiorna()

if __name__ == "__main__":
	main_domande()