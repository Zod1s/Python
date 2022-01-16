import matplotlib.pyplot as plt

plt.style.use("bmh")  # setta lo stile dei grafici

VAL_LEN = 3  # numero dei valori su cui fa la media

path = ""  # path del file .txt dove sono salvati i valori
text = ""  # stringa per contenere il file
values = []  # array per i valori letti

with open(path) as f:
    for line in f:
        # prende i valori dal file e li mette in un'unica variabile
        text += str(line)

    text = text.splitlines()  # elimina tutti i \n presenti nella stringa. text passa da
    # essere str a essere list

    for element in text:
        # prende il valore letto, scartando il valore
        values.append(int(element.split(", ")[1]))
        # del tempo in cui è stato letto

time_step = 3
# genera una lista da 0 a time_step * samples
time = [time_step * _ for _ in range(len(values))]
# con incremento di time_step ogni volta

plt.plot(time, values, 'b')

plt.show()
