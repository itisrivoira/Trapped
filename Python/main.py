import pygame, sys
import impostazioni, classifica, gioco
pygame.init()

### carico immagini ##############################################
img_btn_gioca = pygame.image.load('./IMMAGINI/BUTTON/img_gioca.png')
img_btn_gioca_on = pygame.image.load('./IMMAGINI/BUTTON/img_gioca_on.png')
img_btn_impos = pygame.image.load('./IMMAGINI/BUTTON/img_impostazioni.png')
img_btn_impos_on = pygame.image.load('./IMMAGINI/BUTTON/img_impostazioni_on.png')
img_btn_class = pygame.image.load('./IMMAGINI/BUTTON/img_classifica.png')
img_btn_class_on = pygame.image.load('./IMMAGINI/BUTTON/img_classifica_on.png')
img_icon = pygame.image.load('./IMMAGINI/ICON/icon.png')

### settaggi #####################################################
SCHERMO = pygame.display.set_mode((800,600))
pygame.display.set_caption("Trapped")
pygame.display.set_icon(img_icon)
FPS = 60

### classi #######################################################
class Testo():
	def __init__(self, font, size, testo, colore, punto_x, punto_y, allineamento):
		self.setFont(font)
		self.setSize(size)
		self.setTesto(testo)
		self.setColore(colore)
		self.setCord_x(punto_x)
		self.setCord_y(punto_y)
		self.setAll(allineamento)
		self.disegna()
	
	def setFont(self, f):
		self.font = f
	
	def getFont(self):
		return self.font
	
	def setSize(self, s):
		self.size = s
	
	def getSize(self):
		return self.size
	
	def setTesto(self, t):
		self.testo = t
	
	def getTesto(self):
		return self.testo
	
	def setColore(self, c):
		self.colore = c
	
	def getColore(self):
		return self.colore
		
	def setCord_x(self, x):
		self.cordX = x
	
	def getCord_x(self):
		return self.cordX
	
	def setCord_y(self, y):
		self.cordY = y
	
	def getCord_y(self):
		return self.cordY
		
	def setAll(self, a):
		self.all = a
	
	def getAll(self):
		return self.all
	
	def disegna(self):
		self.f = pygame.font.Font(self.font, self.size)
		self.surf_text = self.f.render(self.testo, True, self.colore)
		if self.getAll() == "centro":
			self.metaSchermoW = SCHERMO.get_width()/2
			self.metaSchermoH = SCHERMO.get_height()/2
			self.metaTestoW = self.surf_text.get_width()/2
			self.metaTestoH = self.surf_text.get_height()/2
			nuova_x = self.metaSchermoW-self.metaTestoW
			nuova_y = self.metaSchermoH-self.metaTestoH-100
			self.setCord_x(nuova_x)
			self.setCord_y(nuova_y)
			SCHERMO.blit(self.surf_text, (self.cordX, self.cordY))
		

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
		self.width = self.immagine.get_width()
	
	def getWidth(self):
		return self.width
		
	def setHeight(self):
		self.height = self.immagine.get_height()
	
	def getHeight(self):
		return self.height
	
	def disegna(self):
		SCHERMO.blit(self.immagine, (self.cordX, self.cordY))
	
	def on_button(self, mouse_x, mouse_y, img, img_on):		
		if mouse_x >= self.cordX and mouse_x <= (self.cordX + self.width) and mouse_y >= self.cordY and mouse_y <= (self.cordY + self.height):
			self.setImmagine(img_on)
			self.disegna()
		else:
			self.setImmagine(img)
			self.disegna()
	
	def pressed_button(self, mouse_x, mouse_y, pagina):
		if mouse_x >= self.cordX and mouse_x <= (self.cordX + self.width) and mouse_y >= self.cordY and mouse_y <= (self.cordY + self.height):
			print("Click " + pagina)
			if pagina == "impostazioni":
				impostazioni.main_impostazioni()
				SCHERMO.fill((0,0,0))
				titolo = Testo("./font/04B_30__.TTF", 100, "Trapped", (255, 255, 255), 0, 0, "centro")
			elif pagina == "gioca":
				gioco.main_gioco()
				SCHERMO.fill((0,0,0))
				titolo = Testo("./font/04B_30__.TTF", 100, "Trapped", (255, 255, 255), 0, 0, "centro")
			elif pagina == "classifica":
				classifica.main_classifica()
				SCHERMO.fill((0,0,0))
				titolo = Testo("./font/04B_30__.TTF", 100, "Trapped", (255, 255, 255), 0, 0, "centro")
			 
##################################################################

def aggiorna():
	pygame.display.update()
	pygame.time.Clock().tick(FPS)

titolo = Testo("./font/04B_30__.TTF", 100, "Trapped", (255, 255, 255), 0, 0, "centro")
btn_impos = Button(img_btn_impos, 175, 350)
btn_gioca = Button(img_btn_gioca, 320, 350)
btn_class = Button(img_btn_class, 580, 350)

running = True
while running:		
	for event in pygame.event.get():
		if event.type == pygame.QUIT:
			running = False
			pygame.quit()
			sys.exit()

		#ottengo cordiante mouse
		cordMouse_x, cordMouse_y = pygame.mouse.get_pos()
		#con esc chiude tutto
		if event.type == pygame.KEYDOWN:
			if event.key == pygame.K_ESCAPE:
				pygame.quit()
				sys.exit()

		#verifico se passo sopra ad un button
		btn_impos.on_button(cordMouse_x, cordMouse_y, img_btn_impos, img_btn_impos_on)
		btn_gioca.on_button(cordMouse_x, cordMouse_y, img_btn_gioca, img_btn_gioca_on)
		btn_class.on_button(cordMouse_x, cordMouse_y, img_btn_class, img_btn_class_on)
		
		#verifico se clicco un buttton
		if event.type == pygame.MOUSEBUTTONDOWN:
			cordMClick_x, cordMClick_y = pygame.mouse.get_pos()
			btn_impos.pressed_button(cordMClick_x, cordMClick_y, "impostazioni")
			btn_gioca.pressed_button(cordMClick_x, cordMClick_y, "gioca")
			btn_class.pressed_button(cordMClick_x, cordMClick_y, "classifica")
	aggiorna()