from random import *
def craps(derrota,victoria):
    jugar = True 
    tiro = (randint(1,6),randint(1,6))
    print("tiro : "+ str(tiro))   
    if tiro in derrota:  
        print("Pierdes")
    else:
        if tiro in victoria:  
            print("Ganas")
        else:                
            print("Punto")           
            puntaje = tiro[0] + tiro[1]            
            while jugar:                   
                lpunto = (randint(1,6),randint(1,6))              
                print("tiro: "+ str(lpunto))  
                if puntaje == 7:    
                    print("Pierdes")
                    jugar = False
                else:
                    if lpunto == tiro:   
                        print("Ganas")
                        jugar = False


dado = []
for i in range(13):  		
    dado.append(set())
for j in range(6):			
	for k in range(6):
		dado[j+k+2].add((j+1,k+1))

derrota = dado[2]|dado[3]|dado[12]
victoria = dado[7]|dado[11]
punto = dado[4]|dado[5]|dado[6]|dado[8]|dado[9]|dado[10]

	

craps(derrota,victoria)
