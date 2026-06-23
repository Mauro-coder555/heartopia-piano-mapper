# Heartopia MIDI Piano Mapper

Proyecto en Python para tocar el piano de **Heartopia** usando un teclado, piano o controlador MIDI real.

El programa escucha las notas MIDI de un dispositivo físico y las convierte en pulsaciones del teclado de la PC, usando el mapeo necesario para el piano de Heartopia en modo **3 octavas**.

## Qué hace

Heartopia permite tocar su piano usando el teclado de la computadora. Este proyecto permite reemplazar esa experiencia por un controlador MIDI real.

En resumen:

```text
Teclado MIDI → Nota MIDI → Tecla de PC → Piano de Heartopia
```

## Tecnologías usadas

* Python
* Mido
* python-rtmidi
* pynput
* Tkinter

## Estructura del proyecto

```text
heartopia-midi-piano-mapper/
├── README.md
├── requirements.txt
└── midi_gui.py
```

## Requisitos

Antes de usar el proyecto necesitás:

* Python instalado.
* Un teclado, piano o controlador MIDI conectado a la PC.
* Heartopia abierto.
* El piano de Heartopia configurado en modo **3 octavas**.
* El teclado de la PC configurado en **Inglés / US**.

## Instalación

Clonar o descargar el proyecto:

```bash
git clone https://github.com/tu-usuario/heartopia-midi-piano-mapper.git
cd heartopia-midi-piano-mapper
```

Crear un entorno virtual:

```bash
python -m venv .venv
```

Activarlo en Windows:

```bash
.venv\Scripts\activate
```

Activarlo en macOS o Linux:

```bash
source .venv/bin/activate
```

Instalar dependencias:

```bash
pip install -r requirements.txt
```

El archivo `requirements.txt` debería contener:

```txt
mido
python-rtmidi
pynput
```

## Uso

Ejecutar la aplicación:

```bash
python midi_gui.py
```

Luego:

1. Seleccionar el puerto MIDI desde la interfaz.
2. Presionar **Iniciar**.
3. Abrir Heartopia y entrar al piano.
4. Tocar desde el teclado MIDI real.

La interfaz también incluye un botón para detener la escucha y otro para liberar teclas en caso de que alguna quede presionada.

## Mapeo MIDI

El mapeo está pensado para el piano de Heartopia en modo **3 octavas**.

Cubre estas notas MIDI:

```text
48–59  → Octava baja
60–71  → Octava media
72–84  → Octava alta
```

Algunas teclas especiales usan códigos virtuales de Windows para asegurar que símbolos como coma, punto, punto y coma, corchetes y otros caracteres funcionen correctamente.

## Consideraciones

El proyecto está pensado principalmente para Windows y para usar el layout de teclado **Inglés / US**.

Si el sistema operativo usa otra distribución de teclado, algunas teclas pueden no coincidir con las que espera Heartopia.

## Estado

El proyecto está funcional y permite tocar el piano de Heartopia usando un controlador MIDI real mediante una interfaz gráfica simple.
::: 
