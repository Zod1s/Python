import matplotlib.pyplot as plt

plt.style.use("bmh") #setta lo stile dei grafici

VAL_LEN = 3 # numero dei valori su cui fa la media

path = "" # path del file .txt dove sono salvati i valori
text = "" # stringa per contenere il file
values = [] # array per i valori letti

with open(path) as f:
    for line in f:
        text += str(line)    # prende i valori dal file e li mette in un'unica variabile

    text = text.splitlines() # elimina tutti i \n presenti nella stringa. text passa da 
                             # essere str a essere list

    for element in text:
        values.append(int(element.split(", ")[1])) # prende il valore letto, scartando il valore 
                                                   # del tempo in cui è stato letto

time_step = 3
time = [time_step * _ for _ in range(len(values))] # genera una lista da 0 a time_step * samples 
                                               # con incremento di time_step ogni volta

plt.plot(time, values, 'b')

plt.show()