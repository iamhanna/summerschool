"""
Create function to illustrate optimization
"""

import matplotlib.pyplot as plt
import math
import numpy as np

inputs = np.random.uniform(-330, 330, 2000)
outputs = [x**4 + (0.4*(x-20))**3+(x-40)**2 + 500 for x in inputs]
outputs = [(0.1*x)**4-(3*x)**2 + 200*x + 200*math.sin(0.01*x) for x in inputs]

title = 'function'
file = 'function.pdf'
plt.plot(inputs, outputs, 'o')
plt.xlabel('input')
plt.ylabel('output')
plt.title(title)
plt.savefig('images/' + file)
