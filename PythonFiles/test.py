# Testing synth data
import numpy as np
import matplotlib.pyplot as plt


samples=2000
a0=0.17
a1=0.32
b1=0.0055
c1=np.pi/2
x=np.arange(samples)

y=a0+a1*np.sin(2*np.pi*x*b1+c1)
print(type(y))

mu,sigma=0.0,0.93
noise=np.random.normal(mu,sigma,samples)

out=y+noise


a,b=np.array([1.0, -1.734725768809275, 0.7660066009432638]),np.array([0.007820208033497193, 0.015640416066994386, 0.007820208033497193])

iir=[]
for i in range(samples):
	if(i>=2):
		iir.append(-a[1]*iir[i-1]-a[2]*iir[i-2]+b[0]*out[i]+b[1]*out[i-1]+b[2]*out[i-2])
	else:
		iir.append(out[i])


# plt.plot(iir)
# plt.plot(abs(np.fft.fft(out))[0:100])
plt.plot(abs(np.fft.fft(iir))[0:1000])
plt.show()