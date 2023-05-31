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
# print(mt)

# imprimindo tipo da mt
# print(type(mt))

# mudando o tipo da mt
mt = mt.astype(np.int32)

# também pode-se criar uma nova matriz de novo tipo a partir de uma matriz antiga
novamt = mt.astype(np.int32)

# criar arrays vazios tipificados
vazio = np.empty ([3,2], dtype=int)

# criar matriz 4x3 com valores zero
# sempre serão no formato "ordenadas, absissas"
zero = np.zeros([4,3]) 

#agora uma matriz 5x7 com valores um
um = np.ones([5,7])

# matriz com diagonal principal com valores 1 e outros valores 0
diagonal = np.eye(5)

# matriz quadrada de tamanho 5 com valores aleatórios entre 0 e 1
aleatório = np.random.random((5))

# dados aleatórios numa distribuição normal
aleatório = np.random.randn((5))
print(aleatório)
