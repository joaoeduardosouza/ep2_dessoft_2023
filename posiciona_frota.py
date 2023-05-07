def posiciona_frota(frota):
    tabuleiro = [[0] * 10 for i in range(10)]
    for navio, posicoes in frota.items():
        for posicao in posicoes:
            for linha, coluna in posicao:
                tabuleiro[linha][coluna] = 1
    
    return tabuleiro