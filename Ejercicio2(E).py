from interpreter import draw
from chessPictures import *

celdaBlanca = Picture(SQUARE)
celdaNegra = celdaBlanca.negative()
tablero = celdaNegra.join(celdaBlanca).horizontalRepeat(4)
draw(tablero)