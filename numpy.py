import numpy as np

# declarando matriz
mfloat = np.array([12, 24.99999, 10, 18, 10])

# declarando matriz com tipo especificado
mfloat = np.array([12, 24.99999, 10, 18, 10], dtype=np.float64)

# declarar matriz com mais de uma dimensão
mfloat = np.array([[12, 24.99999, 10, 18, 10],
                   [10, 20, 30, 40, 50, 60,],
                   [24, 15, 44, 21, 42, 71]],
                    dtype=np.float64)

# imprimindo matriz
print(mfloat) 

# imprimindo tipo da matriz
print(type(mfloat))

# mudando o tipo da matriz
mfloat = mfloat.astype(np.int32)
