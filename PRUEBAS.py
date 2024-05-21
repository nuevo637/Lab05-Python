from interpreter import draw
from chessPictures import *

peon = Picture(KING)
#ficha = Picture(SQUARE)
tablero = peon.horizontalRepeat(3)
draw(tablero)
