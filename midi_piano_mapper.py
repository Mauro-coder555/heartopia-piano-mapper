import mido
from pynput.keyboard import Controller, Key
import time

# ==============================
# CONFIG
# ==============================
mido.set_backend('mido.backends.rtmidi')
keyboard = Controller()

# ==============================
# FUNCIONES DE PRESIÓN SEGURA
# ==============================

def press_key(key):
    if isinstance(key, tuple):
        # combinación (ej: Shift + tecla)
        keyboard.press(key[0])
        keyboard.press(key[1])
    else:
        keyboard.press(key)

def release_key(key):
    if isinstance(key, tuple):
        keyboard.release(key[1])
        keyboard.release(key[0])
    else:
        keyboard.release(key)

# ==============================
# MAPPING MIDI → TECLAS
# ==============================
from pynput.keyboard import KeyCode

    # =========================
    # LOW OCTAVE (C3–B3)
    # =========================


mapping = {
    48: KeyCode.from_vk(0xBC),  # ,
    49: KeyCode.from_vk(0x4C),  # L
    50: KeyCode.from_vk(0xBE),  # .
    51: KeyCode.from_vk(0xBA),  # ;
    52: KeyCode.from_vk(0xBF),  # /
    53: KeyCode.from_vk(0x4F),  # O
    54: KeyCode.from_vk(0x30),  # 0
    55: KeyCode.from_vk(0x50),  # P
    56: KeyCode.from_vk(0xBD),  # -
    57: KeyCode.from_vk(0xDB),  # [
    58: KeyCode.from_vk(0xBB),  # =
    59: KeyCode.from_vk(0xDD),  # ],

    # =========================
    # MIDDLE OCTAVE (C4–B4)
    # =========================
    60: 'z',
    61: 's',
    62: 'x',
    63: 'd',
    64: 'c',
    65: 'v',
    66: 'g',
    67: 'b',
    68: 'h',
    69: 'n',
    70: 'j',
    71: 'm',

    # =========================
    # HIGH OCTAVE (C5–C6)
    # =========================
    72: 'q',
    73: '2',
    74: 'w',
    75: '3',
    76: 'e',
    77: 'r',
    78: '5',
    79: 't',
    80: '6',
    81: 'y',
    82: '7',
    83: 'u',
    84: 'i',
}

# ==============================
# MIDI LOOP
# ==============================

print("Puertos disponibles:")
for name in mido.get_input_names():
    print("-", name)

port_name = input("\nEscribe el nombre EXACTO del puerto: ")

with mido.open_input(port_name) as port:
    print("Escuchando MIDI...")

    for msg in port:

        if msg.type == 'clock':
            continue

        if msg.note not in mapping:
            continue

        if msg.type == 'note_on' and msg.velocity > 0:
            press_key(mapping[msg.note])

        if msg.type == 'note_off' or (msg.type == 'note_on' and msg.velocity == 0):
            release_key(mapping[msg.note])