#dato un voto da 1 a 30 assegnare la lettera corrispondente
voto=int(input("Inserisci il voto: "))
if voto==30:
    print("Il voto è A")
    
elif voto>=27 and voto<=29:
    print("Il voto è B")

elif voto>=24 and voto<=26:
    print("Il voto è C")
    
elif voto>=21 and voto<=23:
    print("Il voto è D")
    
elif voto>=18 and voto<=20:
    print("Il voto è E")
    
elif voto<=17:
    print("Il voto è F")