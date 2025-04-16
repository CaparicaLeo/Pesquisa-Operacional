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