# coding=utf8

A = (input("Intorduzca un numero cualquiera:"))
B = (input("Intorduzca un numero diferente al anterior:"))
C = (input("Intorduzca un numero diferente a los anteriorores:"))




if A<B and A<C:
    print "A Es el valor mas pequeño"
else: 
    if B<A and B<C:
	print "B Es el valor mas pequeño"
    else:
	print "C Es el valor mas pequeño"


if A==B and A==C and B==C:
    print "Hay 3 valores iguales"
else:
    if (B==C and A==C) or (A==B and B==C) or (B==C and A==C):
        print "Hay 2 valores iguales"
				    
    else:
	if B==C:
            print "Hay 1 valor igual"
        else:
            if A==C:
               print "Hay 1 valor igual"
						    
	    else:
               if A==B:
                   print "Hay 1 valor igual"
               else:
                   if A>B and A>C:
                       print  "A Es el valor mas grande"
	
                   else:
                       if B>A and B>C:
     	                   print "B Es el valor mas grande"
		
                       else:
                           if C>A and C>B:
         	               print "C Es el valor mas grande"  
	



	            
