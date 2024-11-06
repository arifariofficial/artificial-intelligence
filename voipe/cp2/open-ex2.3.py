import numpy as np
import matplotlib.pyplot as plt

data = np.genfromtxt(
    "/Users/ari/Desktop/artificial-intelligence/voipe/cp2/weight-height.csv",
    delimiter=",",
    skip_header=1,
    usecols=(1, 2),
)

lengths_in_inches = data[:, 0]
weights_in_pounds = data[:, 1]

lengths_in_cm = lengths_in_inches * 2.54
weights_in_kg = weights_in_pounds * 0.453592

mean_length = np.mean(lengths_in_cm)
meidan_length = np.median(lengths_in_cm)
std_dev_length = np.std(lengths_in_cm)
variance_length = np.var(lengths_in_cm)

mean_weight = np.mean(weights_in_kg)
median_weight = np.median(weights_in_kg)
std_dev_weight = np.std(weights_in_kg)
variance_weight = np.var(weights_in_kg)

plt.hist(lengths_in_cm, bins=20, edgecolor="black")
plt.xlabel("Length (cm)")
plt.ylabel("Frequency")
plt.show()
