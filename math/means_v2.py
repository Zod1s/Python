import matplotlib.pyplot as plt

plt.style.use("bmh")

path = "C:/Lorenzo/Sviluppo/Python/math/misurazione01.txt"

with open(path) as f:
    text = ""

    for line in f:
        text += str(line)

    text = text.splitlines()

    values = []

    for element in text:
        values.append(element.split("\t"))

    sensor0, sensor1, sensor2, sensor3, sensor4, sensor5 = [], [], [], [], [], []

    for element in values:
        sensor0.append(int(element[0][3:]))
        sensor1.append(int(element[1][3:]))
        sensor2.append(int(element[2][3:]))
        sensor3.append(int(element[3][3:]))
        sensor4.append(int(element[4][3:]))
        sensor5.append(int(element[5][3:]))

time_step = 3
time = [time_step * _ for _ in range(len(sensor0))]

fig, ((gr0, gr1), (gr2, gr3), (gr4, gr5)) = plt.subplots(nrows=3, ncols=2, sharex=True, constrained_layout=True)
fig.suptitle("sensori")

gr0.set(ylabel="valore(s0)")
gr0.plot(time, sensor0, 'b')

gr1.set(ylabel="valore(s1)")
gr1.plot(time, sensor1, 'r')

gr2.set(ylabel="valore(s2)")
gr2.plot(time, sensor2, 'g')

gr3.set(ylabel="valore(s3)")
gr3.plot(time, sensor3, 'c')

gr4.set(ylabel="valore(s4)")
gr4.plot(time, sensor4, 'm')

gr5.set(ylabel="valore(s5)")
gr5.plot(time, sensor5, 'y')

plt.show()