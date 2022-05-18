import pygame, sys, random
import classi, domande
from PIL import Image, ImageFont, ImageDraw
import copy

pygame.init()

img_pc = pygame.image.load('./IMMAGINI/INTRO/pc.webp')
img_vuota = Image.open('./prova/img_vuota.png')
img_ris = Image.open('./prova/img_vuota.png')
img_vuota_on = Image.open('./prova/img_vuota_on.png')
pygame.display.set_caption("Trapped")
SCHERMO = pygame.display.set_mode((600,600))
FPS = 60
img_pc = classi.Immagini(img_pc, 0, 0)
font = ImageFont.truetype("./font/Retro Gaming.ttf", 15)

def creabtn(testo, f):
  prova = copy.deepcopy(img_vuota)
  i = 0
  image_editable = ImageDraw.Draw(prova)
  if f == True:
    image_editable.text((5,5), testo, (0,0,0), font=font)
  else:
    image_editable.text((10,10), testo, (0,0,0), font=font)
  prova.save("result" + str(i) +".png")
  img_prova = pygame.image.load('./result'+ str(i) + '.png')
  return img_prova

#def forward():
  #  global qnum
   # 
    #screen.fill(0)
    #if qnum < len(domande):
    #    time.sleep(.3)
    #    qnum += 1
    #    question(qnum)

def aggiorna():
	pygame.display.update()
	pygame.time.Clock().tick(FPS)

def disegna_domanda():
  global d, ris, d1, d2, d3, d4
  domanda = domande.domande[0][0][0]
  ris = [domande.domande[0][1][0], domande.domande[0][2][0], domande.domande[0][3][0], domande.domande[0][4][0]]
  random.shuffle(ris)
  d = classi.Testo("./font/Retro Gaming.ttf", 20, domanda, (0,0,0), 50, 50)
  for i in range (4):
    if ris[i]=='Nessuna delle precedenti':
      ris[i]='Nessuna' + "\n" + 'delle precedenti'
      f = True
  img_btn1= creabtn(ris[0], f)
  img_btn2 = creabtn(ris[1], f)
  img_btn3 = creabtn(ris[2], f)
  img_btn4 = creabtn(ris[3], f)
  d1 = classi.Button(img_btn1, 120, 170)
  d2 = classi.Button(img_btn2, 360, 170)
  d3 = classi.Button(img_btn3, 120, 300)
  d4 = classi.Button(img_btn4, 360, 300)

def controlla_risp(r):
  corr = domande.domande[0][1][0]
  #print(corr)
  if (str(r)==corr):
    print('corretta')
    SCHERMO.fill(0,0,0)
    yes = classi.Testo("./font/Retro Gaming.ttf", 40, 'risposta corretta', (255,255,255), 300,300)
    SCHERMO.blit(yes.surf_text, (yes.getCord_x(), yes.getCord_y()))
  else:
    print('sbagliatoo')

def disegna_main():
  SCHERMO.blit(img_pc.getImmagine(), ( img_pc.getCord_x(), img_pc.getCord_y() ))
  SCHERMO.blit(d1.getImmagine(),(d1.getCord_x(), d1.getCord_y()))
  SCHERMO.blit(d2.getImmagine(),(d2.getCord_x(), d2.getCord_y()))
  SCHERMO.blit(d3.getImmagine(),(d3.getCord_x(), d3.getCord_y()))
  SCHERMO.blit(d4.getImmagine(),(d4.getCord_x(), d4.getCord_y()))
  SCHERMO.blit(d.surf_text, (d.getCord_x(), d.getCord_y()))

def main_domande():
  running = True
  disegna_domanda()
  while running:
      disegna_main()
      for event in pygame.event.get():
          if event.type == pygame.QUIT:
              pygame.quit()
              sys.exit()
          cordMouse_x, cordMouse_y = pygame.mouse.get_pos()
          if event.type == pygame.MOUSEBUTTONDOWN:
            statod1 = d1.pressed_button(cordMouse_x, cordMouse_y)
            if statod1 == True:
              print("clicked d1")
              controlla_risp(ris[0])
            statod2 = d2.pressed_button(cordMouse_x, cordMouse_y)
            if statod2 == True:
              print("clicked d2")
              controlla_risp(ris[1])
            statod3 = d3.pressed_button(cordMouse_x, cordMouse_y)
            if statod3 == True:  
              print("clicked d3")
              controlla_risp(ris[2])
            statod4 = d4.pressed_button(cordMouse_x, cordMouse_y)
            if statod4 == True:
              print("clicked d4")
              controlla_risp(ris[3])
      aggiorna()

if __name__ == "__main__":
	main_domande()