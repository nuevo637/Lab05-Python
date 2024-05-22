from interpreter import draw
from chessPictures import *


#CREACIÓN DE PIEZAS
celdaBlanca = Picture(SQUARE)
celdaNegra = celdaBlanca.negative()
torre = Picture(ROCK)
caballo = Picture(KNIGHT)
alfil = Picture(BISHOP)
reyna = Picture(QUEEN)
rey = Picture(KING)
peon = Picture(PAWN)

#FICHAS
fichasBlancas = torre.join(caballo).join(alfil).join(reyna).join(rey).join(alfil).join(caballo).join(torre)
peonesBlancos = peon.horizontalRepeat(8)
fichasNegras = fichasBlancas.negative()
peonesNegros = peonesBlancos.negative()

#FILAS
fila1 = celdaBlanca.join(celdaNegra).horizontalRepeat(4)
fila2 = celdaNegra.join(celdaBlanca).horizontalRepeat(4)

#FILAS Y FICHAS
filass = fila1.under(peonesBlancos)

#CREACIÓN DE TABLERO


#CREACIÓN DEL TABLERO

draw(filass)