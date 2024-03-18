#search

import os
from collections import defaultdict

def ler_arquivo(caminho):
    with open(caminho, 'r', encoding='utf-8') as arquivo:
        return arquivo.read()

def encontrar_texto_comum(caminho_pasta, termos_pesquisa_arquivo, nome_arquivo_saida=None):
    arquivos = [arquivo for arquivo in os.listdir(caminho_pasta) if arquivo.endswith(".txt")]

    textos = defaultdict(str)
    for arquivo in arquivos:
        caminho_arquivo = os.path.join(caminho_pasta, arquivo)
        texto = ler_arquivo(caminho_arquivo)
        textos[arquivo] = texto

    resultados = defaultdict(lambda: defaultdict(int))
    with open(termos_pesquisa_arquivo, 'r', encoding='utf-8') as arquivo_termos:
        termos_pesquisa = [termo.strip().replace(" ", "") for termo in arquivo_termos.read().split(';')]

    if nome_arquivo_saida is None:
        nome_arquivo_saida = input("Digite o nome do arquivo de saída: ")

    for termo_original in termos_pesquisa:
        termo_lower = termo_original.lower().replace(" ", "")  # Converter para minúsculas e remover espaços
        for arquivo, texto in textos.items():
            texto_lower = texto.lower().replace(" ", "")  # Converter para minúsculas e remover espaços
            quantidade = texto_lower.count(termo_lower)
            if quantidade > 0:
                resultados[termo_original][arquivo] += quantidade

    with open(nome_arquivo_saida, 'w', encoding='utf-8') as arquivo_saida:
        for termo, ocorrencias in resultados.items():
            arquivo_saida.write(f'O termo "{termo}" foi encontrado nas seguintes quantidades nos arquivos:\n')
            for arquivo, quantidade in ocorrencias.items():
                arquivo_saida.write(f'- No arquivo {arquivo}: {quantidade} vezes\n')
            arquivo_saida.write('\n')

    print(f"Os resultados foram salvos no arquivo '{nome_arquivo_saida}'.")

if __name__ == "__main__":
    caminho_diretorio = input("Digite o caminho do diretório: ")
    
    termos_pesquisa_arquivo = input("Digite o nome do arquivo contendo os termos de pesquisa (txt): ")

    encontrar_texto_comum(caminho_diretorio, termos_pesquisa_arquivo)
