a=int(input("Inserisci costo lordo: "))
iva=int(input("Inserisci Iva: "))
iva=(iva/100)+1
cn=a/iva
print(cn)
