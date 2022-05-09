import pygame, sys
import classi, domande

pygame.init()

img_pc = pygame.image.load('./IMMAGINI/INTRO/pc.webp')
img_vuota = pygame.image.load('./prova/img_vuota.png')
img_vuota_on = pygame.image.load('./prova/img_vuota_on.png')
pygame.display.set_caption("Trapped")
SCHERMO = pygame.display.set_mode((600,600))
FPS = 60
img_pc = classi.Immagini(img_pc, 0, 0)

def aggiorna():
	pygame.display.update()
	pygame.time.Clock().tick(FPS)

def disegna_domanda():
  i=0
  #[0][1][0] primo la domanda,secondo risposta alla domanda, l'ultimo sempre a 0 o è out of range
  for i in range(11):
    domanda = domande.domande[0][0][0]
    txt_d = classi.Domande((0,0,0), domanda, (0,1,0), 60, 50)
    SCHERMO.blit(txt_d.surf_text, ( txt_d.getCord_x(), txt_d.getCord_y() ))

def disegna_main():
  SCHERMO.blit(img_pc.getImmagine(), ( img_pc.getCord_x(), img_pc.getCord_y() ))

running = True
while running:
    disegna_main()
    disegna_domanda()
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    aggiorna()