from interpreter import draw
from chessPictures import *

caballo1 = Picture(KNIGHT)
caballo2 = Picture(KNIGHT)
tablero = caballo1.up(caballo2)
draw(tablero)
