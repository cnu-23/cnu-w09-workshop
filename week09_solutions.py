import numpy as np
import matplotlib.pyplot as plt

# Task 1

# Define all values of a
a = np.array([2.9, 3.1, 3.5, 3.7], dtype = float)

# Prepare an array to store the solutions
x = np.zeros([4, 201])
x[:, 0] = np.random.rand(4)

# Iterate all four at the same time
for i in range(x.shape[1] - 1):
    x[:, i + 1] = a * x[:, i] * (1.0 - x[:, i])
    

# Plot the results
fig, ax = plt.subplots(len(a), 1, figsize = (8, 12))
for i in range(len(a)):
    ax[i].plot(x[i, :], "k")
    ax[i].set(xlim=[0, x.shape[1] - 1], ylim=[0, 1], xlabel=r"$n$", ylabel=r"$x_n$", title=f"a = {a[i]}")

plt.subplots_adjust(hspace = 0.5)
plt.show()


# Task 2

# Prepare the plot
fig, ax = plt.subplots()
ax.set(xlabel=r"$a$", ylabel=r"$x_n$")

# Initial value and coefficient a
x = np.random.rand(1)
avals = np.arange(2.5, 3.801, 0.025)

# Loop over values of a
for a in avals:
    # Iterate 100 times per value of a
    for i in range(100):
        x = a * x * (1.0 - x)
        
        # Plot the point
        ax.plot(a, x, 'o', color=[0.1]*4, markersize=2)

plt.show()

# We can see bifurcations happening at certain values of a, which seem to get closer
# and closer together. In many cases, for a given a, the solution seems to periodically
# end up cycling around 2, then 4, then 8 values, etc. (with increasing a). This corresponds
# to the results from Task 1, where for different values of a, we seem to observe some
# periodicity/cycling between distinct values.



# Task 3
# SEE THE NOTEBOOK!

# This also corresponds to observations from Task 2. For instance, at a=3.5,
# we clearly observe that the logistic map eventually settles to a cycle
# between 4 points, corresponding to the 4 distinct points seen at a=3.5
# in the graph from Task 2.
