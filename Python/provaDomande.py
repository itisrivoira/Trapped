import pygame, sys
import classi, domande

pygame.init()

img_pc = pygame.image.load('./IMMAGINI/INTRO/pc.webp')
pygame.display.set_caption("Trapped")
SCHERMO = pygame.display.set_mode((600,600))
FPS = 60
img_pc = classi.Immagini(img_pc, 0, 0)

def aggiorna():
	pygame.display.update()
	pygame.time.Clock().tick(FPS)

def disegna_main():
  SCHERMO.blit(img_pc.getImmagine(), ( img_pc.getCord_x(), img_pc.getCord_y() ))

running = True
while running:
    disegna_main()

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    aggiorna()