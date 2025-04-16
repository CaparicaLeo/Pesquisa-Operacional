import numpy as np;

def multiplicarMatriz(matrizA, matrizB):
    # Verifica se as matrizes podem ser multiplicadas
    if len(matrizA[0]) != len(matrizB):
        raise ValueError("Número de colunas da primeira matriz deve ser igual ao número de linhas da segunda.")

    linhas_A = len(matrizA)
    colunas_B = len(matrizB[0])
    colunas_A = len(matrizA[0])

    # Cria a matriz resultado cheia de zeros
    matriz_resultante = np.zeros((linhas_A, colunas_B))

    # Multiplicação manual
    for i in range(linhas_A):
        for j in range(colunas_B):
            for k in range(colunas_A):
                matriz_resultante[i][j] += matrizA[i][k] * matrizB[k][j]

    return matriz_resultante