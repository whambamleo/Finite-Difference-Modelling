import matplotlib.pyplot as plt
import numpy as np
from scipy.stats import chi2

def main():
    
    WAVE_TYPES = ["triangular", "sine", "square"]
    FREQUENCY_REGIONS = ["below cut-off", "near cut-off", "above cut-off"]
    
    R = 11.97E3 #resistance in ohms
    C = 10.00E-9 #capacitance in farads
    cutOff = 1/(2*np.pi*R*C)
    deltaT = 0.01 #milliseconds
    RCoverdeltaT = ((R*C)/deltaT)
    
    print("Resistance: "+ str(R) + " ohms")
    print("Capacitance: "+ str(C) + " farads")
    print("Cut-off Frequency: "+ str(cutOff) + " Hz")
    print("delta T: "+ str(deltaT) + " milliseonds")
    print("RCoverdeltaT: "+ str(RCoverdeltaT) )
    print()
    
    #data files
    set1A = ["Set 1A Vin.txt", "Set 1A Vout.txt"]
    set1B = ["Set 1B Vin.txt", "Set 1B Vout.txt"]
    set1C = ["Set 1C Vin.txt", "Set 1C Vout.txt"]
    set2A = ["Set 2A Vin.txt", "Set 2A Vout.txt"]
    set2B = ["Set 2B Vin.txt", "Set 2B Vout.txt"]
    set2C = ["Set 2C Vin.txt", "Set 2C Vout.txt"]
    set3A = ["Set 3A Vin.txt", "Set 3A Vout.txt"]
    set3B = ["Set 3B Vin.txt", "Set 3B Vout.txt"]
    set3C = ["Set 3C Vin.txt", "Set 3C Vout.txt"]
             
    
    print("==> Low Pass Filter Data Visualization and Finite Difference Modeling <==")
    print()
    print("--- Model Parameters ---")
    
    #INPUT
    
    #wave type input
    waveType=input("Enter wave type (sine, square, triangular):")
    while waveType not in WAVE_TYPES:
        print("Try again :( , case-sensitive!")
        waveType = input("Enter wave type (sine, square, triangular):")
        
    # frequency region input
    frequencyRegion = input("Enter frequency region (below cut-off, near cut-off, above cut-off):")
    while frequencyRegion not in FREQUENCY_REGIONS:
        print("Try again :( , case-sensitive!")
        frequencyRegion = input("Enter frequency region (below cut-off, near cut-off, above cut-off):")
        
    # loading appropriate data file
    fileSet = []
    if waveType == "sine":
        if frequencyRegion == "below cut-off":
            fileSet = set1A.copy()
        if frequencyRegion == "near cut-off":
            fileSet = set1B.copy()
        if frequencyRegion == "above cut-off":
            fileSet = set1C.copy()
            
    if waveType == "triangular":
        if frequencyRegion == "below cut-off":
            fileSet = set2A.copy()
        if frequencyRegion == "near cut-off":
            fileSet = set2B.copy()
        if frequencyRegion == "above cut-off":
            fileSet = set2C.copy()
            
    if waveType == "square":
        if frequencyRegion == "below cut-off":
            fileSet = set3A.copy()
        if frequencyRegion == "near cut-off":
            fileSet = set3B.copy()
        if frequencyRegion == "above cut-off":
            fileSet = set3C.copy()
            
    #parsing data file and reading in data
            #filenames are Vin and Vout
            #files are read into the lists VinList and VoutList
            #parsed as need into the list VinValues and VoutValues
            
    Vin= open(fileSet[0], 'r')
    Vout= open(fileSet[1], 'r')
    
    VinList = Vin.readlines()
    VoutList = Vout.readlines()
    
    VinValues = []
    VoutValues = []
    
    for line in VinList:
        rowElements = line.split()
        
        #making sure voltage data is in millivolts
        if rowElements [4] != 'mv':
            if rowElements [4] == 'uv':
                rowElements[3] = float(rowElements[3])/1000
            elif rowElements [4] == 'v':
                rowElements[3] = float(rowElements[3])*1000
                
        VinValue = float(rowElements[3])
        VinValues.append(VinValue)
                        
    
    for line in VoutList:
        rowElements = line.split()
        
        #making sure voltage data is in millivolts
        if rowElements [4] != 'mv':
            if rowElements [4] == 'uv':
                rowElements[3] = float(rowElements[3])/1000
            elif rowElements [4] == 'v':
                rowElements[3] = float(rowElements[3])*1000
                
        VoutValue = float(rowElements[3])
        
        VoutValues.append(VoutValue)
                        

    #deselecting data (limiting range for zoom)
        
#    VinValues = VinValues[0:100]
 #   VoutValues = VoutValues[0:100]
    
     # creating x-axis with a delta T of 0.01 milliseconds
     
    tValues = []
    tInitial = 0.00
    tValues.append(tInitial)
    for i in range(3199):
        t=tInitial+deltaT
        tValues.append(t)
        tInitial=t
    
    #model
    initialVout = VoutValues[0]
    VoutModel = [initialVout]
    for VinValue in VinValues:
        nextVout = (VinValue + RCoverdeltaT*(initialVout))/(RCoverdeltaT + 1)
        VoutModel.append(nextVout-3.5)
        initialVout = nextVout
        
    VoutModel = VoutModel[0:3200]
    
     #chi-square analysis
    
    chisq = 0
    
    for i in range(3199):
        chiSquare = (VoutValues[i]-VoutModel[i]/0.01)**2
        chisq = chisq + chiSquare
    
    dof = 100-2     #3200 data values minus two constraints (resistance and capacitance)
    reducedChisq = chisq/dof
    chisqProb = 1 - chi2.cdf(chisq, dof)
    
    print ("Chi-square =", chisq)
    print("Reduced Chi-square =", reducedChisq)
    print("Chi-Square Probability =", chisqProb)
    
    #model
    
    
    
   #plotting

    x = tValues
    fig, (ax1, ax2) = plt.subplots(2)
    fig.suptitle("Plot 1: Vin, Plot 2: Vout overlayed with model")
    ax1.plot(x, VinValues)
    ax1.set(ylabel='Vin')
    ax2.plot(x, VoutValues)
    ax2.set(ylabel='Vout and Model')
    ax2.plot(x, VoutModel)
    plt.xlabel("Time")
    plt.show()
    
    
   
    
    
    
    
    
    
        
        
main()
    
    
    
    