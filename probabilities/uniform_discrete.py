import numpy as np
import matplotlib.pyplot as plt

nb_data = 100

style = {'facecolor': 'blue', 'alpha': 0.2, 'pad': 10}
x = np.random.randint(0, 6, nb_data)
plt.plot(range(nb_data), x, 'o')
title = 'Unifom discrete distribution'
plt.xlabel('datapoint index')
plt.ylabel('datapoint value')
plt.title(title, bbox=style)
plt.savefig('images/uniform_discrete.pdf')
plt.close()

nbins = 50
plt.hist(x, bins=nbins)
title_hist = 'Histogram ' + title
plt.xlabel('datapoint value')
plt.ylabel('number of occurrences')
plt.title(title, bbox=style)
plt.savefig('images/hist_uniform_discrete.pdf')
plt.close()
