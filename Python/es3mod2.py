voto=input("Inserisci il voto: ")
try:
    if len(voto)==3:
        num=int(voto[0]+voto[1])
        sim=voto[2]
    elif len(voto)==2:
        num=int(voto[0])
        sim=voto[1]
    elif len(voto)==1: 
        num=int(voto)
except IndexError: pass    

    
print (num)
