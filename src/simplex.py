from determinante import determinante;
from leitor import lerTxt;
from inversa import inversa;
from multiplicarMatriz import multiplicarMatriz;
import numpy as np;

def simplex(tipo, A, b, c):
    A = np.array(A, dtype=float)
    b = np.array(b, dtype=float)
    c = np.array(c, dtype=float)

    if tipo == 'min':
        c = -c  # transforma em maximização

    num_restricoes, num_variaveis = A.shape

    # Monta a tabela do simplex
    tabela = np.zeros((num_restricoes + 1, num_variaveis + 1))
    tabela[:num_restricoes, :num_variaveis] = A
    tabela[:num_restricoes, -1] = b
    tabela[-1, :num_variaveis] = -c

    # Lista para rastrear variáveis básicas
    variaveis_basicas = [f"x{i+1}" for i in range(num_variaveis, num_variaveis + num_restricoes)]
    variaveis_todas = [f"x{i+1}" for i in range(num_variaveis)] + variaveis_basicas

    iteracao = 0
    while True:
        print(f"\nIteração {iteracao}")
        print("Tabela:")
        print(np.round(tabela, 3))

        # Mostrar variáveis básicas e não básicas
        basicas = []
        nao_basicas = []
        for j in range(num_variaveis):
            coluna = tabela[:num_restricoes, j]
            if list(coluna).count(1) == 1 and list(coluna).count(0) == num_restricoes - 1:
                linha = np.where(coluna == 1)[0][0]
                basicas.append((f"x{j+1}", tabela[linha, -1]))
            else:
                nao_basicas.append(f"x{j+1}")

        print("Variáveis básicas:", [f"{v} = {round(val, 3)}" for v, val in basicas])
        print("Variáveis não básicas:", nao_basicas)

        # Passo 1: escolher coluna pivô (menor valor negativo na linha Z)
        coluna_pivo = np.argmin(tabela[-1, :-1])
        if tabela[-1, coluna_pivo] >= 0:
            break  # solução ótima encontrada

        # Passo 2: escolher linha pivô (menor razão positiva)
        razoes = []
        for i in range(num_restricoes):
            elemento = tabela[i, coluna_pivo]
            if elemento > 0:
                razoes.append(tabela[i, -1] / elemento)
            else:
                razoes.append(np.inf)

        linha_pivo = np.argmin(razoes)
        if all(r == np.inf for r in razoes):
            raise ValueError("Problema ilimitado!")

        # Passo 3: pivoteamento
        pivo = tabela[linha_pivo, coluna_pivo]
        tabela[linha_pivo, :] /= pivo

        for i in range(num_restricoes + 1):
            if i != linha_pivo:
                tabela[i, :] -= tabela[i, coluna_pivo] * tabela[linha_pivo, :]

        iteracao += 1

    # Resultado final
    print("\n✅ Tabela final do Simplex:")
    print(np.round(tabela, 3))

    solucao = np.zeros(num_variaveis)
    for j in range(num_variaveis):
        coluna = tabela[:num_restricoes, j]
        if list(coluna).count(1) == 1 and list(coluna).count(0) == num_restricoes - 1:
            linha = np.where(coluna == 1)[0][0]
            solucao[j] = tabela[linha, -1]

    print("\n✅ Solução ótima:")
    print("Variáveis:", np.round(solucao, 3))
    print("Valor ótimo de Z:", np.round(tabela[-1, -1], 3))


tipo, a, b, c = lerTxt("entrada.txt")
simplex(tipo,a,b,c)
