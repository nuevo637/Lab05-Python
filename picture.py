from colors import *
class Picture:
  def __init__(self, img):
    self.img = img;

  def __eq__(self, other):
    return self.img == other.img

  def _invColor(self, color):
    if color not in inverter:
      return color
    return inverter[color]

  #FUNCIÓN REALIZADA: DEVUELVE LA IMAGEN REFLEJADA VERTICALMENTE
  def verticalMirror(self):
    vertical = []
    for value in self.img:
      vertical.append(value[::-1])
    return vertical

  #FUNCIÓN PENDIENTE: 
  def horizontalMirror(self):
    """ Devuelve el espejo horizontal de la imagen """
    return Picture(None)

  #FUNCIÓN REALIZADA: DEVUELVE EL COLOR CONTRARIO DE LA IMAGEN
  def negative(self):
      negativo = []
      for value in self.img:
          filaInvertida = ""
          for character in value:
              inverted_character = self._invColor(character)
              filaInvertida += inverted_character
          negativo.append(filaInvertida)
      return Picture(negativo)

  #FUNCIÓN PENDIENTE: DEVUELVE UNA NUEVA FIGURA AL LADO DERECHO
  def join(self, p):
    unido = []
    for value in self.img:
      filaJunta = ""
      filaJunta += value + p[value]
    return Picture(None)

  #FUNCIÓN PENDIENTE: 
  def up(self, p):
    return Picture(None)

  #FUNCIÓN PENDIENTE: 
  def under(self, p):
    """ Devuelve una nueva figura poniendo la figura p sobre la
        figura actual """
    return Picture(None)
  
  #FUNCIÓN PENDIENTE: 
  def horizontalRepeat(self, n):
    """ Devuelve una nueva figura repitiendo la figura actual al costado
        la cantidad de veces que indique el valor de n """
    return Picture(None)

  #FUNCIÓN PENDIENTE: 
  def verticalRepeat(self, n):
    return Picture(None)

  #Extra: Sólo para realmente viciosos 
  def rotate(self):
    """Devuelve una figura rotada en 90 grados, puede ser en sentido horario
    o antihorario"""
    return Picture(None)

