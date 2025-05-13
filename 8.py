from matplotlib import pyplot as plt
import numpy as np
from textwrap import wrap
import matplotlib.ticker as ticker

with open('C:/Users/user/Downloads/settings.txt') as file:
    settings = [float(i) for i in file.read().split('\n') if i] 

data = np.loadtxt('C:/Users/user/Downloads/data.txt', dtype=int) * settings[1]
data_t = np.array([i*settings[0] for i in range(data.size)])


maxv = np.max(data)
minv = np.min(data)
start_x = np.where(data >= minv)[0][0]
end_x = np.where(data == maxv)[0][0]
end2_x = np.where(data <= minv + 0.1*(maxv-minv))[0][-1]  

ctime = data_t[end_x] - data_t[start_x]
dtime = data_t[end2_x] - data_t[end_x]

f, ax = plt.subplots(figsize=(12, 8), dpi=300)  


ax.axis([data_t.min(), data_t.max()+1, data.min()-0.2, data.max()+0.2])
ax.xaxis.set_major_locator(ticker.MultipleLocator(1))
ax.xaxis.set_minor_locator(ticker.MultipleLocator(0.2))
ax.yaxis.set_major_locator(ticker.MultipleLocator(0.5))
ax.yaxis.set_minor_locator(ticker.MultipleLocator(0.1))


ax.set_title('Процесс заряда и разряда конденсатора в RC-цепочке', 
             loc='center', pad=20, fontsize=14)
ax.set_ylabel("Напряжение, В", fontsize=12)
ax.set_xlabel("Время, с", fontsize=12)

time_info = (f"Время заряда = {ctime:.2f} с\n"
             f"Время разряда = {dtime:.2f} с")

props = dict(boxstyle='round', facecolor='white', alpha=0.8, 
             edgecolor='gray', pad=0.5, linewidth=1)
ax.text(0.95, 0.85, time_info, transform=ax.transAxes,
        fontsize=11, verticalalignment='top', horizontalalignment='right',
        bbox=props)

ax.grid(which='major', color='gray', linestyle='-', linewidth=0.7)
ax.grid(which='minor', color='lightgray', linestyle=':', linewidth=0.5)
ax.minorticks_on()

ax.plot(data_t, data, c='black', linewidth=1.5, label='V(t)')
ax.legend(shadow=False, loc='upper right', fontsize=11, framealpha=1)

plt.tight_layout()
plt.show()
f.savefig('C:/graph.png', dpi=300, bbox_inches='tight')
f.savefig('C:/graph.svg', bbox_inches='tight')
print('done')