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
          for caracter in value:
              filaInvertida += self._invColor(caracter)
          negativo.append(filaInvertida)
      return Picture(negativo)

  #FUNCIÓN REALIZADA: DEVUELVE UNA NUEVA FIGURA AL LADO DERECHO
  def join(self, p):
    unido = []
    for i in range(len(self.img)):
      filaJunta = self.img[i] + p.img[i]
      unido.append(filaJunta)
    return Picture(unido)

  #FUNCIÓN REALIZADA: DEVUELVE UNA FIGURA SELF ENCIMA DE LA FIGURA P 
  def up(self, p):
    sobrepuesto = []
    for fila in self.img:  
      filaSobrepuesta = ""
      for caracter in fila:  
        if caracter != " ":
          filaSobrepuesta += caracter  
        else:
          filaSobrepuesta += p.img[self.img.index(fila)][fila.index(caracter)]
      sobrepuesto.append(filaSobrepuesta)
    return Picture(sobrepuesto)

  #FUNCIÓN REALIZADA: DEVUELVE UNA FIGURA P ENCIMA DE LA FIGURA SELF 
  def under(self, p):
    sobrepuesto = []
    for fila in p.img:  
      filaSobrepuesta = ""
      for caracter in fila:  
        if caracter != " ":
          filaSobrepuesta += caracter
        else:
          filaSobrepuesta += self.img[p.img.index(fila)][fila.index(caracter)]  
      sobrepuesto.append(filaSobrepuesta)
    return Picture(sobrepuesto)
  
  #FUNCIÓN REALIZADA: Repite n veces al lado derecho la imagen generada
  def horizontalRepeat(self, n):
    repetidoH = []
    for fila in self.img:
      filaRepetida = fila * n
      repetidoH.append(filaRepetida)
    return Picture(repetidoH)

  #FUNCIÓN PENDIENTE: 
  def verticalRepeat(self, n):
    return Picture(None)

  #Extra: Sólo para realmente viciosos 
  def rotate(self):
    """Devuelve una figura rotada en 90 grados, puede ser en sentido horario
    o antihorario"""
    return Picture(None)

