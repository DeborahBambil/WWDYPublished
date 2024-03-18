def gerar_abreviacao(nome):
    partes = nome.split()
    sobrenome = partes[-1].upper()
    primeira_letra = partes[0][0].upper()
    abreviacao_com_pontos = f"{sobrenome}, {primeira_letra}"
    return f"{abreviacao_com_pontos}"

def processar_nomes_arquivo(nome_arquivo_entrada, nome_arquivo_saida):
    with open(nome_arquivo_entrada, 'r') as arquivo_entrada:
        nomes = arquivo_entrada.read().splitlines()

    abreviacoes = ';'.join([gerar_abreviacao(nome) for nome in nomes])

    with open(nome_arquivo_saida, 'w') as arquivo_saida:
        arquivo_saida.write(abreviacoes)

    print(f"Resultados salvos em '{nome_arquivo_saida}'")

# Solicitar nome do arquivo de entrada e saída
nome_arquivo_entrada = input("Digite o nome do arquivo de entrada: ")
nome_arquivo_saida = input("Digite o nome do arquivo de saída: ")

# Processar os nomes e salvar no arquivo de saída
processar_nomes_arquivo(nome_arquivo_entrada, nome_arquivo_saida)
