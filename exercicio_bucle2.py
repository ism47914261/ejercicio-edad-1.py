# coding=utf8

# Inicializaciones
salir = "N"
numero=1
numero1=(input("Introduzca un numero:"))
if numero1 > 1:
    while ( salir=="N" ):
        # Hago cosas
        print numero

        # Incremento
        numero= numero + 1
    
        # Activo indicador de salida si toca
        if ( numero > numero1 ): # Condición de salida
            salir = "S"
