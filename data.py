# data.py
# Módulo para carregar e salvar dados em JSON.

import json
import os

def carregar_dados(caminho_arquivo):
    """
    Carrega os dados de produtos de um arquivo JSON.
    Retorna lista vazia se o arquivo não existir ou estiver corrompido.
    """
    if os.path.exists(caminho_arquivo):
        try:
            with open(caminho_arquivo, 'r', encoding='utf-8') as arquivo:
                return json.load(arquivo)
        except json.JSONDecodeError:
            print("Arquivo corrompido ou mal formatado. Retornando lista vazia.")
            return []
        except IOError:
            print("Erro ao ler o arquivo. Verifique permissões.")
            return []
    return []

def salvar_dados(caminho_arquivo, dados):
    """
    Salva os dados de produtos em um arquivo JSON com indentação para legibilidade.
    """
    try:
        with open(caminho_arquivo, 'w', encoding='utf-8') as arquivo:
            json.dump(dados, arquivo, indent=4, ensure_ascii=False)
        print("Dados salvos com sucesso!")
    except IOError:
        print("Erro ao salvar arquivo. Verifique permissões ou espaço em disco.")