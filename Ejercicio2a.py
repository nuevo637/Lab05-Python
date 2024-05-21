from interpreter import draw
from chessPictures import *

peon = Picture(BISHOP)
rey = Picture(KING)
tablero = peon.join(rey)
draw(tablero)