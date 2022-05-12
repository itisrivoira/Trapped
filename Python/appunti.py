class Domande(Testo):
  def __init__(self, img = "", testo = "", corretta = "", punto_x = 0, punto_y = 0):
      super().__init__("./font/Retro Gaming.ttf", 20, testo, (0,0,0), punto_x, punto_y)
      self.setImmagine(img)
      super().setCord_x(punto_x)
      super().setCord_y(punto_y)
      self.x = super().setCord_x(punto_x)
      self.y = super().setCord_y(punto_y)
      self.setTesto(testo)
      self.setCorretta(corretta)
  
  def setImmagine(self, i):
    self.__immagine = i
	
  def getImmagine(self):
    return self.__immagine
  
  def setTesto(self, testo):
    self.domanda = testo
  
  def setCorretta(self, corretta):
    self.__corretta = corretta
	
  def getCorretta(self):
    return self.__corretta