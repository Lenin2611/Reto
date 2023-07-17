import core

def agregarCita():
    citas = core.leerArchivo('citas')
    ciclo = True
    while(ciclo):
        cicloTry = True
        while(cicloTry):
            core.clean()
            print('-'*10, '{:^40}'.format('CAMPUS MD'), '-'*10)
            print('-'*10, '{:^40}'.format('AGREGAR CITA'), '-'*10)
            print('\n0 - Volver al Menu Principal')
            cantidadCitas = core.tryExcept(input('\nIngrese la cantidad de citas a agregar: '))
            if(type(cantidadCitas) == int):
                if(cantidadCitas >= 0):
                    cicloTry = False
                else:
                    print('\nOpcion Invalida... La cantidad de citas debe ser un numero positivo.')
                    input('\nPresione Enter para volver. . . ')
        if(cantidadCitas > 0):
            x = 0
            while(cantidadCitas > x):
                cantidadCitas -= 1
                idCita = (len(citas) + 1001)
                idCitaStr = str(idCita)
                while(idCitaStr in citas):
                    idCita -= 1
                    idCitaStr = str(idCita)
                core.clean()
                print('-'*10, '{:^40}'.format('CAMPUS MD'), '-'*10)
                print('-'*10, '{:^40}'.format('AGREGAR CITA'), '-'*10)
                print('-'*10, '{:^40}'.format(f'CITA {idCita}'), '-'*10)
                nombrePaciente = input('\nIngrese el nombre completo del paciente: ').title()
                cicloTry = True
                while(cicloTry):
                    core.clean()
                    print('-'*10, '{:^40}'.format('CAMPUS MD'), '-'*10)
                    print('-'*10, '{:^40}'.format('AGREGAR CITA'), '-'*10)
                    print('-'*10, '{:^40}'.format(f'CITA {idCita}'), '-'*10)
                    añoCita = core.tryExcept(input('\nIngrese el año de la cita (2023 o 2024): '))
                    if(type(añoCita) == int):
                        if(añoCita >= 2023) and (añoCita <= 2024):
                            cicloTry = False
                        else:
                            print('\nOpcion Invalida. . . El año ingresado no esta dentro del rango de tiempo.')
                            input('\nPresione Enter para volver. . . ')
                cicloTry = True
                while(cicloTry):
                    core.clean()
                    print('-'*10, '{:^40}'.format('CAMPUS MD'), '-'*10)
                    print('-'*10, '{:^40}'.format('AGREGAR CITA'), '-'*10)
                    print('-'*10, '{:^40}'.format(f'CITA {idCita}'), '-'*10)
                    print(f'\nIngrese el año de la cita (2023 o 2024): {añoCita}')
                    mesCita = core.tryExcept(input('\nIngrese el numero del mes de la cita: '))
                    if(type(mesCita) == int):
                        if(mesCita > 0) and (mesCita <= 12):
                            cicloTry = False
                        else:
                            print('\nOpcion Invalida. . . El mes ingresado no existe.')
                            input('\nPresione Enter para volver. . . ')
                cicloTry = True
                while(cicloTry):
                    core.clean()
                    print('-'*10, '{:^40}'.format('CAMPUS MD'), '-'*10)
                    print('-'*10, '{:^40}'.format('AGREGAR CITA'), '-'*10)
                    print('-'*10, '{:^40}'.format(f'CITA {idCita}'), '-'*10)
                    print(f'\nIngrese el año de la cita (2023 o 2024): {añoCita}')
                    print(f'\nIngrese el numero del mes de la cita: {mesCita}')
                    diaCita = core.tryExcept(input('\nIngrese el dia de la cita: '))
                    if(type(diaCita) == int):
                        if(mesCita == 1) or (mesCita == 3) or (mesCita == 5) or (mesCita == 7) or (mesCita == 8) or (mesCita == 10) or (mesCita == 12):
                            if(diaCita > 0) and (diaCita <= 31):
                                cicloTry = False
                            else:
                                print('\nOpcion Invalida. . . El dia ingresado no existe.')
                                input('\nPresione Enter para volver. . . ')
                        elif(mesCita == 4) or (mesCita == 6) or (mesCita == 9) or (mesCita == 11):
                            if(diaCita > 0) and (diaCita <= 30):
                                cicloTry = False
                            else:
                                print('\nOpcion Invalida. . . El dia ingresado no existe.')
                                input('\nPresione Enter para volver. . . ')
                        elif(mesCita == 2):
                            if(diaCita > 0) and (diaCita <= 28):
                                cicloTry = False
                            else:
                                print('\nOpcion Invalida. . . El dia ingresado no existe.')
                                input('\nPresione Enter para volver. . . ')
                        else:
                            print('\nOpcion Invalida. . . El mes ingresado no existe.')
                            input('\nPresione Enter para volver. . . ')
                fechaCompleta = f'{diaCita}-{mesCita}-{añoCita}'
                cicloTry = True
                while(cicloTry):
                    core.clean()
                    print('-'*10, '{:^40}'.format('CAMPUS MD'), '-'*10)
                    print('-'*10, '{:^40}'.format('AGREGAR CITA'), '-'*10)
                    print('-'*10, '{:^40}'.format(f'CITA {idCita}'), '-'*10)
                    print('\nEl horario de la veterinaria es de 8:00 a 20:00 y se atiende cada 30 minutos.')
                    horaCita = core.tryExcept(input('\nIngrese la hora de la cita (Horario 24h): '))
                    if(type(horaCita) == int):
                        if(horaCita >= 8) and (horaCita < 20):
                            cicloTry = False
                        else:
                            print('\nOpcion Invalida. . . La hora ingresada no esta dentro del tiempo de atencion.')
                            input('\nPresione Enter para volver. . . ')
                cicloTry = True
                while(cicloTry):
                    core.clean()
                    print('-'*10, '{:^40}'.format('CAMPUS MD'), '-'*10)
                    print('-'*10, '{:^40}'.format('AGREGAR CITA'), '-'*10)
                    print('-'*10, '{:^40}'.format(f'CITA {idCita}'), '-'*10)
                    print('\nEl horario de la veterinaria es de 8:00 a 20:00 y se atiende cada 30 minutos.')
                    print(f'\nIngrese la hora de la cita (Horario 24h): {horaCita}')
                    minutoCita = core.tryExcept(input('\nIngrese el minuto de la cita (00 o 30): '))
                    if(type(minutoCita) == int):
                        if(minutoCita == 00) or (minutoCita == 30):
                            cicloTry = False
                        else:
                            print('\nOpcion Invalida. . . El minuto ingresado debe ser 30 0 00.')
                            input('\nPresione Enter para volver. . . ')
                horaCompleta = f'{horaCita}:{minutoCita}'
                core.clean()
                print('-'*10, '{:^40}'.format('CAMPUS MD'), '-'*10)
                print('-'*10, '{:^40}'.format('AGREGAR CITA'), '-'*10)
                print('-'*10, '{:^40}'.format(f'CITA {idCita}'), '-'*10)
                motivoCita = input('\nIngrese el motivo de la consulta: ').capitalize()
                citas.update({idCita: {}})
                citas[idCita].update({'nombre': nombrePaciente,'fecha': fechaCompleta, 'hora': horaCompleta, 'motivo': motivoCita})
                core.escribirArchivo('citas', core.convertirArchivo(citas))
                core.clean()
                print('-'*10, '{:^40}'.format('CAMPUS MD'), '-'*10)
                print('-'*10, '{:^40}'.format('AGREGAR CITA'), '-'*10)
                print('-'*10, '{:^40}'.format(f'CITA {idCita}'), '-'*10)
                print(f'\nLa cita del paciente {nombrePaciente} para la fecha {fechaCompleta} y la hora {horaCompleta} fue agregada satisfactoriamente al sistema.')
                if (cantidadCitas > 0):
                    input('\nPresione Enter para agregar otra Cita. . . ')
                else:
                    input('\nPresione Enter para volver al Menu Principal. . . ')
                    ciclo = False
        elif(cantidadCitas == 0):
            ciclo = False

