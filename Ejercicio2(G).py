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
celdaYFichas1 = fila1.under(fichasNegras)
celdaYFichas2 = fila2.under(peonesNegros)
celdasVacias = fila1.up(fila2).verticalRepeat(2)
celdaYFichas3 = fila1.under(peonesBlancos)
celdaYFichas4 = fila2.under(fichasBlancas)

#CREACIÓN DE TABLERO
tablero = celdaYFichas1.up(celdaYFichas2).up(celdasVacias).up(celdaYFichas3).up(celdaYFichas4)

draw(tablero)