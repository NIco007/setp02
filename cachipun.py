def ganador_cachipun():
    permiso = 0
    while permiso == 0:
        A =  [input('Nombre del primer jugador ')]
        A2 = [input('jugada ')]
        B = [input('Nombre del segundo jugador ')]
        B2 = [input('jugada ')]
        if A2[0] != 'T' and A2[0] != 'R' and A2[0] != 'P':
          print (" Accion no valida del primer jugador, vuelva a intentarlo")
        if B2[0] != 'T' and B2[0] != 'R' and B2[0] != 'P':
	        print (" Accion no valida del segundo jugador, vuelva a intentarlo")
        if (A2[0] == 'T' or A2[0] == 'R' or A2[0] == 'P') and (B2[0] == 'T' or B2[0] == 'R' or B2[0] == 'P'):
                permiso=1
    if A2[0] == 'R' and B2[0] == 'T':
        print("Gana ",A, "con ",A2[0])
    if A2[0] == 'R' and B2[0] == 'P':
        print("Gana ",'B', "con ",B2[0])
    if A2[0] == 'T' and B2[0] == 'P':
    	print("Gana ",A, "con ",A2[0])
    if A2[0] == B2[0]:
        print("Gana ", A ,'por ser el primero en escoger la jugada')



ganador_cachipun()
