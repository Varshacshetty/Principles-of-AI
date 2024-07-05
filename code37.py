import numpy as np
import matplotlib.pyplot as plt

# Define the universe of discourse (x-axis values)
x = np.linspace(0, 10, 100)

# Define two triangular fuzzy sets
# Fuzzy set A: triangular membership function (3, 1, 7)
def fuzzy_set_A(x):
    return np.maximum(0, 1 - abs(x - 5) / 2)

# Fuzzy set B: triangular membership function (6, 2, 9)
def fuzzy_set_B(x):
    return np.maximum(0, 1 - abs(x - 7.5) / 1.5)

# Compute membership degrees for fuzzy sets A and B
membership_A = fuzzy_set_A(x)
membership_B = fuzzy_set_B(x)

# Plot the membership functions of sets A and B
plt.figure(figsize=(8, 4))
plt.plot(x, membership_A, label='Fuzzy Set A')
plt.plot(x, membership_B, label='Fuzzy Set B')
plt.title('Membership Functions of Fuzzy Sets A and B')
plt.xlabel('x')
plt.ylabel('Membership degree')
plt.legend()
plt.grid(True)
plt.show()

# Compute union and intersection of fuzzy sets A and B
union = np.maximum(membership_A, membership_B)
intersection = np.minimum(membership_A, membership_B)

# Plot the resulting fuzzy sets after union and intersection
plt.figure(figsize=(8, 4))
plt.plot(x, union, label='Union of A and B')
plt.plot(x, intersection, label='Intersection of A and B')
plt.title('Union and Intersection of Fuzzy Sets A and B')
plt.xlabel('x')
plt.ylabel('Membership degree')
plt.legend()
plt.grid(True)
plt.show()
