from cripta_lib import *

testo_preso = False
chiave_presa = False
maiusc = False
char_spec = True
while not testo_preso:
    testo_criptato = input("dammi il messagio da decriptare:")
    if len(testo_criptato) > 0:
        testo_preso = True

print()

while not chiave_presa:
    chiave = input("dammi la chiave:")
    if len(chiave) > 0:
        chiave_presa = True

print()

testo_decriptato = ""
lchiave = len(chiave)

for i in range(len(testo_criptato)):
    char_spec = True
    lettera_criptata = ord(testo_criptato[i])
    lettera_chiave = ord(chiave[i % lchiave]) - 97
    if lettera_criptata >= 97:
        lettera_criptata -= 97
        maiusc = False
        char_spec = False
    elif lettera_criptata >= 65:
        lettera_criptata -= 65
        maiusc = True
        char_spec = False
    lettera_chiaro = decripta(
        lettera_chiave,
        lettera_criptata,
        maiusc,
        char_spec)
    testo_decriptato += lettera_chiaro

print("il testo decriptato e':", end="")
print(testo_decriptato)
