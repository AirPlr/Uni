#data una stringa contenente un numero e un simbolo + o - stampare il numero corrispondente dando ai simboli + e - i rispettivi valori di +0.25 e -0.25
from termcolor import colored

def colorvoto(voto):
    if voto[0]=="1":
        try:
            if voto[1]=="0":
                return "green"
        except IndexError: pass
    if voto[0] in ["1","2","3","4","5"]:
        return "red"
    elif voto[0] in ["7","8","9"]:
        return "green"
    else :
        return "yellow"
    
def print_voto(r):
    print (colored(str(r),colore))
    
voto =input("Inserisci il voto: ")
colore=colorvoto(voto)
if len(voto)==1:
    print_voto(voto)
elif len(voto)==3:
    if voto[2]=="-":
        print_voto(9.75)
    elif voto[2]=="+":
        print (colored("Congratulazioni, 10 e Lode!","cyan"))
elif voto[1]=="-":
    r=float(voto[0])-0.25
    print_voto(r)
elif voto[1]=="+":
    r=float(voto[0])+0.25
    print_voto(r)
elif voto[1]=="0":
    print_voto(voto)
else: print("Voto non valido")


