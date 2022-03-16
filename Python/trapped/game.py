import pygame
from menu import *
pygame.init()

img_titolo = pygame.image.load('./IMMAGINI/homePage.png')
img_btn_gioca = pygame.image.load('./IMMAGINI/BUTTON/img_gioca.png')
img_btn_gioca_on = pygame.image.load('./IMMAGINI/BUTTON/img_gioca_on.png')
img_btn_impos = pygame.image.load('./IMMAGINI/BUTTON/img_impostazioni.png')
img_btn_impos_on = pygame.image.load('./IMMAGINI/BUTTON/img_impostazioni_on.png')
img_btn_class = pygame.image.load('./IMMAGINI/BUTTON/img_classifica.png')
img_btn_class_on = pygame.image.load('./IMMAGINI/BUTTON/img_classifica_on.png')

pygame.display.set_caption("Trapped")
FPS = 60

class Game():
	def __init__(self):
		self.running, self.playing = True, False
		self.UP_KEY, self.DOWN_KEY, self.START_KEY, self.BACK_KEY = False, False, False, False
		self.DISPLAY_W, self.DISPLAY_H = 800, 600
		self.display = pygame.Surface((self.DISPLAY_W,self.DISPLAY_H))
		self.window = pygame.display.set_mode(((self.DISPLAY_W,self.DISPLAY_H)))
		self.font_name = 'Retro Gaming.ttf'
		#self.font_name = pygame.font.get_default_font()
		self.BLACK, self.WHITE = (0, 0, 0), (255, 255, 255)
		self.main_menu = MainMenu(self)
		self.options = OptionsMenu(self)
		self.credits = CreditsMenu(self)
		self.curr_menu = self.main_menu

	def game_loop(self):
		while self.playing:
			self.check_events()
			if self.START_KEY:
				self.playing= False
			self.display.fill(self.BLACK)
			self.draw_text('game', 20, self.DISPLAY_W/2, self.DISPLAY_H/2)
			self.window.blit(self.display, (0,0))
			pygame.display.update()
			self.reset_keys()

	def check_events(self):
		for event in pygame.event.get():
			self.display.blit(img_titolo,(0,100))
			if event.type == pygame.QUIT:
				self.running, self.playing = False, False
				self.curr_menu.run_display = False
			if event.type == pygame.KEYDOWN:
				if event.key == pygame.K_RETURN:
					self.START_KEY = True
				if event.key == pygame.K_BACKSPACE:
					self.BACK_KEY = True
				if event.key == pygame.K_DOWN:
					self.DOWN_KEY = True
				if event.key == pygame.K_UP:
					self.UP_KEY = True

	def reset_keys(self):
		self.UP_KEY, self.DOWN_KEY, self.START_KEY, self.BACK_KEY = False, False, False, False

	def draw_text(self, text, size, x, y ):
		font = pygame.font.Font(self.font_name,size)
		text_surface = font.render(text, True, self.WHITE)
		text_rect = text_surface.get_rect()
		text_rect.center = (x,y)
		self.display.blit(text_surface,text_rect)

	def update():
		pygame.display.update()
		pygame.time.Clock().tick(FPS)

class Img():
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
	
	def on_button(self, mouse_x, mouse_y, img, img_on):
		self.setWidth()
		self.setHeight()
		
		if mouse_x >= self.cordX and mouse_x <= (self.cordX + self.width) and mouse_y >= self.cordY and mouse_y <= (self.cordY + self.height):
			self.setImmagine(img_on)
			self.disegna()
		else:
			self.setImmagine(img)
			self.disegna()