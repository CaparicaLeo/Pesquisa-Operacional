def lerTxt():
    with open('src/assets/entrada.txt', 'r', encoding='utf-8') as entrada:
        tipo_funcao = definitTipoFunc(entrada)
        
        # Volta pro início do arquivo para as outras funções
        entrada.seek(0)
        vetor_c = acharC(entrada)

        entrada.seek(0)
        matriz_a = acharA(entrada)

        entrada.seek(0)
        vetor_b = acharVetorB(entrada)

        print("Tipo:", tipo_funcao)
        print("Vetor C:", vetor_c)
        print("Matriz A:", matriz_a)
        print("Vetor B:", vetor_b)


def definitTipoFunc(arquivo):
    primeira_linha = arquivo.readline().strip()
    if 'max' in primeira_linha.lower():
        return 'max'
    elif 'min' in primeira_linha.lower():
        return 'min'
    else:
        raise ValueError("Entrada incorreta: não foi encontrado 'max' ou 'min'")


def acharC(arquivo):
    linha = arquivo.readline().strip()
    partes = linha.split('=')[1]  # Pega o lado direito da equação
    partes = partes.replace('+', ' +').replace('-', ' -').split()
    
    vetor_c = []
    for termo in partes:
        coef = ''.join([c for c in termo if c.isdigit() or c == '-' or c == '.'])
        if coef == '' or coef == '-':
            coef += '1'
        vetor_c.append(int(coef))
    
    return vetor_c


def acharA(arquivo):
    linhas = arquivo.readlines()[1:]  # Ignora a primeira linha (função objetivo)
    matriz_a = []

    for linha in linhas:
        lado_esquerdo = linha.split('<=')[0].split('>=')[0].split('=')[0].strip()
        partes = lado_esquerdo.replace('+', ' +').replace('-', ' -').split()

        linha_coef = []
        for termo in partes:
            coef = ''.join([c for c in termo if c.isdigit() or c == '-' or c == '.'])
            if coef == '' or coef == '-':
                coef += '1'
            linha_coef.append(int(coef))
        matriz_a.append(linha_coef)

    return matriz_a


def acharVetorB(arquivo):
    linhas = arquivo.readlines()[1:]  # Ignora a primeira linha (função objetivo)
    vetor_b = []

    for linha in linhas:
        if '<=' in linha:
            valor = linha.split('<=')[1]
        elif '>=' in linha:
            valor = linha.split('>=')[1]
        elif '=' in linha:
            valor = linha.split('=')[1]
        else:
            continue
        vetor_b.append(int(valor.strip()))
    
    return vetor_b


lerTxt()