def buscarCita():
    citas = core.leerArchivo('citas')
    ciclo = True
    while(ciclo):
        ciclo2 = True
        while(ciclo2):
            core.clean()
            print('-'*10, '{:^40}'.format('CAMPUS MD'), '-'*10)
            print('-'*10, '{:^40}'.format('BUSCAR CITA'), '-'*10)
            print('')
            for idCita in citas:
                print(f'{idCita} - {citas[idCita]["nombre"]}')
            nombreBuscar = input('\nIngrese el nombre completo del paciente a buscar: ').title()
            for idCita in citas:
                if(nombreBuscar == citas[idCita]['nombre']):
                    ciclo2 = False
                    break
                else:
                    pass
        cicloTry = True
        while(cicloTry):
            core.clean()
            print('-'*10, '{:^40}'.format('CAMPUS MD'), '-'*10)
            print('-'*10, '{:^40}'.format('BUSCAR CITA'), '-'*10)
            print(f'\nSeguro quiere ver las citas de {nombreBuscar}? \n\n1. Si \n2. No, volver al Menu Principal')
            opcion = core.tryExcept(input('\nOpcion: '))
            if(type(opcion) == int):
                citaNumero = 0
                if(opcion == 1):
                    for idCita in citas:
                        if(opcion == 1):
                            if(nombreBuscar == citas[idCita]["nombre"]):
                                citaNumero += 1
                                core.clean()
                                print('-'*10, '{:^40}'.format('CAMPUS MD'), '-'*10)
                                print('-'*10, '{:^40}'.format('BUSCAR CITA'), '-'*10)
                                print('-'*10, '{:^40}'.format(f'CITA {citaNumero}'), '-'*10)
                                print('')
                                for dato,valor in citas[idCita].items():
                                    print(f'{dato}: {valor}')
                                input('\nPresione Enter para continuar. . . ')
                                cicloTry = False
                                ciclo = False
                elif(opcion == 2):
                    cicloTry = False
                    ciclo = False
                else:
                    print('\nOpcion Invalida. . . El numero ingresado no se encuentra en las opciones.')
                    input('\nPresione Enter para volver. . . ')

