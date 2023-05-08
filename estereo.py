"""
    Quinta tarea de APA - Sonido estéreo y ficheros WAVE

    Nombre y apellidos: RAfael A. Echevarria Silva

"""

import struct as str

def estereo2mono(ficEste, ficMono, canal=2):
    """
    La función lee el fichero ficEste, que debe contener una señal estéreo, y escribe el fichero ficMono,
    con una señal monofónica. El tipo concreto de señal que se almacenará en ficMono depende del argumento canal.
    """

    with open(ficEste, 'rb') as input_file:
        contenido = input_file.readlines()

    if canal == 0:
        mono_signal = [line.split()[0] for line in contenido]
    
    elif canal == 1:
        mono_signal = [line.split()[1] for line in contenido]
    
    elif canal == 2:
        mono_signal = [(float(line.split()[0]) + float(line.split()[1])) / 2 for line in contenido]

    elif canal == 3:
        mono_signal = [(float(line.split()[0]) - float(line.split()[1])) / 2 for line in contenido]
    
    else:
        raise ValueError("El valor del 'canal' debe ser 0, 1, 2 o 3.")
    
    with open(ficMono, 'wb') as output_file:
        output_file.write('\n'.join(map(str, mono_signal)))

    print("Señal estéreo convertida a señal mono con éxito.")
    
def codEstereo(ficEste, ficCod):
    """
    
    """

    with open(ficEste, 'rb') as input_file:
        contenido = input_file.readlines()

    cod_signal = []

    for line in contenido:
        left_channel, right_channel = map(int, line.strip().split())
        cod_sample = (left_channel << 16) | (right_channel & 0xFFFF)
        cod_signal.append(str(cod_sample))

    with open(ficCod, 'wb') as output_file:
        output_file.write('\n'.join(cod_signal))

    print("Señal estéreo codificada con éxito.")