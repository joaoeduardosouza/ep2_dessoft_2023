def define_posicoes(linha, coluna, orientacao, tamanho):
    posicoes = []
    
    if orientacao == "vertical":
        for i in range(tamanho):
            posicoes.append([linha+i, coluna])
    elif orientacao == "horizontal":
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

embarcacoes = [
    ("porta-aviões", 4, 1),
    ("navio-tanque", 3, 2),
    ("contratorpedeiro", 2, 3),
    ("submarino", 1, 4)
]

for embarcacao in embarcacoes:
    nome_navio, tamanho, quantidade = embarcacao
    print(f"Insira as informações referentes ao navio {nome_navio} que possui tamanho {tamanho}")
    
    for _ in range(quantidade):
        linha = int(input("Linha: "))
        coluna = int(input("Coluna: "))
        
        if nome_navio == "submarino":
            orientacao = "vertical"
        else:
            opcao_orientacao = int(input("[1] Vertical [2] Horizontal > "))
            orientacao = "vertical" if opcao_orientacao == 1 else "horizontal"
        
        if not posicao_valida(frota, linha, coluna, orientacao, tamanho):
            print("Esta posição não está válida!")
            continue
        
        frota = preenche_frota(frota, nome_navio, linha, coluna, orientacao, tamanho)
    
    print()

print(frota)
