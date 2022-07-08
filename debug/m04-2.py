def extrai_linha_especifica(nome_arquivo: str, numero_linha: int) -> list:
  
  linha_str = ""
  palavras_linha = []

  with open(file=nome_arquivo, mode='r', encoding='utf8') as arquivo:
    
    # Corrige o índice das linhas do arquivo
    numero_linha = numero_linha - 1
    
    # Percorre todas as linhas do arquivo, que inicia do 0
    for i, linha in enumerate(arquivo):
        # Se a iteração for igual ao número da linha (corrigido), atribui o valor tipo 'str' a uma variável
        if i == numero_linha:
          linha_str = linha.strip()
        # Interrompe a iteração após encontrar a linha desejada
        elif i > numero_linha:
          break

        # Quebra a linha e armazena as palavras em uma lista
        palavras_linha = linha_str.split(" ")

    return palavras_linha

linha18 = extrai_linha_especifica(nome_arquivo='./musica.txt', numero_linha=18)
print(linha18)