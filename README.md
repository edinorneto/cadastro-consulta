# 💼 Cadastro de Produtos + Consulta Fiscal para NF-e (Demo Educacional)

Este software foi desenvolvido como uma solução prática para um gargalo administrativo comum: a complexidade no preenchimento de dados tributários em notas fiscais manuais.

O Problema: No ambiente corporativo, a equipe frequentemente precisava interromper o fluxo de trabalho para consultar regras fiscais específicas, memorizar códigos (NCM, CFOP, CST) e calcular alíquotas manualmente. Isso gerava ineficiência e aumentava o risco de erro humano.

A Solução: Criei uma aplicação modular em Python que atua como um facilitador fiscal. O sistema permite:

- Cadastro Simplificado: Armazenamento persistente de produtos em JSON.
- Inteligência Tributária: O sistema cruza automaticamente o produto com o regime tributário e a região de venda para determinar os impostos corretos.
- Resultado Imediato: Retorna todos os campos necessários para a emissão da NF, eliminando a necessidade de consulta manual a tabelas externas.

Vale ressaltar que foi pensado para **fins educacionais, avaliação técnica** e demonstração de automação.

> ⚠️ **Atenção:** Este projeto utiliza exemplos fictícios de alíquotas e regras fiscais, NÃO utilize para fins fiscais reais em produção. Consulte sempre um especialista tributário!

---

## 🚀 Visão Geral

Este projeto demonstra:
- Um fluxo completo para pequenas empresas/agro: **cadastre produtos** e depois **consulte os tributos necessários** para emitir NF-e de maneira prática.
- Modularidade: Cadastro e consulta estão desacoplados, podendo ser evoluídos separadamente.
- Interface 100% em Python de terminal, fácil de expandir e integrar.

---

## 📂 Estrutura do Projeto

```
├── main.py              # Menu principal (cadastro ou consulta de tributos para NF)
├── config.py            # Caminho dos arquivos/settings globais
├── data.py              # Funções de leitura/salvamento de dados JSON
├── interface.py         # Funções de UI/texto/input/output
├── dados.py             # Base de dados fiscal genérica/fictícia
├── cadastro_produtos.json  # Exemplo de base de produtos (podem ser criados pelo usuário)
```

---

## ✨ Funcionalidades

- Cadastro guiado de produtos (nome, categoria, NCM, preço, unidade, estoque, etc.)
- Geração automática de ID e data/hora de cadastro
- Consulta de produtos cadastrados já com estoque atualizado
- Seleção do regime tributário e da região de venda (simulando lógica real de nota fiscal)
- Cálculo e exibição dos dados fiscais (CFOP, CST, ICMS, IPI, PIS, COFINS) conforme a escolha
- Tudo salvo em `cadastro_produtos.json`, facilmente portável

---

## 📝 Como Usar

1. **Clone o repositório:**
    ```bash
    git clone https://github.com/seuusuario/cadastro-produtos-fiscal-demo.git
    cd cadastro-produtos-fiscal-demo
    ```

2. **(Opcional) Crie um ambiente virtual:**
    ```bash
    python -m venv .venv
    source .venv/bin/activate  # Unix/macOS
    .venv\Scripts\activate     # Windows
    ```

3. **Rode o sistema:**
    ```bash
    python main.py
    ```

4. **Siga o menu:**
    - `Cadastrar novo produto`: basta seguir as perguntas.
    - `Consultar tributos para Nota Fiscal`: escolha o produto, regime (Convênio 100/97 ou TTD 409) e destino.

5. **Exemplo de uso** (saída resumida):

    ```
    Bem-vindo ao Gerenciador de Produtos e Tributos Fiscais!
    1. Cadastrar novo produto
    2. Consultar tributos para Nota Fiscal
    3. Sair
    Escolha uma opção: 2

    Produtos disponíveis:
    1. Ureia Agrícola
        Categoria: Fertilizante
        Preço: R$ 1500,00 | Quantidade: 1000kg
        Descrição: Produto para uso agrícola

    Escolha o número do produto: 1
    Regime (1. Convênio 100/97 | 2. TTD 409): 1
    Venda (1. Interna SC | 2. Externa): 2
    Estado (PR, RS, MT, MS): PR

    ===== INFORMAÇÕES PARA SUA NOTA FISCAL =====
    [saída formatada]
    ```

---

## 📊 Exemplo de cadastro_produtos.json

```json
[
  {
    "id": 1,
    "nome": "Ureia Agrícola",
    "descricao": "Produto para uso agrícola",
    "preco": 1500.0,
    "categoria": "Fertilizante",
    "estoque": 1000,
    "unidade": "kg",
    "ncm": 31021010,
    "ativo": true,
    "data_cadastro": "01/12/2025 09:23"
  }
]
```

---

## 👤 Sobre o autor

Desenvolvido por [Edinor de Souza Neto](https://www.linkedin.com/in/edinor-de-souza-neto/)
Contato: edinorneto41@gmail.com

Se gostou do projeto, deixe uma estrela ⭐, contribua ou entre em contato!
