# main.py
# Script principal que permite cadastrar produtos ou consultar tributos para NF.
# Rode com python main.py e escolha o modo.

from config import ARQUIVO_JSON
from data import carregar_dados, salvar_dados
from interface import (obter_dados_do_produto, escolher_produto, definir_regime, 
                       regiao_venda, mostrar_resultado, exibir_mensagem)
from dados import obter_informacoes_tributarias

def modo_cadastro():
    """
    Modo para cadastrar um novo produto.
    """
    produtos = carregar_dados(ARQUIVO_JSON)
    ultimo_id = max((p.get("id", 0) for p in produtos), default=0)
    proximo_id = ultimo_id + 1
    novo_produto = obter_dados_do_produto(proximo_id)
    produtos.append(novo_produto)
    salvar_dados(ARQUIVO_JSON, produtos)
    exibir_mensagem("\nProduto cadastrado com sucesso!")

def modo_consulta():
    """
    Modo para consultar tributos de um produto para NF.
    """
    produtos = carregar_dados(ARQUIVO_JSON)
    if not produtos:
        print("Nenhum produto cadastrado. Cadastre primeiro.")
        return
    while True:
        produto_selecionado = escolher_produto(produtos)
        if not produto_selecionado:
            return
        regime = definir_regime()
        regiao = regiao_venda()
        info_tributaria = obter_informacoes_tributarias(regime, regiao)
        mostrar_resultado(produto_selecionado, regime, regiao, info_tributaria)
        resp = input("Deseja consultar outro produto? (s/n): ").strip().lower()
        if resp == "n":
            print("Encerrando consulta...")
            break

if __name__ == "__main__":
    while True:
        print("\nBem-vindo ao Gerenciador de Produtos e Tributos Fiscais!")
        print("1. Cadastrar novo produto")
        print("2. Consultar tributos para Nota Fiscal")
        print("3. Sair")
        op = input("Escolha uma opção: ").strip()
        if op == "1":
            modo_cadastro()
        elif op == "2":
            modo_consulta()
        elif op == "3":
            print("Encerrando o programa. Até logo!")
            break
        else:
            print("Opção inválida.")