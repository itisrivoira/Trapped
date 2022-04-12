import pygame, sys

class Testo():
  def __init__(self, font, size, testo, colore, punto_x, punto_y):
    self.setFont(font)
    self.setSize(size)
    self.setTesto(testo)
    self.setColore(colore)
    self.setCord_x(punto_x)
    self.setCord_y(punto_y)
    self.f = pygame.font.Font(self.font, self.size)
    self.surf_text = self.f.render(self.testo, True, self.colore)
	
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


class Button():
  def __init__(self, img = "", punto_x = 0, punto_y = 0):
    self.setImmagine(img)
    self.setCord_x(punto_x)
    self.setCord_y(punto_y)
    self.setWidth()
    self.setHeight()
	
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

  def on_button(self, mouse_x, mouse_y, img, img_on):		
    if mouse_x >= self.cordX and mouse_x <= (self.cordX + self.width) and mouse_y >= self.cordY and mouse_y <= (self.cordY + self.height):
      self.setImmagine(img_on)
    else:
      self.setImmagine(img)
	
  def pressed_button(self, mouse_x, mouse_y):
    if mouse_x >= self.cordX and mouse_x <= (self.cordX + self.width) and mouse_y >= self.cordY and mouse_y <= (self.cordY + self.height):
      return True


class Immagini():
  def __init__(self, img = "", punto_x = 0, punto_y = 0):
    self.setImmagine(img)
    self.setCord_x(punto_x)
    self.setCord_y(punto_y)
	
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

class Personaggio():
  def __init__(self, img = "", punto_x = 0, punto_y = 0):
    self.setImmagine(img)
    self.setCord_x(punto_x)
    self.setCord_y(punto_y)
    self.setWidth()
    self.setHeight()

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