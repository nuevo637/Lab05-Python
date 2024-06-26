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

  #1. FUNCIÓN REALIZADA: DEVUELVE LA IMAGEN REFLEJADA VERTICALMENTE
  def verticalMirror(self):
    vertical = []
    for value in self.img:
      vertical.append(value[::-1])
    return Picture(vertical)

  #2. FUNCIÓN REALIZADA: DEVUELVE LA IMAGEN REFLEJADA HORIZONTALMENTE
  def horizontalMirror(self):
    horizontal = []
    for i in range(len(self.img), -1, -1):
      horizontal.append(self.img[i -1])
    return Picture(horizontal)

  #3. FUNCIÓN REALIZADA: DEVUELVE EL COLOR CONTRARIO DE LA IMAGEN
  def negative(self):
      negativo = []
      for value in self.img:
          filaInvertida = ""
          for caracter in value:
              filaInvertida += self._invColor(caracter)
          negativo.append(filaInvertida)
      return Picture(negativo)

  #4. FUNCIÓN REALIZADA: DEVUELVE UNA NUEVA FIGURA AL LADO DERECHO
  def join(self, p):
    unido = []
    for i in range(len(self.img)):
      filaJunta = self.img[i] + p.img[i]
      unido.append(filaJunta)
    return Picture(unido)

  #5. FUNCIÓN REALIZADA: DEVUELVE UNA FIGURA SELF ENCIMA DE LA FIGURA P 
  def up(self, p):
    compuesto = []
    for fila in self.img:
      compuesto.append(fila)
    for fila in p.img:
      compuesto.append(fila)
    return Picture(compuesto)

  #6. FUNCIÓN REALIZADA: DEVUELVE UNA FIGURA P ENCIMA DE LA FIGURA SELF 
  def under(self, p):
    sobrepuesto = []
    for fila_index, fila in enumerate(p.img):  
      filaSobrepuesta = ""
      for col_index, caracter in enumerate(fila):  
        if caracter != " ":
          filaSobrepuesta += caracter
        else:
          filaSobrepuesta += self.img[fila_index][col_index]  
      sobrepuesto.append(filaSobrepuesta)
    return Picture(sobrepuesto)
  
  #7. FUNCIÓN REALIZADA: Repite n veces al lado derecho la imagen generada
  def horizontalRepeat(self, n):
    repetidoH = []
    for fila in self.img:
      filaRepetida = fila * n
      repetidoH.append(filaRepetida)
    return Picture(repetidoH)

  #8. FUNCIÓN REALIZADA: Repite n veces hacia la dirección de abajo
  def verticalRepeat(self, n):
    repetidoV = []
    for i in range(n):
      for fila in self.img:
        repetidoV.append(fila)
    return Picture(repetidoV)

  #Extra 9.: Sólo para realmente viciosos 
  def rotate(self):
    b = []
    lenSelf = len(self.img)
    for i in range(lenSelf):
      a = ""
      for value in self.img:
        a += value[lenSelf - 1 - i]
      b.append(a)
    return Picture(b)

