# Heartopia MIDI Piano Mapper

Proyecto en Python para tocar el piano del juego **Heartopia** usando un piano, teclado o controlador MIDI real.

El programa escucha las notas MIDI ejecutadas desde un dispositivo físico y las convierte en pulsaciones del teclado de la PC, respetando el mapeo específico del piano de Heartopia en su configuración de **3 octavas**.

## Índice

* [Descripción](#descripción)
* [Objetivo del proyecto](#objetivo-del-proyecto)
* [Tecnologías usadas](#tecnologías-usadas)
* [Estructura del proyecto](#estructura-del-proyecto)
* [Cómo funciona](#cómo-funciona)
* [Requisitos](#requisitos)
* [Instalación](#instalación)
* [Uso](#uso)
* [Mapeo MIDI](#mapeo-midi)
* [Consideraciones importantes](#consideraciones-importantes)
* [Limitaciones conocidas](#limitaciones-conocidas)
* [Posibles mejoras](#posibles-mejoras)
* [Estado del proyecto](#estado-del-proyecto)
* [Autor](#autor)

## Descripción

**Heartopia MIDI Piano Mapper** permite usar un teclado MIDI real para tocar el piano dentro de Heartopia.

Heartopia permite tocar su piano usando teclas del teclado de la computadora. Sin embargo, tocar melodías usando el teclado de la PC puede resultar incómodo o poco natural, especialmente cuando se necesita mayor rango, precisión o fluidez.

Este proyecto resuelve ese problema traduciendo notas MIDI a teclas del teclado de la computadora, permitiendo que cada nota tocada en el piano/controlador MIDI active la tecla correspondiente dentro del juego.

## Objetivo del proyecto

El objetivo principal es mejorar la experiencia de tocar el piano dentro de Heartopia, haciendo posible usar un instrumento físico real en lugar del teclado de la computadora.

Este proyecto combina música, gaming y automatización para lograr una experiencia más natural al tocar dentro del juego.

## Tecnologías usadas

* **Python**: lenguaje principal del proyecto.
* **Mido**: librería utilizada para recibir y procesar mensajes MIDI.
* **python-rtmidi**: backend MIDI utilizado por Mido para conectarse con dispositivos MIDI reales.
* **pynput**: librería utilizada para simular pulsaciones del teclado de la computadora.
* **Windows Virtual Key Codes**: usados para mapear correctamente algunas teclas especiales como coma, punto, punto y coma, corchetes y otros símbolos.

## Estructura del proyecto

La estructura sugerida del repositorio es:

```text
heartopia-midi-piano-mapper/
├── README.md
├── requirements.txt
└── heartopia_midi_piano_mapper.py
```

El archivo `requirements.txt` contiene las dependencias necesarias para ejecutar el proyecto:

```txt
mido
python-rtmidi
pynput
```

## Cómo funciona

El programa realiza los siguientes pasos:

1. Configura el backend MIDI usando `mido.backends.rtmidi`.
2. Detecta los puertos MIDI disponibles en la computadora.
3. Solicita al usuario el nombre exacto del puerto MIDI que quiere usar.
4. Abre ese puerto y comienza a escuchar eventos MIDI.
5. Cuando detecta una nota MIDI presionada, simula la pulsación de una tecla del teclado de la PC.
6. Cuando detecta que la nota MIDI fue soltada, libera también la tecla correspondiente.

En resumen:

```text
Teclado MIDI real → Nota MIDI → Tecla de PC → Nota en el piano de Heartopia
```

## Requisitos

Para usar este proyecto necesitás:

* Python instalado.
* Un teclado, piano o controlador MIDI conectado a la PC.
* El juego Heartopia abierto.
* El piano de Heartopia configurado en modo de 3 octavas.
* El idioma/distribución del teclado de la PC configurado en **Inglés / US**.

## Instalación

Primero, clonar o descargar este repositorio:

```bash
git clone https://github.com/tu-usuario/heartopia-midi-piano-mapper.git
cd heartopia-midi-piano-mapper
```

Luego instalar las dependencias desde `requirements.txt`:

```bash
pip install -r requirements.txt
```

También se pueden instalar manualmente con:

```bash
pip install mido python-rtmidi pynput
```

## Uso

Ejecutar el script principal:

```bash
python heartopia_midi_piano_mapper.py
```

Al iniciar, el programa mostrará los puertos MIDI disponibles:

```text
Puertos disponibles:
- Nombre de tu dispositivo MIDI
```

Luego pedirá ingresar el nombre exacto del puerto:

```text
Escribe el nombre EXACTO del puerto:
```

Una vez seleccionado el puerto, el programa comenzará a escuchar las notas MIDI.

Después, solo hay que abrir Heartopia, entrar al piano del juego y tocar desde el teclado MIDI real.

## Mapeo MIDI

El mapeo está diseñado específicamente para la configuración de **3 octavas** del piano de Heartopia.

El programa cubre tres rangos principales:

### Octava baja

Notas MIDI `48–59`.

Estas notas se asignan a teclas especiales y letras usadas por el layout inferior del piano en Heartopia.

Ejemplos:

```python
48: KeyCode.from_vk(0xBC)  # ,
49: KeyCode.from_vk(0x4C)  # L
50: KeyCode.from_vk(0xBE)  # .
```

### Octava media

Notas MIDI `60–71`.

Ejemplos:

```python
60: 'z'
61: 's'
62: 'x'
63: 'd'
64: 'c'
65: 'v'
```

### Octava alta

Notas MIDI `72–84`.

Ejemplos:

```python
72: 'q'
73: '2'
74: 'w'
75: '3'
76: 'e'
77: 'r'
```

## Consideraciones importantes

Este proyecto está pensado para funcionar con el teclado de la PC configurado en:

```text
Inglés / US keyboard layout
```

Esto es necesario porque Heartopia interpreta las teclas según una distribución específica. Si el sistema operativo está configurado con otro idioma o layout de teclado, algunas teclas pueden no coincidir con las esperadas por el juego.

Por ejemplo, símbolos como:

```text
, . ; / [ ] - =
```

pueden estar ubicados en posiciones distintas según el idioma del teclado.

Por ese motivo, para que el mapeo funcione correctamente, es importante cambiar la distribución del teclado de la PC a Inglés / US antes de usar el programa.

## Limitaciones conocidas

* El programa fue diseñado para la configuración de 3 octavas del piano de Heartopia.
* Actualmente está optimizado para Windows.
* Requiere que el teclado de la PC esté configurado en Inglés / US.
* Otros layouts de teclado pueden producir notas incorrectas dentro del juego.
* El usuario debe ingresar manualmente el nombre exacto del puerto MIDI.
* Si Heartopia modifica su sistema de teclas o su configuración de piano, puede ser necesario actualizar el mapeo.

## Posibles mejoras

Algunas mejoras posibles para futuras versiones:

* Selección automática del dispositivo MIDI.
* Archivo de configuración externo para personalizar el mapeo.
* Soporte para diferentes distribuciones de teclado.
* Interfaz gráfica simple.
* Presets para diferentes configuraciones del piano de Heartopia.
* Detección más robusta de mensajes MIDI que no sean notas.
* Opción para transponer octavas.
* Opción para cambiar el canal MIDI escuchado.

## Estado del proyecto

El proyecto se encuentra en estado funcional.

Actualmente permite tocar el piano de Heartopia con un teclado/controlador MIDI real usando la configuración de 3 octavas del juego.

## Autor

Proyecto creado como herramienta personal para mejorar la experiencia de tocar el piano dentro de Heartopia usando un instrumento MIDI real.

Combina música, gaming y automatización para transformar el piano del juego en una experiencia más cercana a tocar un teclado físico.
