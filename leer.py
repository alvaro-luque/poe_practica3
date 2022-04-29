import numpy as np
import pandas as pd
import matplotlib.pyplot as plt


#para que salga en latex
plt.rcParams.update({
    "text.usetex": True,
    "font.family": "serif",
    "font.serif": ["Palatino"],
})

datos=pd.read_csv('acoplador.data', header=None)
#la lectura del tornillo siempre estará en la columna [0]

x=np.array(datos[0])
y1=np.array(datos[1])
y2=np.array(datos[2])

errx=np.array(datos[3])
erry1=np.array(datos[4])
erry2=np.array(datos[5])

fig, ax=plt.subplots()

ax.axis([max(x)+0.2,min(x)-0.2,min(y2)-2,30])
ax.set_xlabel('Lectura del tornillo', fontsize=15)
ax.set_ylabel('Amplificación (dBm)', fontsize=15)

plt.scatter(x,y1, color='b', label='Salida sin atenuación')
plt.errorbar(x,y1, yerr=erry1, xerr=errx, color='b', fmt='none')
plt.scatter(x,y2, color='r', label='Salida atenuada 20 dBm')
plt.errorbar(x,y2, yerr=erry2, xerr=errx, color='r', fmt='none')
plt.xticks(ticks=[9,8.5,8,7.5,7,6.5,6,5.5,5,4.5])
plt.plot(x,y1-y2, color='g', label='Diferencia de amplificación')

plt.title('\\bf{Acoplador}', fontsize=15)
plt.legend()

plt.savefig("acoplador.pdf", dpi=96)