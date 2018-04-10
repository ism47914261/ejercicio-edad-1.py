# coding=utf8

# Inicializaciones
salir = "N"
numero_dias=(input("Introduzca un numero:"))
anyo= 0
mes= 0
semana= 0
resto= 0

while ( salir=="N" ):
    # Hago cosas
    if (numero_dias >= 365):
        resto= numero_dias-365
        anyo= anyo + 1
        
    elif (numero_dias >= 30):
        resto= numero_dias-30
        mes= mes + 1
    
    elif (numero_dias >= 7):
        resto= numero_dias-7
        semana= semana + 1
        
    elif (numero_dias > 1):
        numero_dias= numero_dias - 1
        
        
    elif (numero_dias == 0):
        print "No hay ningun dia"
        
    # Incremento
    
    
    
    
    # Activo indicador de salida si toca
    if ( numero_dias == 0 ): # Condición de salida
        salir = "S"
print "El numero de dias son:" , anyo , mes , semana , numero_dias


