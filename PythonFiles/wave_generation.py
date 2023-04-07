##########################################################################
#                                                                        #
#                          Wave Generation                               #
#                                                                        #
##########################################################################

'''
    Wave generation for synthesizer purposes with:
    - Sine wave
    - Triangular wave
    - Sawtooth wave (normal and reversed)
    - Square wave (variable duty-cycle)
    Variable oscilators with amplitude, frequency and phase control.
    Signals are generated by hand (not using Scipy)
    The frequency range is from A0 (27.5Hz) to B8 (4186.01Hz) to cover 
    the full standard piano range
    Inputs:
    - size: signal output lenght
    - f: sampling frequency
    - fs: signal frequency
    - amp: signal amplitude (0 <= amp <= 1)
    - phase: singal phase  (-2pi < phase < 2pi)
    - reverse: change sawtooth ascending or descending
    - duty: duty cycle setting for square wave (0 <= duty <=1)
'''

############################### Imports ##################################
import matplotlib.pyplot as plt
import numpy as np


############################## Functions #################################
def get_sine_wave(size=16,f=440.0,fs=16000.0,amp=0.5,phase=0.0):
    signal=[]
    # Digital frequency
    df=2*np.pi*(f/fs)
    for i in range(size):
        signal.append(amp*np.sin((df*i)+phase))
    return signal


def get_triangular_wave(size=16,f=440.0,fs=16000.0,amp=0.5,phase=0.0):
    signal=[]
    # Digital frequency
    df=2*np.pi*(f/fs)
    for i in range(size):
        # Calculate angle
        alfa=((df*i)+phase-np.pi/2)%(2*np.pi)
        if(alfa<np.pi):
            signal.append(((1-(2*alfa/np.pi)))*amp)
        else:
            signal.append(((2*alfa/np.pi)-3)*amp)
    return signal

def get_sawtooth_wave(size=16,f=440.0,fs=16000.0,amp=0.5,phase=0.0,reverse=False):
    signal=[]
    # Digital frequency
    df=2*np.pi*(f/fs)
    for i in range(size):
        # Calculate angle
        alfa=((df*i)+phase)%(2*np.pi)
        if(reverse):
            signal.append(amp*(1-(alfa/np.pi)))
        else:
            signal.append(amp*((alfa/np.pi)-1))
    return signal

def get_square_wave(size=16,f=440.0,fs=16000.0,amp=0.5,phase=0.0,duty=0.5):
    signal=[]
    # Digital frequency
    df=2*np.pi*(f/fs)
    for i in range(size):
        # Calculate angle
        alfa=((df*i)+phase)%(2*np.pi)
        if(alfa<2*np.pi*duty):
            signal.append(amp)
        else:
            signal.append(-amp)
    return signal

############################## Execution #################################
if __name__ == '__main__':
    # Wave settings
    fs=44100
    f=4186.01 # Max freq
    f=27.5 # Min freq
    f=440 # Standard freq
    size=int(fs/f)*6
    amp=1

    # Waveforms instances
    sine_wave=get_sine_wave(size,f,fs,amp)
    triang_wave=get_triangular_wave(size,f,fs,amp)
    saw_wave=get_sawtooth_wave(size,f,fs,amp)
    square_wave=get_square_wave(size,f,fs,amp)

    # Plotting wave forms
    plt.figure()
    plt.plot(sine_wave,"-x")
    plt.plot(triang_wave,"-x")
    plt.plot(saw_wave,"-x")
    plt.plot(square_wave,"-x")

    # Plotting harmonic info
    half=int(size/2)
    freq=np.linspace(0,fs/2,half+1)
    plt.figure()
    plt.plot(freq,abs(np.fft.fft(sine_wave*np.hanning(size))[0:half+1])/half)
    plt.plot(freq,abs(np.fft.fft(triang_wave*np.hanning(size))[0:half+1])/half)
    plt.plot(freq,abs(np.fft.fft(saw_wave*np.hanning(size))[0:half+1])/half)
    plt.plot(freq,abs(np.fft.fft(square_wave*np.hanning(size))[0:half+1])/half)
    plt.show()
