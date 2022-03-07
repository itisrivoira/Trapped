import pygame

pygame.init()

### carico immagini ##############################################
img_titolo = pygame.image.load('./IMMAGINI/homePage.png')
img_btn_gioca = pygame.image.load('./IMMAGINI/BUTTON/img_gioca.png')
img_btn_gioca_on = pygame.image.load('./IMMAGINI/BUTTON/img_gioca_on.png')
img_btn_impos = pygame.image.load('./IMMAGINI/BUTTON/img_impostazioni.png')
img_btn_impos_on = pygame.image.load('./IMMAGINI/BUTTON/img_impostazioni_on.png')
img_btn_class = pygame.image.load('./IMMAGINI/BUTTON/img_classifica.png')
img_btn_class_on = pygame.image.load('./IMMAGINI/BUTTON/img_classifica_on.png')

### settaggi #####################################################
SCHERMO = pygame.display.set_mode((800,600))
pygame.display.set_caption("Trapped")
FPS = 60

### classi #######################################################
class Button():
	def __init__(self, img = "", punto_x = 0, punto_y = 0):
		self.setImmagine(img)
		self.setCord_x(punto_x)
		self.setCord_y(punto_y)
		self.setWidth()
		self.setHeight()
		self.disegna()
	
	def setImmagine(self, i):
		self.immagine = i
	
	def getImmagine(self):
		return self.immagine
	
	def setCord_x(self, x):
		self.cordX = x
	
	def getCord_x(self):
		return self.cordX
	
	def setCord_y(self, y):
		self.cordY = y
	
	def getCord_y(self):
		return self.cordY
	
	def setWidth(self):
		self.width = self.immagine.get_width()	#metodo di pygame per ottenere la lunghezza
	
	def getWidth(self):
		return self.width
		
	def setHeight(self):
		self.height = self.immagine.get_height()	#metodo di pygame per ottenere l'altezza
	
	def getHeight(self):
		return self.height
	
	def disegna(self):
		SCHERMO.blit(self.immagine, (self.cordX, self.cordY))
	
	def on_button(self, muose_x, mouose_y, img, img_on):
		self.setWidth()
		self.setHeight()
		
		if muose_x >= self.cordX and muose_x <= (self.cordX + self.width) and mouose_y >= self.cordY and mouose_y <= (self.cordY + self.height):
			self.setImmagine(img_on)
			self.disegna()
		else:
			self.setImmagine(img)
			self.disegna()

##################################################################

def aggiorna():
	pygame.display.update()
	pygame.time.Clock().tick(FPS)

btn_impos = Button(img_btn_impos, 175, 400)
btn_gioca = Button(img_btn_gioca, 320, 400)
btn_class = Button(img_btn_class, 580, 400)

while True:			
	for event_pausa in pygame.event.get():
		SCHERMO2 = pygame.display.set_mode((800,600))
		SCHERMO2.blit(img_titolo,(0,100))
		
		if (event_pausa.type == pygame.QUIT):
			pygame.quit()
			
		cordM_x, cordM_y = pygame.mouse.get_pos()
		btn_impos.on_button(cordM_x, cordM_y, img_btn_impos, img_btn_impos_on)
		btn_gioca.on_button(cordM_x, cordM_y, img_btn_gioca, img_btn_gioca_on)
		btn_class.on_button(cordM_x, cordM_y, img_btn_class, img_btn_class_on)
	aggiorna()
		