def modificarCita():
    citas = core.leerArchivo('citas')
    ciclo = True
    while(ciclo):
        ciclo2 = True
        while(ciclo2):
            core.clean()
            print('-'*10, '{:^40}'.format('CAMPUS MD'), '-'*10)
            print('-'*10, '{:^40}'.format('MODIFICAR CITA'), '-'*10)
            print('')
            for idCita in citas:
                print(f'{idCita} - {citas[idCita]["nombre"]}')
            print('\n0 - Volver al Menu Principal')
            idModificar = input('\nIngrese el id de la cita a modificar: ')
            if(idModificar in citas) or (idModificar == '0'):
                ciclo2 = False
            else:
                print('\nOpcion Invalida. . . El id ingresado no se encuentra en el sistema.')
                input('\nPresione Enter para volver. . . ')
        if(idModificar in citas):
            ciclo2 = True
            while(ciclo2):
                core.clean()
                print('-'*10, '{:^40}'.format('CAMPUS MD'), '-'*10)
                print('-'*10, '{:^40}'.format('MODIFICAR CITA'), '-'*10)
                print('-'*10, '{:^40}'.format(f'{idModificar}'), '-'*10)
                print(f'\n1. Nombre: {citas[idModificar]["nombre"]}')
                print(f'2. Fecha y Hora: {citas[idModificar]["fecha"]} / {citas[idModificar]["hora"]}')
                print(f'3. Motivo: {citas[idModificar]["motivo"]}')
                print('\n0. Volver al Menu Principal')
                datoModificar = input('\nIngrese el numero del dato a modificar: ').title()
                if(datoModificar.title() == '1') or (datoModificar.title() == '2') or (datoModificar.title() == '3'):
                    ciclo2 = False
                elif(datoModificar.title() == '0'):
                    ciclo2 = False
                    ciclo = False
                else:
                    print('\nOpcion Invalida. . . El dato ingresado no se encuentra en el sistema.')
                    input('\nPresione Enter para volver. . . ')
            if(datoModificar.title() == '1'):
                ciclo3 = True
                while(ciclo3):
                    core.clean()
                    print('-'*10, '{:^40}'.format('CAMPUS MD'), '-'*10)
                    print('-'*10, '{:^40}'.format('MODIFICAR CITA'), '-'*10)
                    print('-'*10, '{:^40}'.format(f'{idModificar}'), '-'*10)
                    print('-'*10, '{:^40}'.format('NOMBRE'), '-'*10)
                    nombrePaciente = input('\nIngrese el nombre nuevo completo del paciente: ').title()
                    if(nombrePaciente == citas[idModificar]['nombre']):
                        print('\nEl nombre ingresado es el mismo que el nombre en el sistema.')
                        input('\nPresione Enter para volver. . . ')
                    else:
                        ciclo3 = False
                citas[idModificar].update({'nombre': nombrePaciente})
                core.escribirArchivo('citas', core.convertirArchivo(citas))
                core.clean()
                print('-'*10, '{:^40}'.format('CAMPUS MD'), '-'*10)
                print('-'*10, '{:^40}'.format('MODIFICAR CITA'), '-'*10)
                print('-'*10, '{:^40}'.format(f'{idModificar}'), '-'*10)
                print('-'*10, '{:^40}'.format('NOMBRE'), '-'*10)
                print(f'\nEl nombre de la cita {idModificar} fue cambiado a {nombrePaciente} satisfactoriamente.')
                input('\nPresione Enter para volver al Menu Principal. . . ')
                ciclo = False
            elif(datoModificar.title() == '2'):
                ciclo3 = True
                while(ciclo3):
                    cicloTry = True
                    while(cicloTry):
                        core.clean()
                        print('-'*10, '{:^40}'.format('CAMPUS MD'), '-'*10)
                        print('-'*10, '{:^40}'.format('MODIFICAR CITA'), '-'*10)
                        print('-'*10, '{:^40}'.format(f'{idModificar}'), '-'*10)
                        print('-'*10, '{:^40}'.format('FECHA Y HORA'), '-'*10)
                        añoCita = core.tryExcept(input('\nIngrese el año nuevo de la cita (2023 o 2024): '))
                        if(type(añoCita) == int):
                            if(añoCita >= 2023) and (añoCita <= 2024):
                                cicloTry = False
                            else:
                                print('\nOpcion Invalida. . . El año ingresado no esta dentro del rango de tiempo.')
                                input('\nPresione Enter para volver. . . ')
                    cicloTry = True
                    while(cicloTry):
                        core.clean()
                        print('-'*10, '{:^40}'.format('CAMPUS MD'), '-'*10)
                        print('-'*10, '{:^40}'.format('MODIFICAR CITA'), '-'*10)
                        print('-'*10, '{:^40}'.format(f'{idModificar}'), '-'*10)
                        print('-'*10, '{:^40}'.format('FECHA Y HORA'), '-'*10)
                        print(f'\nIngrese el año nuevo de la cita (2023 o 2024): {añoCita}')
                        mesCita = core.tryExcept(input('\nIngrese el numero del mes nuevo de la cita: '))
                        if(type(mesCita) == int):
                            if(mesCita > 0) and (mesCita <= 12):
                                cicloTry = False
                            else:
                                print('\nOpcion Invalida. . . El mes ingresado no existe.')
                                input('\nPresione Enter para volver. . . ')
                    cicloTry = True
                    while(cicloTry):
                        core.clean()
                        print('-'*10, '{:^40}'.format('CAMPUS MD'), '-'*10)
                        print('-'*10, '{:^40}'.format('MODIFICAR CITA'), '-'*10)
                        print('-'*10, '{:^40}'.format(f'{idModificar}'), '-'*10)
                        print('-'*10, '{:^40}'.format('FECHA Y HORA'), '-'*10)
                        print(f'\nIngrese el año nuevo de la cita (2023 o 2024): {añoCita}')
                        print(f'\nIngrese el numero del mes nuevo de la cita: {mesCita}')
                        diaCita = core.tryExcept(input('\nIngrese el dia nuevo de la cita: '))
                        if(type(diaCita) == int):
                            if(mesCita == 1) or (mesCita == 3) or (mesCita == 5) or (mesCita == 7) or (mesCita == 8) or (mesCita == 10) or (mesCita == 12):
                                if(diaCita > 0) and (diaCita <= 31):
                                    cicloTry = False
                                else:
                                    print('\nOpcion Invalida. . . El dia ingresado no existe.')
                                    input('\nPresione Enter para volver. . . ')
                            elif(mesCita == 4) or (mesCita == 6) or (mesCita == 9) or (mesCita == 11):
                                if(diaCita > 0) and (diaCita <= 30):
                                    cicloTry = False
                                else:
                                    print('\nOpcion Invalida. . . El dia ingresado no existe.')
                                    input('\nPresione Enter para volver. . . ')
                            elif(mesCita == 2):
                                if(diaCita > 0) and (diaCita <= 28):
                                    cicloTry = False
                                else:
                                    print('\nOpcion Invalida. . . El dia ingresado no existe.')
                                    input('\nPresione Enter para volver. . . ')
                            else:
                                print('\nOpcion Invalida. . . El mes ingresado no existe.')
                                input('\nPresione Enter para volver. . . ')
                    fechaCompleta = f'{diaCita}-{mesCita}-{añoCita}'
                    cicloTry = True
                    while(cicloTry):
                        core.clean()
                        print('-'*10, '{:^40}'.format('CAMPUS MD'), '-'*10)
                        print('-'*10, '{:^40}'.format('MODIFICAR CITA'), '-'*10)
                        print('-'*10, '{:^40}'.format(f'{idModificar}'), '-'*10)
                        print('-'*10, '{:^40}'.format('FECHA Y HORA'), '-'*10)
                        print('\nEl horario de la veterinaria es de 8:00 a 20:00 y se atiende cada 30 minutos.')
                        horaCita = core.tryExcept(input('\nIngrese la hora nueva de la cita (Horario 24h): '))
                        if(type(horaCita) == int):
                            if(horaCita >= 8) and (horaCita < 20):
                                cicloTry = False
                            else:
                                print('\nOpcion Invalida. . . La hora ingresada no esta dentro del tiempo de atencion.')
                                input('\nPresione Enter para volver. . . ')
                    cicloTry = True
                    while(cicloTry):
                        core.clean()
                        print('-'*10, '{:^40}'.format('CAMPUS MD'), '-'*10)
                        print('-'*10, '{:^40}'.format('MODIFICAR CITA'), '-'*10)
                        print('-'*10, '{:^40}'.format(f'{idModificar}'), '-'*10)
                        print('-'*10, '{:^40}'.format('FECHA Y HORA'), '-'*10)
                        print('\nEl horario de la veterinaria es de 8:00 a 20:00 y se atiende cada 30 minutos.')
                        print(f'\nIngrese la hora nueva de la cita (Horario 24h): {horaCita}')
                        minutoCita = core.tryExcept(input('\nIngrese el minuto nuevo de la cita (00 o 30): '))
                        if(type(minutoCita) == int):
                            if(minutoCita == 00) or (minutoCita == 30):
                                cicloTry = False
                            else:
                                print('\nOpcion Invalida. . . El minuto ingresado debe ser 30 0 00.')
                                input('\nPresione Enter para volver. . . ')
                    horaCompleta = f'{horaCita}:{minutoCita}'
                    if(fechaCompleta == citas[idModificar]['fecha']) and (horaCompleta == citas[idModificar]['hora']):
                        core.clean()
                        print('-'*10, '{:^40}'.format('CAMPUS MD'), '-'*10)
                        print('-'*10, '{:^40}'.format('MODIFICAR CITA'), '-'*10)
                        print('-'*10, '{:^40}'.format(f'{idModificar}'), '-'*10)
                        print('-'*10, '{:^40}'.format('FECHA Y HORA'), '-'*10)
                        print('\nLa fecha y la hora ingresadas son las mismas que la fecha y la hora en el sistema.')
                        input('\nPresione Enter para volver. . . ')
                    else:
                        ciclo3 = False
                citas[idModificar].update({'hora': horaCompleta})
                citas[idModificar].update({'fecha': fechaCompleta})
                core.escribirArchivo('citas', core.convertirArchivo(citas))
                core.clean()
                print('-'*10, '{:^40}'.format('CAMPUS MD'), '-'*10)
                print('-'*10, '{:^40}'.format('MODIFICAR CITA'), '-'*10)
                print('-'*10, '{:^40}'.format(f'{idModificar}'), '-'*10)
                print('-'*10, '{:^40}'.format('FECHA Y HORA'), '-'*10)
                print(f'\nLa fecha y la hora de la cita {idModificar} fueron cambiadas a {fechaCompleta} / {horaCompleta} satisfactoriamente.')
                input('\nPresione Enter para volver al Menu Principal. . . ')
                ciclo = False
            if(datoModificar.title() == '3'):
                ciclo3 = True
                while(ciclo3):
                    core.clean()
                    print('-'*10, '{:^40}'.format('CAMPUS MD'), '-'*10)
                    print('-'*10, '{:^40}'.format('MODIFICAR CITA'), '-'*10)
                    print('-'*10, '{:^40}'.format(f'{idModificar}'), '-'*10)
                    print('-'*10, '{:^40}'.format('MOTIVO'), '-'*10)
                    motivoCita = input('\nIngrese el motivo nuevo de la consulta: ').capitalize()
                    if(motivoCita == citas[idModificar]['motivo']):
                        print('\nEl motivo ingresado es el mismo que el anterior.')
                        input('\nPresione Enter para volver. . . ')
                    else:
                        ciclo3 = False
                citas[idModificar].update({'motivo': motivoCita})
                core.escribirArchivo('citas', core.convertirArchivo(citas))
                core.clean()
                print('-'*10, '{:^40}'.format('CAMPUS MD'), '-'*10)
                print('-'*10, '{:^40}'.format('MODIFICAR CITA'), '-'*10)
                print('-'*10, '{:^40}'.format(f'{idModificar}'), '-'*10)
                print('-'*10, '{:^40}'.format('MOTIVO'), '-'*10)
                print(f'\nEl motivo de la cita {idModificar} fue cambiado a "{motivoCita}" satisfactoriamente.')
                input('\nPresione Enter para volver al Menu Principal. . . ')
                ciclo = False
        elif(idModificar == '0'):
            ciclo = False

