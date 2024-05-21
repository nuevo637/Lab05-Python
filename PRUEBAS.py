from interpreter import draw
from chessPictures import *

peon = Picture(KNIGHT)
#ficha = Picture(SQUARE)
tablero = peon.verticalRepeat(4)
draw(tablero)
