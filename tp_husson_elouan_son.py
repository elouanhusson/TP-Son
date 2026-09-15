import numpy as np
import matplotlib.pyplot as plt
from IPython.display import Audio
from scipy.io import wavfile

#2.1

#1 La fréquence d'échantillonnage vaut 44.1 kHz, il faut donc 44100 échantillons pour un extrait d'une seconde.

#2
def position(phi,t) :
    return np.sin(2*np.pi*phi*t)

#3

f=44100 #Fréquence d'échantillonnage en Hz
la=440 #Fréquence du la en Hz
time=0.05 #Temps de l'extrait en secondes
t=np.linspace(0,0.05,int(time*f)) #échantillons 

plt.close(1)
plt.figure(1)
plt.plot(t,position(la,t)) #On trace la position en fonction du temps
plt.show()

#2.2

def sine(freq, duration, amplitude) :
    timelist=np.linspace(0,duration,int(freq*duration)) #On crée le vecteur des temps
    return amplitude*np.sin(2*np.pi*freq*timelist)

#2.3

def sine_linear(freq1,freq2,duration) :
    timelist=np.linspace(0,duration,int(freq*duration))
    freq_variable=(freq2-freq1)/duration*timelist #On crée un vecteur des fréquences qui varient linéairement avec le temps
    return amplitude*np.sin(2*np.pi*freq_variable*timelist)

#3.1 Pour modifier l'amplitude de la sinusoïde, on peut multiplier l'amplitude initiale par un coefficient qui dépend du temps.

#3.2 

def crescendo_sine(freq, duration):
    time=np.linspace(0,duration,int(freq*duration))
    