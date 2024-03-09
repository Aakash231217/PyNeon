import numpy as np
import matplotlib.pyplot as plt
sims = 100000
A = np.random.uniform(3,5,sims)
B = np.random.uniform(2,5,sims)

duration = A+B
plt.figure(figsize = (3,1.5))
plt.hist(duration, density = True)
plt.axvline(9, color = 'r')
plt.show()
print((duration > 9).sum()/sims)