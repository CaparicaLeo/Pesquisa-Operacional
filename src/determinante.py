import numpy as np;

def determinante(matriz):
    n = matriz.shape[0]
    #if matriz.shape != (n, n):
    #   raise ValueError("A matriz deve ser quadrada.")
    
    if n==1:
        return matriz[0,0]
    
    if n == 2:
        return matriz[0, 0] * matriz[1, 1] - matriz[0, 1] * matriz[1, 0]
    

    det = 0
    for j in range(n):
        submatriz = np.delete(np.delete(matriz, 0, axis=0), j, axis=1)  # remove 1ª linha e j-ésima coluna
        cofator = ((-1) ** j) * matriz[0, j] * determinante(submatriz)
        det += cofator
    
    return det
    
    

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


matriz_lida = ler_matriz()
det = determinante(matriz_lida)
print(f'Matriz lida: \n {matriz_lida} \n Determinante da matriz: {det}')