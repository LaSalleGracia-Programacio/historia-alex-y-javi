#!/usr/bin/env python3
# Historia interactiva: "La noche de Alex y Javi"
# Archivo generado automáticamente. Lenguaje: español.

import sys

def entrada(prompt):
    try:
        return input(prompt).strip().lower()
    except (EOFError, KeyboardInterrupt):
        print('\nFin. Gracias por jugar.')
        sys.exit(0)


def escena_inicio():
    print('\nLa noche ha caído sobre el pequeño pueblo. Alex y Javi se encuentran frente a un bosque misterioso.\n')
    print('1) Entrar al bosque en busca de una leyenda antigua.')
    print('2) Ir a la plaza para hablar con la gente.')
    print('3) Volver a casa y descansar.')
    return entrada('\nElige 1, 2 o 3 (o escribe salir): ')


def escena_bosque():
    print('\nEntre los árboles se siente una brisa que parece susurrar nombres. Hay un sendero que se bifurca.\n')
    print('1) Seguir el sendero iluminado por luciérnagas.')
    print('2) Tomar el sendero oscuro que baja hacia un viejo río.')
    print('3) Llamar a Javi para que vuelvan a la plaza.')
    return entrada('\nElige 1, 2 o 3 (o escribe salir, r para reiniciar): ')


def escena_plaza():
    print('\nLa plaza está animada: algunas personas cuentan historias y un anciano ofrece una pista sobre un tesoro.\n')
    print('1) Escuchar al anciano.')
    print('2) Preguntar a los niños sobre una cueva cercana.')
    print('3) Regresar al bosque con más información.')
    return entrada('\nElige 1, 2 o 3 (o escribe salir, r para reiniciar): ')


def escena_cueva():
    print('\nSiguiendo la pista, encuentran una cueva oculta tras una cascada. La entrada está cubierta de extraños símbolos.\n')
    print('1) Entrar con cuidado y encender una linterna.')
    print('2) Dibujar los símbolos y llevar la foto al anciano.')
    print('3) Volver y buscar herramientas.')
    return entrada('\nElige 1, 2 o 3 (o escribe salir, r para reiniciar): ')


def final_tesoro():
    print('\nSiguen las inscripciones y encuentran una pequeña caja con objetos antiguos: notas de amistad, una moneda antigua y una carta que habla de valentía.\n')
    print('Alex y Javi comprenden que el verdadero tesoro es la aventura compartida. Fin.')


def final_peligro():
    print('\nAl adentrarse imprudentemente, despiertan a una criatura que custodia el lugar. Logran escapar, pero aprenden a respetar los misterios. Fin.')


def final_paz():
    print('\nDeciden que algunas noches son para descansar: regresan a casa, comparten historias y planean una excursión al día siguiente. Fin.')


def juego():
    while True:
        opcion = escena_inicio()
        if opcion in ('salir', 's'):
            print('\nHasta pronto.')
            break
        if opcion == '1':
            opcion2 = escena_bosque()
            if opcion2 in ('salir', 's'):
                print('\nHasta pronto.')
                break
            if opcion2 == '1':
                print('\nEl sendero iluminado las lleva a una zona segura donde encuentran ruinas antiguas...')
                final_tesoro()
            elif opcion2 == '2':
                print('\nEl sendero oscuro revela sonidos extraños y piedras resbaladizas...')
                final_peligro()
            elif opcion2 == '3':
                print('\nRegresan a la plaza para buscar más información.')
                opcion3 = escena_plaza()
                if opcion3 == '1':
                    print('\nEl anciano sonríe y les trae un mapa gastado...')
                    opcion_cueva = escena_cueva()
                    if opcion_cueva == '1':
                        final_tesoro()
                    elif opcion_cueva == '2':
                        print('\nEl anciano agradece la copia y les cuenta la historia personal detrás del mapa.')
                        final_paz()
                    else:
                        final_peligro()
                elif opcion3 == '2':
                    print('\nLos niños indican la dirección de la cueva y juegan a guiarles.')
                    final_tesoro()
                else:
                    final_paz()
        elif opcion == '2':
            opcion3 = escena_plaza()
            if opcion3 in ('salir', 's'):
                print('\nHasta pronto.')
                break
            if opcion3 == '1':
                print('\nEl anciano narra la leyenda de una llave escondida en el bosque...')
                final_tesoro()
            elif opcion3 == '2':
                print('\nLos niños los llevan a jugar y encuentran una entrada secreta por accidente.')
                final_tesoro()
            else:
                final_paz()
        elif opcion == '3':
            final_paz()
        elif opcion == 'r':
            print('\nReiniciando la aventura...')
            continue
        else:
            print('\nOpción no válida. Intenta de nuevo.\n')
            continue

        # Después de un final, preguntar si quieren jugar otra vez
        resp = entrada('\n¿Quieres jugar otra vez? (s/n): ')
        if resp in ('s', 'si'):
            print('\nReiniciando la historia...')
            continue
        else:
            print('\nGracias por jugar. Adiós.')
            break


if __name__ == '__main__':
    print('Historia interactiva: La noche de Alex y Javi')
    print('Instrucciones: escribe el número de la opción y presiona Enter. Escribe "salir" para terminar o "r" para reiniciar.\n')
    juego()
