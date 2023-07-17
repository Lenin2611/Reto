import core
import citas

if __name__ == '__main__':
    ciclo = True
    while(ciclo):
        cicloTry = True
        while(cicloTry):
            core.menuPrincipal()
            opcionMenu = core.tryExcept(input('\nIngrese la opcion: '))
            if (type(opcionMenu) == int):
                if (opcionMenu >= 0) and (opcionMenu <= 4):
                    cicloTry = False
                else:
                    print('\nOpcion no valida. . . El numero ingresado no se encuentra en las opciones.')
                    input('\nPresione Enter para volver. . . ')
        if (opcionMenu == 1):
            citas.agregarCita()
        elif (opcionMenu == 2):
            citas.buscarCita()
        elif (opcionMenu == 3):
            citas.modificarCita()
        elif (opcionMenu == 4):
            citas.cancelarCita()
        elif (opcionMenu == 0):
            core.clean()
            print('¡¡¡¡¡¡¡¡¡¡¡¡¡¡¡¡¡¡¡¡¡¡¡¡¡¡¡¡')
            print('¡¡¡¡¡ HASTA LA PROXIMA !!!!!')
            print('!!!!!!!!!!!!!!!!!!!!!!!!!!!!')
            ciclo = False