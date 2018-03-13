# coding=utf8

# Inicializaciones
salir = "N"
numero=0
numero1=(input("Introduzca un numero:"))

while ( salir=="N" ):
    if numero1 % 2==0:
			
        # Hago cosas
        print numero

        # Incremento
        numero= numero + 2
                    
        
        
        
        # Activo indicador de salida si toca
        if ( numero > numero1 ): # Condición de salida
            salir = "S"

"""Que cuente del número 1 hasta el límite que yo le diga. Sólo los pares."""
