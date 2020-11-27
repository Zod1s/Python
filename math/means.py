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
samples  = len(values)
time = [time_step * _ for _ in range(samples)] # genera una lista da 0 a time_step * samples 
                                               # con incremento di time_step ogni volta

fig, (gr1, gr2) = plt.subplots(nrows=2, ncols=1, constrained_layout=True)

fig.suptitle("grafici")

sensors_values = [0 for _ in range(VAL_LEN)] # genera una lista di VAL_LEN zeri
sensor_mean = []
index = 0

for item in values:
    sensors_values[index] = item

    mean = 0 # media dei valori salvati
    for value in sensors_values:
        mean += value
    
    mean /= len(sensors_values)

    sensor_mean.append(mean) # fa la media degli ultimi VAL_LEN valori salvati

    index = (index + 1) % VAL_LEN

gr1.set(xlabel="tempo(ms)", ylabel="valore misurato")
gr1.plot(time, values, 'b')

gr2.set(xlabel="tempo(ms)", ylabel="media")
gr2.plot(time, sensor_mean, 'g')

plt.show()