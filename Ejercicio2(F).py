from interpreter import draw
from chessPictures import *

celdaBlanca = Picture(SQUARE)
celdaNegra = celdaBlanca.negative()
fila1 = celdaBlanca.join(celdaNegra).horizontalRepeat(4)
fila2 = celdaNegra.join(celdaBlanca).horizontalRepeat(4)
filas = fila1.up(fila2)
tablero = filas.verticalRepeat(2)
draw(tablero)