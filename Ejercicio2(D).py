from interpreter import draw
from chessPictures import *

celdaBlanca = Picture(SQUARE)
celdaNegra = celdaBlanca.negative()
tablero = celdaBlanca.join(celdaNegra).horizontalRepeat(4)
draw(tablero)