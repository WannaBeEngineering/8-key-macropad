# Basic KMK code for the WannaBe Engineering 8-Key macropad
# To customize your keymap, and all other possibilities visit https://kmkfw.io/keycodes/
# Big thanks to the team at KMK for providing their code to the public

import board

from kmk.kmk_keyboard import KMKKeyboard
from kmk.keys import KC
from kmk.scanners import DiodeOrientation

kb = KMKKeyboard()

kb.col_pins = (board.GP29, board.GP28, board.GP27, board.GP26)
kb.row_pins = (board.GP15, board.GP14)
kb.diode_orientation = DiodeOrientation.COL2ROW

kb.keymap = [
    [KC.N1, KC.N2, KC.N3, KC.N4, KC.N5, KC.N6, KC.N7, KC.N8]
]

if __name__ == '__main__':
    kb.go()