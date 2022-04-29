import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

#para que salga en latex
plt.rcParams.update({
    "text.usetex": True,
    "font.family": "serif",
    "font.serif": ["Palatino"],
})

x=np.array(pd.read_csv('calibracion.data', header=None)[0])
calib=np.array(pd.read_csv('calibracion.data', header=None)[1])
aisl=np.array(pd.read_csv('aislador.data', header=None)[1])
acop=np.array(pd.read_csv('acoplador.data', header=None)[1])
circ1=np.array(pd.read_csv('circ1.data', header=None)[1])
circ2=np.array(pd.read_csv('circ2.data', header=None)[1])
circ3=np.array(pd.read_csv('circ3.data', header=None)[1])

fig, ax=plt.subplots()
ax.axis([max(x)+0.2,min(x)-0.2,-30,10])
ax.set_xlabel('Lectura del tornillo', fontsize=15)
ax.set_ylabel('Amplificación (dBm)', fontsize=15)
plt.plot(x,calib, color='b', label='Perfil de medida')
plt.plot(x,aisl, color='r', label='Aislador')
plt.plot(x,acop, color='g', label='Acoplador')
plt.plot(x,circ1, color='orange', label='Circulador, posición 1')
plt.plot(x,circ2, color='magenta', label='Circulador, posición 2')
plt.plot(x,circ3, color='slategray', label='Circulador, posición 3')
plt.xticks(ticks=[9,8.5,8,7.5,7,6.5,6,5.5,5,4.5])
plt.title('\\bf{Comparativa de perfiles}', fontsize=15)
plt.legend()

plt.savefig("comparativa.pdf", dpi=96)