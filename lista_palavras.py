# essa é a lista de palavras
palavras = ["paralelepipedo", "museologia", "arte"]

# função da maior palavra
def maiorPalavra(lista_palavras):
    palavra_mais_longa = lista_palavras[0]

    for palavra in lista_palavras:
        if len(palavra) > len(palavra_mais_longa):
            palavra_mais_longa = palavra

    return palavra_mais_longa

# função da menor palavra
def menorPalavra(lista_palavras):
    palavra_mais_curta = lista_palavras[0]

    for palavra in lista_palavras:
        if len(palavra) < len(palavra_mais_curta):
            palavra_mais_curta = palavra

    return palavra_mais_curta
    
print(maiorPalavra(palavras))
print(menorPalavra(palavras))