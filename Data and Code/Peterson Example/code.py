import matplotlib.pyplot as plt
import numpy as np
from scipy.stats import chi2

# load the data
data = np.loadtxt('chisqprob_demo.py', delimiter=',', skiprows=29, max_rows=3200)
vmeas = data[:,0]
vmodel = data[:,1]

sd_volts = 0.06 # voltage measurement uncertainty (estimated)

chisq = np.sum(((vmeas - vmodel) / sd_volts ) ** 2)
dof = len(vmeas) - 4

# probability of obtaining reduced chi-square > chisq/dof
chisqprob = 1 - chi2.cdf(chisq, dof)

plt.plot(vmeas, label='$V_{out}$', linestyle='None', marker='o')
plt.plot(vmodel, label='$V_{model}$')
plt.xlabel('Time ($\mu$sec)')
plt.ylabel('Voltage (V)')
plt.title('RC LPF Finite Difference Model')
plt.annotate('Chi-Square Probability = %f' % chisqprob,
                xy=(0.45, 0.95), xycoords='axes fraction')
plt.legend()
plt.show()
