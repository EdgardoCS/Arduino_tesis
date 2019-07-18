# -*- coding: utf-8 -*-
"""
Created on Thu Dec  6 11:28:12 2018

@author: Edgardo
"""
# from matplotlib import cm
import os
import time
import datetime
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.widgets import Slider, Button


elapsed_time = []
f0 = 0
delta_f = 1
values = []
trial = []
trials = []
res_values = []


meta_sub = input('sujeto: ')
    
plt.figure(figsize=[16, 5])
plt.figtext(0.40, 0.75, 'Visual Analog Scale (VAS)', size="x-large")

axcolor = '#FFFFFF'
cmap = plt.cm.get_cmap("winter")

VASax = plt.axes([0.1, 0.5, 0.8, 0.2])

sVAS = Slider(VASax, 'No Agradable', -10.0, 10.0, valinit=f0, valstep=delta_f, dragging=True, edgecolor='r',
              fill=False)
sVAS.valtext.set_visible(False)
sVAS.vline.set_visible(False)

plt.figtext(0.915, 0.6, 'Agradable', size="medium")
plt.figtext(0.1, 0.44, '-10', size="medium")
plt.figtext(0.89, 0.44, '10', size="medium")
plt.figtext(0.5, 0.44, '0', size="medium")

plt.figtext(0.098, 0.48, '|', size="medium")
plt.figtext(0.138, 0.48, '|', size="medium")
plt.figtext(0.178, 0.48, '|', size="medium")
plt.figtext(0.218, 0.48, '|', size="medium")
plt.figtext(0.258, 0.48, '|', size="medium")
plt.figtext(0.298, 0.48, '|', size="medium")
plt.figtext(0.338, 0.48, '|', size="medium")
plt.figtext(0.378, 0.48, '|', size="medium")
plt.figtext(0.418, 0.48, '|', size="medium")
plt.figtext(0.458, 0.48, '|', size="medium")
plt.figtext(0.498, 0.48, '|', size="medium")

plt.figtext(0.538, 0.48, '|', size="medium")
plt.figtext(0.578, 0.48, '|', size="medium")
plt.figtext(0.618, 0.48, '|', size="medium")
plt.figtext(0.658, 0.48, '|', size="medium")
plt.figtext(0.698, 0.48, '|', size="medium")
plt.figtext(0.738, 0.48, '|', size="medium")
plt.figtext(0.778, 0.48, '|', size="medium")
plt.figtext(0.818, 0.48, '|', size="medium")
plt.figtext(0.858, 0.48, '|', size="medium")
plt.figtext(0.898, 0.48, '|', size="medium")

reset = plt.axes([0.8, 0.3, 0.10, 0.08])
reset_button = Button(reset, 'Almacenar Valor', hovercolor='0.975')
save = plt.axes([0.8, 0.2, 0.10, 0.08])
save_button = Button(save, 'Guardar y Salir ', hovercolor='0.975')
plt.figtext(0.8, 0.75, "Trials: ", size="medium")
trial_axis = plt.figtext(0.87, 0.75, 0, size="medium")

plt.show()


def update(val):
    values
    if sVAS.val:
        values.append(sVAS.val)
    return values


def reset(event):
    global values

    if values:
        res_values.append(values[-1])
    if values == []:
        values = 0.0
        res_values.append(values)

    trials = len(res_values)
    trial_axis.set_text(trials)

    w_time = time.asctime(time.localtime(time.time()))
    temp_time = w_time.split()
    elapsed_time.append(temp_time[3])

    sVAS.reset()
    time.sleep(.09)
    values = []

    return res_values


def save(event):
    global meta_sub
    
    global_path = os.getcwd()
    out_name = global_path + '/../data/sujetos'
    
    path = out_name+ '/' + meta_sub
    
    n_time = time.asctime(time.localtime(time.time()))
    _today = str(datetime.date.today())
    today = _today.replace('-','')
    _time = n_time.split()
    save_time = today+'_'+_time[3].replace(':','')[:-2]
    
    try:  
       os.mkdir(path)
    except OSError:  
        print ("Creation of the directory %s failed" % path)
    else:  
        print ("Successfully created the directory %s " % path)
        
#    #    np.savetxt(meta_sub+'_'+meta_time+'.csv', res_values, delimiter=',', fmt='% 4d', header="Resultado VAS")
#    #    np.savetxt(meta_sub+'_'+meta_time+'.txt', res_values, delimiter=',', fmt='% 4d', header="Resultado VAS")
    np.savetxt(path+ '/'+ meta_sub + '_' + save_time + '.csv', np.c_[res_values, elapsed_time], delimiter=';', fmt='%s',
               header="Resultado VAS")
    plt.close()

sVAS.on_changed(update)
reset_button.on_clicked(reset)
save_button.on_clicked(save)
