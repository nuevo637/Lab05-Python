from interpreter import draw
from chessPictures import *

caballo1 = Picture(KNIGHT)
caballo2 = caballo1.negative()
fila1 = caballo1.join(caballo2)
fila2 = fila1.verticalMirror()
tablero = fila1.up(fila2)
draw(tablero)
