import numpy as np

# Membuat vector
a = np.array([1, 2, 3, 4, 5])
b = np.array([1.5, 4.6, 7.1, 8, 9])

# Membuat vector dengan arange
c = np.arange(1, 10, 1)

# Membuat linspace
d = np.linspace(1, 10, 4)

# Array Multidimensi/matriks
e = np.array([(1, 2, 3), (3, 0, 1)])

# Matriks nol
f = np.zeros((5, 5))

# Matrks satu
g = np.ones((5, 5))

# Matriks Identitas
h = np.identity(5)

# Display
print(f"\nmembuat vector:\n{a}\n{b}")
print(f"\nvector dengan range:\n{c}")
print(f"\nlinspace:\n{d}")
print(f"\narray multidimensi/matriks:\n{e}\n\n{f}\n\n{g}\n\n{h}")
