import pygame, sys
pygame.init()
### carico immagini ##############################################
img_btn_acceso = pygame.image.load('./IMMAGINI/BUTTON/img_acceso.png')
img_btn_acceso_on = pygame.image.load('./IMMAGINI/BUTTON/img_acceso_on.png')
img_btn_spento = pygame.image.load('./IMMAGINI/BUTTON/img_spento.png')
img_btn_spento_on = pygame.image.load('./IMMAGINI/BUTTON/img_spento_on.png')
img_btn_tornaIndietro = pygame.image.load('./IMMAGINI/BUTTON//img_tornaIndietro.png')
img_icon = pygame.image.load('./IMMAGINI/ICON/icon.png')

### carico suoni ##############################################
pygame.mixer.music.load('./sound/sound.ogg')

### settaggi #####################################################
SCHERMO = pygame.display.set_mode((800,600))
pygame.display.set_caption("Trapped")
pygame.display.set_icon(img_icon)
FPS = 60

### classi #######################################################
class Testo():
	pygame.init()
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
			self.metaShermoW = SCHERMO.get_width()/2
			self.metaShermoH = SCHERMO.get_height()/2
			self.metaTestoW = self.surf_text.get_width()/2
			self.metaTestoH = self.surf_text.get_height()/2
			nuova_x = self.metaShermoW-self.metaTestoW
			#nuova_y = self.metaShermoH-self.metaTestoH
			self.setCord_x(nuova_x)
			#self.setCord_y(nuova_y)
			SCHERMO.blit(self.surf_text, (self.cordX, self.cordY))
		elif self.getAll() == "sinitra":
			self.metaShermoW = SCHERMO.get_width()/4
			self.metaShermoH = SCHERMO.get_height()/4
			self.metaTestoW = self.surf_text.get_width()/2
			self.metaTestoH = self.surf_text.get_height()/2
			nuova_x = self.metaShermoW-self.metaTestoW
			self.setCord_x(nuova_x)
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
			if pagina == "torna indietro":
				return False

##################################################################

def aggiorna():
	pygame.display.update()
	pygame.time.Clock().tick(FPS)

def disegna():
	### carico immagini ###
	img_btn_acceso = pygame.image.load('./IMMAGINI/BUTTON/img_acceso.png')
	img_btn_acceso_on = pygame.image.load('./IMMAGINI/BUTTON/img_acceso_on.png')
	img_btn_spento = pygame.image.load('./IMMAGINI/BUTTON/img_spento.png')
	img_btn_spento_on = pygame.image.load('./IMMAGINI/BUTTON/img_spento_on.png')
	img_btn_tornaIndietro = pygame.image.load('./IMMAGINI/BUTTON//img_tornaIndietro.png')
	titolo = Testo("./font/Retro Gaming.ttf", 70, "Classifica", (255, 255, 255), 0, 50, "centro")

def main_classifica():
	SCHERMO.fill((0,0,0))
	running_classifica = True
	while running_classifica:
		btn_tornaIndietro = Button(img_btn_tornaIndietro, 50, 500)
		disegna()
		for event in pygame.event.get():
			if event.type == pygame.QUIT:
				pygame.quit()
				sys.exit()	
			#ottengo coordinate mouse
			cordMouse_x, cordMouse_y = pygame.mouse.get_pos()
			#con esc chiude tutto
			if event.type == pygame.KEYDOWN:
				if event.key == pygame.K_ESCAPE:
					pygame.quit()
					sys.exit()
			#verifico se clicco un button
			if event.type == pygame.MOUSEBUTTONDOWN:
				cordMClick_x, cordMClick_y = pygame.mouse.get_pos()
				running_classifica = btn_tornaIndietro.pressed_button(cordMClick_x, cordMClick_y, "torna indietro")
		aggiorna()

if __name__ == "__main__":
	main_classifica()	