import numpy as np

# declarando mt
mt = np.array([12, 24.99999, 10, 18, 10])

# declarando mt com tipo especificado
mt = np.array([12, 24.99999, 10, 18, 10], dtype=np.float64)

# declarar mt com mais de uma dimensão
mt = np.array(
    [
        [12, 24.99999, 10, 18, 10],
        [
            10,
            20,
            30,
            40,
            50,
        ],
        [24, 15, 44, 21, 42],
    ],
    dtype=np.float64,
)

# imprimindo mt
print(mt)

# imprimindo tipo da mt
print(type(mt))

# mudando o tipo da mt
mt = mt.astype(np.int32)

# também pode-se criar uma nova matriz de novo tipo a partir de uma matriz antiga
novamt = mt.astype(np.int32)

