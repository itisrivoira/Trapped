import pygame
import varGlobali as vg

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
  def __init__(self, img, x, y):
    if vg.character == 0:
      testo = "UOMO/uomo_"
    else:
      testo = "DONNA/donna_"
    self.animazione_down = ["./IMMAGINI/PERSONAGGI/"+testo+"davanti_1.png", "./IMMAGINI/PERSONAGGI/"+testo+"davanti_2.png", "./IMMAGINI/PERSONAGGI/"+testo+"davanti_3.png"]
    self.animazione_up = ["./IMMAGINI/PERSONAGGI/"+testo+"dietro_1.png", "./IMMAGINI/PERSONAGGI/"+testo+"dietro_2.png", "./IMMAGINI/PERSONAGGI/"+testo+"dietro_3.png"]
    self.animazione_left = ["./IMMAGINI/PERSONAGGI/"+testo+"sinistra_1.png", "./IMMAGINI/PERSONAGGI/"+testo+"sinistra_2.png", "./IMMAGINI/PERSONAGGI/"+testo+"sinistra_3.png"]

    self.contatore_valore = 0.9
    self.is_walking = False

    self.cont_ani_up = 0
    self.cont_ani_down = 0
    self.cont_ani_right = 0
    self.cont_ani_left = 0

    self.up = False
    self.down = False
    self.right = False
    self.left = False

    self.setImmagine(img)
    self.setCord_x(x)
    self.setCord_y(y)
    self.velX = 0
    self.velY = 0
    self.left_pressed = False
    self.right_pressed = False
    self.up_pressed = False
    self.down_pressed = False
    self.speed = 3

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

  #  --- SETTO I FLAG ---

  def setDownPressed(self, v):
    self.down_pressed = v

  def setUpPressed(self, v):
    self.up_pressed = v

  def setLeftPressed(self, v):
      self.left_pressed = v

  def setRightPressed(self, v):
    self.right_pressed = v

  def getDownPressed(self):
    return self.down_pressed

  def getUpPressed(self):
    return self.up_pressed

  def getLeftPressed(self):
    return self.left_pressed

  def getRightPressed(self):
    return self.right_pressed

  def setIsWalking(self, walk):
    self.is_walking = walk

  def getIsWalking(self):
    return self.is_walking

  def update(self):
    self.velX = 0
    self.velY = 0
    velocita = 0.1
    u = self.getUpPressed()
    d = self.getDownPressed()
    l = self.getLeftPressed()
    r = self.getRightPressed()

    if self.getIsWalking() == True:
      
      if d == True:
        self.down = True
        self.cont_ani_down += velocita
        if self.cont_ani_down > len(self.animazione_down):
          self.cont_ani_down = self.contatore_valore
        self.setImmagine(pygame.image.load(self.animazione_down[int(self.cont_ani_down)]))
      elif u == True:
        self.up = True
        self.cont_ani_up += velocita
        if self.cont_ani_up > len(self.animazione_up):
          self.cont_ani_up = self.contatore_valore
        self.setImmagine(pygame.image.load(self.animazione_up[int(self.cont_ani_up)]))
      elif l == True:
        self.left = True
        self.cont_ani_left += velocita
        if self.cont_ani_left > len(self.animazione_left):
          self.cont_ani_left = self.contatore_valore
        self.setImmagine(pygame.image.load(self.animazione_left[int(self.cont_ani_left)]))
      elif r == True:
        self.right = True
        self.cont_ani_right += velocita
        if self.cont_ani_right > len(self.animazione_left):
          self.cont_ani_right = self.contatore_valore
        self.setImmagine(pygame.transform.flip(pygame.image.load(self.animazione_left[int(self.cont_ani_right)]), True, False))
    else:
      if self.down == True:
        self.cont_ani_down = self.contatore_valore
        self.setImmagine(pygame.image.load(self.animazione_down[int(self.cont_ani_down)]))
        self.down = False
      if self.up == True:
        self.cont_ani_up = self.contatore_valore
        self.setImmagine(pygame.image.load(self.animazione_up[int(self.cont_ani_up)]))
        self.up = False
      if self.left == True:
        self.cont_ani_left = self.contatore_valore
        self.setImmagine(pygame.image.load(self.animazione_left[int(self.cont_ani_left)]))
        self.left = False
      if self.right == True:
        self.cont_ani_right = self.contatore_valore
        self.setImmagine(pygame.transform.flip(pygame.image.load(self.animazione_left[int(self.cont_ani_right)]), True, False))
        self.right = False
    
    if self.getLeftPressed() and not self.getRightPressed():
      self.velX = -self.speed
    if self.getRightPressed() and not self.getLeftPressed():
      self.velX = self.speed
    if self.getUpPressed() and not self.getDownPressed():
      self.velY = -self.speed
    if self.getDownPressed() and not self.getUpPressed():
      self.velY = self.speed     

    self.setCord_x(self.getCord_x() + self.velX)
    self.setCord_y(self.getCord_y() + self.velY)