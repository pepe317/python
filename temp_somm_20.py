import matplotlib.pyplot as plt
import datetime as dt
from collections import defaultdict

tageswert = defaultdict(list)

with open('py_train\Temp_da.txt') as f:
    for zeile in f:
        datumStr, t = zeile.split('\t')
        datum = (dt.datetime.strptime(datumStr, '%d.%m.%Y %H:%M:%S')).date()
        t = float(t)
        tageswert[datum].append(t)

tagMax = []  # leere listen erstellen
tagMin = []
tagDatum = []

for key in tageswert:
    höchst = max(tageswert[key])  # hilfsvariablen
    tiefst = min(tageswert[key])

    if abs(höchst) < 40 and abs(tiefst) < 40:
        tagMax.append(höchst)  # listen füllen
        tagMin.append(tiefst)
        tagDatum.append(key)
fig, ax = plt.subplots()
ax.plot(tagDatum, tagMax, lw=0.5, label='Hi', color='red')
ax.plot(tagDatum, tagMin, lw=0.5, label='Low', color='blue')
ax.fill_between(tagDatum, tagMax, tagMin,
                facecolor='orange', alpha=0.2, label='range')
ax.grid(linestyle='-.', linewidth='0.5', color='green')
ax.legend()
plt.yticks([-10, 0, 25, 30, 35, 40])
plt.show()
