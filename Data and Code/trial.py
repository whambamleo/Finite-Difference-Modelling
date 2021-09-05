import matplotlib.pyplot as plt
import numpy as np
#files = ["Set 1A Vin.txt", "Set 1A Vout.txt", "Set 1B Vin.txt", "Set 1B Vout.txt","Set 1C Vin.txt", "Set 1C Vout.txt","Set 2A Vin.txt", "Set 2A Vout.txt","Set 2B Vin.txt", "Set 2B Vout.txt", "Set 2C Vin.txt", "Set 2C Vout.txt", "Set 3A Vin.txt", "Set 3A Vout.txt","Set 3B Vin.txt", "Set 3B Vout.txt", "Set 3C Vin.txt", "Set 3C Vout.txt"]

Set1AVin= open("Set 1A Vin.txt", 'r')
Set1AVout= open("Set 1A Vout.txt", 'r')

VinList = Set1AVin.readlines()
VoutList = Set1AVout.readlines()
 
VinValues = []
VoutValues = []

for line in VinList:
    mvIndex = line.find("mv")
    VinValue  = float(line[mvIndex-5:mvIndex-1])
    VinValues.append(VinValue)
    
for line in VoutList:
    mvIndex = line.find("mv")
    VoutValue  = float(line[mvIndex-5:mvIndex-1])
    VoutValues.append(VoutValue)

#creating time axis with delta t = 0.01 
tValues = []
tInitial = 0.00
tValues.append(tInitial)
for i in range(3199):
    t=tInitial+0.01
    tValues.append(t)
    tInitial=t
   

x = tValues
'''
plt.plot(x,VinValues)
plt.show()

plt.plot(x,VoutValues)
plt.show()
'''

fig, (ax1, ax2) = plt.subplots(2)
fig.suptitle('Set 1A Vin and Vout')
ax1.plot(x, VinValues)
ax1.set(ylabel='Vin')
ax2.plot(x, VoutValues)
ax2.set(ylabel='Vout')
plt.xlabel("Time")
plt.show()
