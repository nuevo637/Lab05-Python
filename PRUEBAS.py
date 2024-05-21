from interpreter import draw
from chessPictures import *

peon = Picture(KNIGHT)
#ficha = Picture(SQUARE)
tablero = peon.horizontalMirror()
draw(tablero)
