#dato un numero controllare che la cifra delle unità sia sia 7

a=int(input("Inserisci un numero: "))
risultato=a%10
if risultato==7:
    print("la cifra delle unità del numero è 7")
else:
    print("la cifra delle unità del numero non è 7 ma è", risultato)