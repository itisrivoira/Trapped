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
  domanda = domande.domande[0][0][0]
  corr = domande.domande[0][1][0]
  ris = [domande.domande[0][1][0], domande.domande[0][2][0], domande.domande[0][3][0], domande.domande[0][4][0]]
  random.shuffle(ris)
  global d 
  d = classi.Testo("./font/Retro Gaming.ttf", 20, domanda, (0,0,0), 50, 50)
  for i in range (4):
    if ris[i]=='Nessuna delle precedenti':
      ris[i]='Nessuna' + "\n" + 'delle precedenti'
      f = True
  img_btn1= creabtn(ris[0], f)
  img_btn2 = creabtn(ris[1], f)
  img_btn3 = creabtn(ris[2], f)
  img_btn4 = creabtn(ris[3], f)
  global d1, d2, d3, d4 
  d1 = classi.Button(img_btn1, 60, 150)
  d2 = classi.Button(img_btn2, 360, 150)
  d3 = classi.Button(img_btn3, 60, 300)
  d4 = classi.Button(img_btn4, 360, 300)

def disegna_main():
  SCHERMO.blit(img_pc.getImmagine(), ( img_pc.getCord_x(), img_pc.getCord_y() ))
  SCHERMO.blit(d1.getImmagine(),(d1.getCord_x(), d1.getCord_y()))
  SCHERMO.blit(d2.getImmagine(),(d2.getCord_x(), d2.getCord_y()))
  SCHERMO.blit(d3.getImmagine(),(d3.getCord_x(), d3.getCord_y()))
  SCHERMO.blit(d4.getImmagine(),(d4.getCord_x(), d4.getCord_y()))
  SCHERMO.blit(d.surf_text, (d.getCord_x(), d.getCord_y()))

running = True
disegna_domanda()
while running:
    disegna_main()
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        if event.type == pygame.MOUSEBUTTONDOWN:
          statod1 = d1.setImmagine()
    aggiorna()