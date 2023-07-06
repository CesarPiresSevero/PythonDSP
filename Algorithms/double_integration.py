##########################################################################
#                                                                        #
#                         Double Integration                             #
#                                                                        #
##########################################################################

'''
    Demonstration script of double integration.
    Commonly done with electronic circuits, a square wave is integrated
    into a triangular wave. This wave is done integrated again into a 
    sinusoidal form wave.

        Square_wave = a  {1 for alpha<=pi and -1 for alpha>pi}
        Triangular_wave = a*x + b
        Sinusoidal_wave = (a*x**2)/2 + b*x + c

    Being x the sample number and a,b and c the coeficients.
'''

############################### Imports ##################################
import matplotlib.pyplot as plt
import numpy as np

############################## Execution #################################
# Original wave with digital frequency 1/5
square_wave=[-1.0,-1.0,-1.0,-1.0,-1.0,1.0,1.0,1.0,1.0,1.0,
             -1.0,-1.0,-1.0,-1.0,-1.0,1.0,1.0,1.0,1.0,1.0,
             -1.0,-1.0,-1.0,-1.0,-1.0,1.0,1.0,1.0,1.0,1.0]

# Integration with numpy cumsum
triangle_wave=np.cumsum(square_wave)
sine_wave=np.cumsum(triangle_wave)

# Integration locally
triangle_wave = []
for i,val in enumerate(square_wave):
    if(i==0): triangle_wave.append(val)
    else: triangle_wave.append(triangle_wave[-1]+val)
sine_wave = []
for i,val in enumerate(triangle_wave):
    if(i==0): sine_wave.append(val)
    else: sine_wave.append(sine_wave[-1]+val)

# Plotting
plt.figure()
plt.subplot(121)
plt.title('First integration')
plt.plot(square_wave,"-x")
plt.plot(triangle_wave,"-x")
plt.grid()
plt.subplot(122)
plt.title('Second integration')
plt.plot(square_wave,"-x")
plt.plot(triangle_wave,"-x")
plt.plot(sine_wave,"-x")
plt.grid()
plt.show()