def cancelarCita():
    citas = core.leerArchivo('citas')
    ciclo = True
    while(ciclo):
        ciclo2 = True
        while(ciclo2):
            core.clean()
            print('-'*10, '{:^40}'.format('CAMPUS MD'), '-'*10)
            print('-'*10, '{:^40}'.format('CANCELAR CITA'), '-'*10)
            print('')
            for idCita in citas:
                print(f'{idCita} - {citas[idCita]["nombre"]}')
            print('\n0 - Volver al Menu Principal')
            idCancelar = input('\nIngrese el id de la cita a cancelar: ')
            if(idCancelar in citas) or (idCancelar == '0'):
                    ciclo2 = False
            else:
                print('\nOpcion Invalida. . . El id ingresado no se encuentra en el sistema.')
                input('\nPresione Enter para volver. . . ')
        if(idCancelar in citas):
            cicloTry = True
            while(cicloTry):
                core.clean()
                print('-'*10, '{:^40}'.format('CAMPUS MD'), '-'*10)
                print('-'*10, '{:^40}'.format('CANCELAR CITA'), '-'*10)
                print('-'*10, '{:^40}'.format(f'{idCancelar}'), '-'*10)
                print(f'\nSeguro quiere cancelar la cita {idCancelar}? \n\n1. Si \n2. No, Volver al Menu Principal')
                opcionSiNo = core.tryExcept(input('\nOpcion: '))
                if(type(opcionSiNo) == int):
                    if(opcionSiNo >= 1) and (opcionSiNo <= 2):
                        cicloTry = False
                    else:
                        print('\nOpcion Invalida. . . La opcion ingresada no se encuentra en las opciones.')
                        input('\nPresione Enter para volver. . . ')
            if(opcionSiNo == 1):
                citas.pop(idCancelar)
                core.escribirArchivo('citas', core.convertirArchivo(citas))
                core.clean()
                print('-'*10, '{:^40}'.format('CAMPUS MD'), '-'*10)
                print('-'*10, '{:^40}'.format('CANCELAR CITA'), '-'*10)
                print('-'*10, '{:^40}'.format(f'{idCancelar}'), '-'*10)
                print(f'\nLa cita {idCancelar} fue cancelada satisfactoriamente.')
                input('\nPresione Enter para volver al Menu Principal. . . ')
                ciclo = False
            elif(opcionSiNo == 2):
                ciclo = False
        elif(idCancelar == '0'):
            ciclo = False