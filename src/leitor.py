import re

def lerTxt():
    with open('src/assets/entrada.txt', 'r', encoding='utf-8') as entrada:
        linhas = entrada.readlines()

    tipo_funcao = definitTipoFunc(linhas[0])
    restricoes = processaRestricoes(linhas[1:])

    vetor_c = acharC(linhas[0], restricoes['n_variaveis'], restricoes['tipos'])
    matriz_a = construirMatrizA(restricoes)
    vetor_b = restricoes['vetor_b']

    print("Tipo:", tipo_funcao)
    print("Vetor C:", vetor_c)
    print("Matriz A:")
    for linha in matriz_a:
        print(linha)
    print("Vetor B:", vetor_b)


def definitTipoFunc(linha):
    if 'max' in linha.lower():
        return 'max'
    elif 'min' in linha.lower():
        return 'min'
    else:
        raise ValueError("A função deve ser 'max' ou 'min'")


def acharC(linha, n_vars, tipos_restricoes):
    parte = linha.split('=')[1]
    termos = re.findall(r'([+-]?\s*\d*)\s*[a-zA-Z]', parte)
    vetor_c = []

    for termo in termos:
        termo = termo.replace(' ', '')
        if termo in ('', '+'):
            coef = 1
        elif termo == '-':
            coef = -1
        else:
            coef = int(termo)
        vetor_c.append(coef)

    # Completa com zeros caso faltem variáveis (x e y por exemplo)
    while len(vetor_c) < n_vars:
        vetor_c.append(0)

    # Adiciona zeros para as variáveis de folga
    n_folgas = tipos_restricoes.count('<=') + tipos_restricoes.count('>=')
    vetor_c.extend([0] * n_folgas)

    return vetor_c


def processaRestricoes(linhas):
    matriz = []
    vetor_b = []
    tipos = []
    n_vars = 0  # número de variáveis reais (x, y)

    for linha in linhas:
        if '<=' in linha:
            lado_esq, lado_dir = linha.split('<=')
            tipos.append('<=')
        elif '>=' in linha:
            lado_esq, lado_dir = linha.split('>=')
            tipos.append('>=')
        elif '=' in linha:
            lado_esq, lado_dir = linha.split('=')
            tipos.append('=')
        else:
            continue

        coeficientes = re.findall(r'([+-]?\s*\d*)\s*[a-zA-Z]', lado_esq)
        linha_coef = []
        for termo in coeficientes:
            termo = termo.replace(' ', '')
            if termo in ('', '+'):
                coef = 1
            elif termo == '-':
                coef = -1
            else:
                coef = int(termo)
            linha_coef.append(coef)

        n_vars = max(n_vars, len(linha_coef))
        matriz.append(linha_coef)
        vetor_b.append(int(lado_dir.strip()))

    return {
        'matriz': matriz,
        'vetor_b': vetor_b,
        'tipos': tipos,
        'n_variaveis': n_vars
    }


def construirMatrizA(info):
    matriz = info['matriz']
    tipos = info['tipos']
    n_folgas = tipos.count('<=') + tipos.count('>=')
    matriz_resultado = []
    folga_index = 0

    for i, linha in enumerate(matriz):
        # Completa com zeros caso alguma linha tenha menos variáveis
        while len(linha) < info['n_variaveis']:
            linha.append(0)

        folgas = [0] * n_folgas
        if tipos[i] == '<=':
            folgas[folga_index] = 1
            folga_index += 1
        elif tipos[i] == '>=':
            folgas[folga_index] = -1
            folga_index += 1
        # '=' não adiciona folga

        linha_final = linha + folgas
        matriz_resultado.append(linha_final)

    return matriz_resultado
lerTxt()