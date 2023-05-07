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