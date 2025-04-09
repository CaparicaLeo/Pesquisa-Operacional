import numpy as np

def ler_matriz():
    n = int(input('Selecione a ordem de sua matriz quadrada: '))
    
    dados = []
    for i in range(n):
        linha = []
        for j in range(n):
            valor = float(input(f'Insira o número da Linha {i+1}, Coluna {j+1}: '))
            linha.append(valor)
        dados.append(linha)
            
    matriz = np.array(dados)    
    return matriz 

def determinante(matriz: np.ndarray) -> float:
    n = matriz.shape[0]
    
    if n == 1:
        return matriz[0, 0]
    
    if n == 2:
        return matriz[0, 0] * matriz[1, 1] - matriz[0, 1] * matriz[1, 0]
    
    det = 0
    for j in range(n):
        submatriz = np.delete(np.delete(matriz, 0, axis=0), j, axis=1)
        cofator = ((-1) ** j) * matriz[0, j] * determinante(submatriz)
        det += cofator
    
    return det

def inversa(matriz: np.ndarray) -> np.ndarray:
    n = matriz.shape[0]
    det = determinante(matriz)
    
    if det == 0:
        raise ValueError("A matriz não possui inversa (determinante = 0).")

    cofatores = np.zeros((n, n))

    for i in range(n):
        for j in range(n):
            submatriz = np.delete(np.delete(matriz, i, axis=0), j, axis=1)
            cofator = ((-1) ** (i + j)) * determinante(submatriz)
            cofatores[i, j] = cofator

    adjunta = cofatores.T  # transposta da matriz de cofatores
    inversa = (1 / det) * adjunta
    return inversa

# Execução
matriz_lida = ler_matriz()
inver = inversa(matriz_lida)

print(f'\nMatriz Lida:\n{matriz_lida}')
print(f'\nMatriz Inversa:\n{inver}')
