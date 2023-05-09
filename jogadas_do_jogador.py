def define_posicoes(linha, coluna, orientacao, tamanho):
    posicoes = []
    
    if orientacao == "vertical":
        for i in range(tamanho):
            posicoes.append([linha+i, coluna])
    else:
        for i in range(tamanho):
            posicoes.append([linha, coluna+i])
    
    return posicoes

def afundados(frota, tabuleiro):
    afundados = 0
    for tipo_navio in frota:
        for posicoes in frota[tipo_navio]:
            afundou = True
            for posicao in posicoes:
                linha, coluna = posicao 
                if tabuleiro[linha][coluna] != 'X':
                    afundou = False
                    break
            if afundou:
                afundados += 1
    
    return afundados

def posiciona_frota(frota):
    tabuleiro = [[0] * 10 for i in range(10)]
    for navio, posicoes in frota.items():
        for posicao in posicoes:
            for linha, coluna in posicao:
                tabuleiro[linha][coluna] = 1
    
    return tabuleiro

def preenche_frota(frota, nome_navio, linha, coluna, orientacao, tamanho):
    posicoes = define_posicoes(linha, coluna, orientacao, tamanho)
    
    if nome_navio in frota:
        frota[nome_navio].append(posicoes)
    else:
        frota[nome_navio] = [posicoes]
    
    return frota

def faz_jogada(tabuleiro, linha, coluna):
    if tabuleiro[linha][coluna] == 1:
        tabuleiro[linha][coluna] = 'X'
    else:
        tabuleiro[linha][coluna] = '-'

    return tabuleiro

def monta_tabuleiros(tabuleiro_jogador, tabuleiro_oponente):
    texto = ''
    texto += '   0  1  2  3  4  5  6  7  8  9         0  1  2  3  4  5  6  7  8  9\n'
    texto += '_______________________________      _______________________________\n'

    for linha in range(len(tabuleiro_jogador)):
        jogador_info = '  '.join([str(item) for item in tabuleiro_jogador[linha]])
        oponente_info = '  '.join([info if str(info) in 'X-' else '0' for info in tabuleiro_oponente[linha]])
        texto += f'{linha}| {jogador_info}|     {linha}| {oponente_info}|\n'

    return texto

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

frota_oponente = {
    'porta-aviões': [
        [[9, 1], [9, 2], [9, 3], [9, 4]]
    ],
    'navio-tanque': [
        [[6, 0], [6, 1], [6, 2]],
        [[4, 3], [5, 3], [6, 3]]
    ],
    'contratorpedeiro': [
        [[1, 6], [1, 7]],
        [[0, 5], [1, 5]],
        [[3, 6], [3, 7]]
    ],
    'submarino': [
        [[2, 7]],
        [[0, 6]],
        [[9, 7]],
        [[7, 6]]
    ]
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

tabuleiro_op = posiciona_frota(frota_oponente)
tabuleiro_jog = posiciona_frota(frota)

jogadas = []

jogando = True
while jogando:
    print(monta_tabuleiros(tabuleiro_jog, tabuleiro_op))

    #perguntar linha e validar
    linha = int(input('Jogador, qual linha deseja atacar? '))
    while linha > 9 or linha < 0:
        print('Linha inválida!')
        linha = int(input('Jogador, qual linha deseja atacar? '))
    
    #perguntar coluna e validar
    coluna = int(input('Jogador, qual coluna deseja atacar? '))
    while coluna > 9 or coluna < 0:
        print('Coluna inválida!')
        coluna = int(input('Jogador, qual coluna deseja atacar? '))
    #se posição valida, faz jogada
    if [linha, coluna] in jogadas:
        print(f'A posição linha {linha} e coluna {coluna} já foi informada anteriormente')
    else:
        tabuleiro_op = faz_jogada(tabuleiro_op, linha, coluna)
        jogadas.append([linha, coluna])
    #se afundou todos os navios (funcao afundados) jogando = False e imprime mensagem
        if afundados(frota_oponente, tabuleiro_op) == 10:
            print('Parabéns! Você derrubou todos os navios do seu oponente!')
            jogando = False

        
