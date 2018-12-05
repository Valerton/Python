import numpy as np
def find(z,A):
    index=np.unravel_index(abs(A-z).argmin(), A.shape)
    print(index)
    print(A[index])
a = np.random.randint(0, 100, (10, 10))
print(a)
find(60,a)