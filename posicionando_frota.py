def define_posicoes(linha, coluna, orientacao, tamanho):
    posicoes = []
    
    if orientacao == "vertical":
        for i in range(tamanho):
            posicoes.append([linha+i, coluna])
    else:
        for i in range(tamanho):
            posicoes.append([linha, coluna+i])
    
    return posicoes

def preenche_frota(frota, nome_navio, linha, coluna, orientacao, tamanho):
    posicoes = define_posicoes(linha, coluna, orientacao, tamanho)
    
    if nome_navio in frota:
        frota[nome_navio].append(posicoes)
    else:
        frota[nome_navio] = [posicoes]
    
    return frota

def posicao_valida(frota, linha, coluna, orientacao, tamanho):
    posicoes = define_posicoes(linha, coluna, orientacao, tamanho)
    
    for posicao in posicoes:
        if posicao[0] < 0 or posicao[0] > 9 or posicao[1] < 0 or posicao[1] > 9:
            return False
    
    for navio in frota.values():
        for i in navio:
            for posicao in posicoes:
                if posicao in i:
                    return False
    
    return True


frota = {
    "porta-aviões": [],
    "navio-tanque": [],
    "contratorpedeiro": [],
    "submarino": [],
}

embarcacoes = {
    "porta-aviões": {
        'quantidade': 1,
        'tamanho': 4,
    },
    "navio-tanque": {
        'quantidade': 2,
        'tamanho': 3,
    }, 
    "contratorpedeiro": {
        'quantidade': 3,
        'tamanho': 2,
    },
    "submarino": {
        'quantidade': 4,
        'tamanho': 1,
    }
}

for nome_navio, informacoes_navio in embarcacoes.items():
    for embarcacao in range(informacoes_navio['quantidade']):
        print(f"Insira as informações referentes ao navio {nome_navio} que possui tamanho {informacoes_navio['tamanho']}")
        linha = int(input('Linha: '))
        coluna = int(input('Coluna: '))

        if nome_navio == 'submarino':
            orientacao = 'vertical'
        else:
            opcao_orientacao = int(input('[1] Vertical [2] Horizontal > '))
        
        if opcao_orientacao == 1:
            orientacao = 'vertical'
        else:
            orientacao = 'horizontal'

        while not posicao_valida(frota, linha, coluna, orientacao, informacoes_navio['tamanho']):
            print("Esta posição não está válida!")
            print(f"Insira as informações referentes ao navio {nome_navio} que possui tamanho {informacoes_navio['tamanho']}")
            linha = int(input('Linha: '))
            coluna = int(input('Coluna: '))

            if nome_navio == 'submarino':
                orientacao = 'vertical'
            else:
                opcao_orientacao = int(input('[1] Vertical [2] Horizontal > '))
            
            if opcao_orientacao == 1:
                orientacao = 'vertical'
            else:
                orientacao = 'horizontal'

        frota = preenche_frota(frota, nome_navio, linha, coluna, orientacao, informacoes_navio['tamanho'])

print(frota)