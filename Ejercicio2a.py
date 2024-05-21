from interpreter import draw
from chessPictures import *

peon = Picture(BISHOP)
peonNegro = peon.negative()
draw(peonNegro)