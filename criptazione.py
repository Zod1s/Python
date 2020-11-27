from cripta_lib import *

testo_preso = False
chiave_presa = False
maiusc = False
char_spec = True
while not testo_preso:
    testo_decriptato = input("dammi il messagio da criptare:")
    if len(testo_decriptato)>0:
        testo_preso = True

print()

while not chiave_presa:
    chiave = input("dammi la chiave:")
    if len(chiave)>0:
        chiave_presa = True

print ()

testo_criptato = ""
lchiave = len(chiave)

for i in range (len(testo_decriptato)):
    char_spec = True
    lettera_chiaro = ord(testo_decriptato[i])
    lettera_chiave = ord(chiave[i%lchiave])-97
    if lettera_chiaro >= 97:
        lettera_chiaro -= 97
        maiusc = False
        char_spec = False
    elif lettera_chiaro >= 65:
        lettera_chiaro -= 65
        maiusc = True
        char_spec = False
    lettera_criptata = cripta(lettera_chiaro,lettera_chiave,maiusc,char_spec)   
    testo_criptato += lettera_criptata
    
print ("il testo criptato e':",end="")
print (testo_criptato)
