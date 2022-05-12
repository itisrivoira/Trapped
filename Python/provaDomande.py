import pygame, sys, random
import classi, domande
from PIL import Image, ImageFont, ImageDraw 

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

def creabtn(testo):
  image_editable = ImageDraw.Draw(img_vuota)
  image_editable.text((5,5), testo, (0,0,0), font=font)
  img_vuota.save("result.png")
  img_prova = pygame.image.load('./result.png')
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
  #print(ris[0])
  img_btn1= creabtn(ris[0])
  global d1 
  d1 = classi.Button(img_btn1, 60, 150)

def disegna_main():
  SCHERMO.blit(img_pc.getImmagine(), ( img_pc.getCord_x(), img_pc.getCord_y() ))
  SCHERMO.blit(d1.getImmagine(),(d1.getCord_x(), d1.getCord_y()))

running = True
disegna_domanda()
while running:
    disegna_main()
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    aggiorna()