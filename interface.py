# interface.py
# Funções de interface com o usuário: inputs validados, exibições e mensagens.
# Usado tanto para cadastro quanto para consulta tributária.

from datetime import datetime
from zoneinfo import ZoneInfo

def ler_numero(msg, tipo=float, min_val=None):
    """
    Lê um número do usuário com validação. Suporta float (com vírgula/ponto) ou int.
    """
    while True:
        try:
            entrada = input(msg).strip()
            if tipo == float:
                entrada = entrada.replace(".", "")  # Remove separador de milhares
                entrada = entrada.replace(",", ".")  # Normaliza decimal pra ponto
            valor = tipo(entrada)
            if min_val is not None and valor < min_val:
                print(f"Valor deve ser maior ou igual a {min_val}. Tente novamente.")
                continue
            return valor
        except ValueError:
            print("Valor inválido. Tente novamente.")

def validar_ncm(ncm_str):
    """
    Valida se NCM é string de exatamente 8 dígitos.
    """
    return len(ncm_str) == 8 and ncm_str.isdigit()

def obter_dados_do_produto(proximo_id):
    """
    Coleta dados de um novo produto via input do usuário.
    Inclui data de cadastro automática no fuso horário de SP.
    """
    br_time = datetime.now(ZoneInfo("America/Sao_Paulo"))
    ativo_input = input("Produto ativo? (s/n): ").strip().lower()
    ativo = ativo_input in ["s", "sim", "y", "yes"]
    while True:
        ncm_str = input("NCM do produto (ex: 01234567): ").strip()
        if validar_ncm(ncm_str):
            break
        print("NCM inválido: deve ter exatamente 8 dígitos. Tente novamente.")
    produto = {
        "id": proximo_id,
        "nome": input("Nome do produto: ").strip(),
        "descricao": input("Descrição do produto: ").strip(),
        "preco": ler_numero("Preço do produto: R$ ", tipo=float, min_val=0),
        "categoria": input("Categoria do produto: ").strip(),
        "estoque": ler_numero("Quantidade em estoque: ", tipo=float, min_val=0),  # int pra float, pra permitir decimais (ex: 40.5)
        "unidade": input("Unidade (ex: un, kg, t): ").strip(),
        "ncm": ncm_str,
        "ativo": ativo,
        "data_cadastro": br_time.strftime('%d/%m/%Y %H:%M')
    }
    return produto

def escolher_produto(produtos):
  
    # Exibe lista de produtos e permite seleção por número.
    
    if not produtos:
        print("Nenhum produto cadastrado ainda.")
        return None
    print("\nProdutos disponíveis:")
    for idx, prod in enumerate(produtos, 1):
        estoque_formatado = f"{prod['estoque']:.2f}" if isinstance(prod['estoque'], float) and prod['estoque'] % 1 != 0 else f"{int(prod['estoque'])}"  # MUDANÇA: Formatação pra mostrar decimais só se necessário (ex: 40.5 vira "40.5", 40 vira "40")
        qtd_unid = f"{estoque_formatado} {prod['unidade']}"
        print(f"{idx}. {prod['nome']}")
        print(f"\tCategoria: {prod['categoria']}")
        print(f"\tPreço: R$ {prod['preco']:.2f} | Quantidade: {qtd_unid}")
        print(f"\tDescrição: {prod['descricao']}")
    while True:
        try:
            escolha = int(input("\nEscolha o número do produto: "))
            if 1 <= escolha <= len(produtos):
                return produtos[escolha - 1]
            print("Número fora do intervalo.")
        except ValueError:
            print("Opção inválida. Digite um número.")

def definir_regime():
    
    #Seleciona o regime tributário via input.
    
    while True:
        op = input("Regime (1. Convênio xx | 2. TTD xx): ").strip()
        if op == "1":
            return "convenio xx"
        if op == "2":
            return "ttd xx"
        print("Opção inválida.")

def regiao_venda():
    
    #Seleciona a região de venda
    
    while True:
        op = input("Venda (1. Interna SC | 2. Externa): ").strip()
        if op == "1":
            return "interna/sc"
        if op == "2":
            est = input("Estado (PR, RS, MT, MS): ").strip().lower()
            if est in ['pr', 'rs', 'mt', 'ms']:
                return f"externa/{est}"
        print("Opção inválida.")

def mostrar_resultado(produto_dic, regime, regiao, info_fiscal):
    
    #Exibe o resultado formatado com dados do produto e tributos para NF.
    
    regime_nome = "Convênio xx" if "convenio" in regime else "TTD xx"
    estoque_formatado = f"{produto_dic['estoque']:.2f}" if isinstance(produto_dic['estoque'], float) and produto_dic['estoque'] % 1 != 0 else f"{int(produto_dic['estoque'])}"  # MUDANÇA: Mesma formatação pra estoque em qtd_unid
    qtd_unid = f"{estoque_formatado} {produto_dic['unidade']}"
    total = produto_dic['preco'] * produto_dic['estoque']

    print("\n" + "=" * 40)
    print("      INFORMAÇÕES PARA SUA NOTA FISCAL")
    print("=" * 40)

    print("\n--- 1. DADOS DO PRODUTO (CADASTRO) ---")
    print(f"Nome:       {produto_dic['nome']}")
    print(f"NCM:        {produto_dic['ncm']}")
    print(f"Preço Unit: R$ {produto_dic['preco']:.2f}")
    print(f"Quantidade: {qtd_unid}")
    print(f"Valor Total: R$ {total:.2f}")
    print(f"Data de Cadastro: {produto_dic['data_cadastro']}")

    print("\n--- 2. DADOS FISCAIS (TRIBUTAÇÃO) ---")
    print(f"Regime:     {regime_nome}")
    print(f"Destino:    {regiao.upper()}")
    print(f"CFOP:       {info_fiscal.get('CFOP', '-')}")
    print(f"CST:        {info_fiscal.get('CST', '-')}")
    print(f"Cód. Trib.: {info_fiscal.get('tributação do icms', '-')}")

    print("\n--- 3. IMPOSTOS ---")
    print(f"ICMS:   {info_fiscal.get('icms', '-')} %")
    print(f"IPI:    {info_fiscal.get('ipi', '-')} %")
    print(f"PIS:    {info_fiscal.get('pis', '-')} %")
    print(f"COFINS: {info_fiscal.get('cofins', '-')} %")

    print("\n--- DESCRIÇÃO LEGAL ---")
    print(info_fiscal.get('descricao', 'Não disponível.'))
    print("=" * 40 + "\n")

def exibir_mensagem(msg):
    
    #Exibe uma mensagem simples.
    
    print(msg)