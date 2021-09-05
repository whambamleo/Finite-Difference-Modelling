 i = 0
    initialVout = VoutValues[i]
    VoutModel = []
    for VinValue in VinValues:
        nextVout = (VinValue + RCoverdeltaT*(initialVout))/(RCoverdeltaT + 1)
        VoutModel.append(nextVout)
        i = i+1
        initialVout = VoutValues[i]
        