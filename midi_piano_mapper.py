import mido
import threading
import tkinter as tk
from tkinter import ttk, messagebox
from pynput.keyboard import Controller, KeyCode
import time

# ==============================
# CONFIG
# ==============================

mido.set_backend('mido.backends.rtmidi')
keyboard = Controller()

running = False
midi_thread = None
current_port = None
pressed_notes = set()

# ==============================
# KEY HELPERS
# ==============================

def press_key(key):
    keyboard.press(key)

def release_key(key):
    keyboard.release(key)

def release_all_keys():
    global pressed_notes

    for note in list(pressed_notes):
        key = mapping.get(note)
        if key:
            try:
                release_key(key)
            except Exception:
                pass

    pressed_notes.clear()
    log("Todas las teclas fueron liberadas.")

# ==============================
# MAPPING MIDI → TECLAS
# ==============================

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
    59: KeyCode.from_vk(0xDD),  # ]

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

def midi_listener(port_name):
    global running, current_port

    try:
        with mido.open_input(port_name) as port:
            current_port = port
            log(f"Escuchando MIDI en: {port_name}")

            for msg in port:
                if not running:
                    break

                if msg.type not in ('note_on', 'note_off'):
                    continue

                if msg.note not in mapping:
                    continue

                key = mapping[msg.note]

                if msg.type == 'note_on' and msg.velocity > 0:
                    if msg.note not in pressed_notes:
                        press_key(key)
                        pressed_notes.add(msg.note)
                        log(f"NOTE ON  {msg.note}")

                elif msg.type == 'note_off' or (msg.type == 'note_on' and msg.velocity == 0):
                    if msg.note in pressed_notes:
                        release_key(key)
                        pressed_notes.remove(msg.note)
                        log(f"NOTE OFF {msg.note}")

    except Exception as e:
        log(f"Error: {e}")
        messagebox.showerror("Error MIDI", str(e))

    finally:
        release_all_keys()
        running = False
        set_status("Detenido")

# ==============================
# GUI ACTIONS
# ==============================

def start_listening():
    global running, midi_thread

    if running:
        return

    port_name = port_combo.get()

    if not port_name:
        messagebox.showwarning("Puerto MIDI", "Seleccioná un puerto MIDI.")
        return

    running = True
    set_status("Escuchando")

    midi_thread = threading.Thread(
        target=midi_listener,
        args=(port_name,),
        daemon=True
    )
    midi_thread.start()

def stop_listening():
    global running
    running = False
    release_all_keys()
    set_status("Detenido")
    log("Escucha detenida.")

def refresh_ports():
    ports = mido.get_input_names()
    port_combo["values"] = ports

    if ports:
        port_combo.current(0)
        log("Puertos actualizados.")
    else:
        log("No se encontraron puertos MIDI.")

def log(text):
    log_box.insert(tk.END, text + "\n")
    log_box.see(tk.END)

def set_status(text):
    status_label.config(text=f"Estado: {text}")

# ==============================
# TKINTER UI
# ==============================

root = tk.Tk()
root.title("MIDI to Keyboard Mapper")
root.geometry("520x380")

main_frame = ttk.Frame(root, padding=12)
main_frame.pack(fill=tk.BOTH, expand=True)

title_label = ttk.Label(
    main_frame,
    text="MIDI to Keyboard Mapper",
    font=("Arial", 16, "bold")
)
title_label.pack(anchor="w", pady=(0, 12))

port_frame = ttk.Frame(main_frame)
port_frame.pack(fill=tk.X, pady=(0, 8))

ttk.Label(port_frame, text="Puerto MIDI:").pack(side=tk.LEFT)

port_combo = ttk.Combobox(port_frame, state="readonly")
port_combo.pack(side=tk.LEFT, fill=tk.X, expand=True, padx=8)

refresh_button = ttk.Button(port_frame, text="Actualizar", command=refresh_ports)
refresh_button.pack(side=tk.LEFT)

buttons_frame = ttk.Frame(main_frame)
buttons_frame.pack(fill=tk.X, pady=8)

start_button = ttk.Button(buttons_frame, text="Iniciar", command=start_listening)
start_button.pack(side=tk.LEFT, padx=(0, 8))

stop_button = ttk.Button(buttons_frame, text="Detener", command=stop_listening)
stop_button.pack(side=tk.LEFT, padx=(0, 8))

panic_button = ttk.Button(
    buttons_frame,
    text="Liberar teclas",
    command=release_all_keys
)
panic_button.pack(side=tk.LEFT)

status_label = ttk.Label(main_frame, text="Estado: Detenido")
status_label.pack(anchor="w", pady=(8, 8))

log_box = tk.Text(main_frame, height=12)
log_box.pack(fill=tk.BOTH, expand=True)

refresh_ports()

root.protocol("WM_DELETE_WINDOW", lambda: (stop_listening(), root.destroy()))
root.mainloop()