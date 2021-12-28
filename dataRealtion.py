import matplotlib.pyplot as plt
import numpy as np

Rawvalues = [300,245,200,170,145,130,112,103,93,87,80,75,70,67,62,59,57]
measuredValues = [20,25,30,35,40,45,50,55,60,65,70,75,80,85,90,95,100]

plt.scatter(Rawvalues,measuredValues)
plt.plot(Rawvalues,measuredValues,color='r')
plt.ylabel("Values measured with a Tape")
plt.xlabel("Values from Python scripts#")
plt.show()

###From the graph it is evident that the Raw values and measured values are not linear but polynoimially distributed with a degree 2. 
##https://en.wikipedia.org/wiki/Polynomial - check graphs subsection for reference.
