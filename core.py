import os
import json

def clean():
    os.system('cls') and os.system('clear')

def tryExcept(variable):
    try:
        numero = int(variable)
        return numero
    except Exception:
        print('\nOpcion Invalida. . . El valor ingresado no es numerico.')
        input('\nPresione Enter para volver. . . ')

def leerArchivo(nombreArchivo):
    ciclo = True
    while(ciclo):
        localizacionArchivo = f'data/{nombreArchivo}.json'
        try:
            with open(localizacionArchivo, 'r') as archivo:
                contenido = archivo.read()
            contenidoDiccionario = json.loads(contenido)
            ciclo = False
            return contenidoDiccionario
        except Exception:
            with open(localizacionArchivo, 'x') as archivo:
                archivo.write('{}')

def escribirArchivo(nombrearchivo, escritura):
    localizacionArchivo = f'data/{nombrearchivo}.json'
    with open(localizacionArchivo, 'w') as archivo:
        archivo.write(escritura)

def convertirArchivo(diccionario):
    convertido = json.dumps(diccionario, indent = 4)
    return convertido

def menuPrincipal():
    clean()
    print('-'*10, '{:^40}'.format('CAMPUS MD'), '-'*10)
    print('-'*10, '{:^40}'.format('MENU PRINCIPAL'), '-'*10)
    print('\n1. Agregar Cita \n2. Buscar Cita \n3. Modificar Cita \n4. Cancelar Cita \n\n0. Salir')