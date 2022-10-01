AÑO= 1980 
ciudadA= 3500000
ciudadB=5000000

while ciudadA<ciudadB:
    ciudadA=(ciudadA*0.07)+ciudadA
    ciudadB=(ciudadB*0.05)+ciudadB

    AÑO=AÑO+1 

print("La poblacion de la ciudad A es mayor en el año: "+ str(AÑO))

