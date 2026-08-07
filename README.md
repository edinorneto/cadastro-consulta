# 💼 Cadastro de Produtos + Consulta Fiscal para NF-e

> **⚠️ Aviso:** Este projeto utiliza dados e regras fiscais **fictícias**, criados exclusivamente para fins de aprendizado e portfólio. Não utilize para fins fiscais reais. Consulte sempre um especialista tributário.

---

## 🔗 Contexto: Ponto de Partida de uma Série de Projetos

Este é o **projeto original** de uma série de soluções para o domínio fiscal. Após desenvolvê-lo como aplicação de terminal em Python, o mesmo domínio de negócio foi **evoluído e reimaginado** como aplicação web em PHP, com arquitetura multi-arquivo, CRUD completo e interface visual:

👉 **[tax-rule-php](https://github.com/edinorneto/tax-rule-php)** — versão web com CRUD completo e design system

Essa progressão demonstra a evolução de uma solução funcional de terminal para uma aplicação web com maior separação de responsabilidades e interface para o usuário.

---

## 💡 O Problema

No ambiente corporativo, preencher dados tributários em notas fiscais exige consultar regras específicas por regime e região, memorizar códigos (NCM, CFOP, CST) e calcular alíquotas manualmente — um processo sujeito a erros que interrompe o fluxo de trabalho da equipe.

## ✅ A Solução

Aplicação modular em Python que atua como facilitador fiscal via terminal:

- **Cadastro persistente** de produtos em JSON
- **Inteligência tributária:** cruza produto × regime × região para retornar dados fiscais corretos
- **Resultado imediato:** retorna CFOP, CST, ICMS, IPI, PIS e COFINS sem consulta manual a tabelas externas

---

## 🗂️ Arquitetura

```
├── main.py                   # Menu principal — ponto de entrada da aplicação
├── config.py                 # Constantes e caminhos globais
├── data.py                   # Funções de leitura/escrita em JSON — camada de dados isolada
├── dados.py                  # Base de dados fiscal fictícia (regimes × regiões × alíquotas)
├── interface.py              # Funções de UI: menus, inputs e outputs formatados
└── cadastro_produtos.json    # Persistência dos produtos cadastrados (gerado automaticamente)
```

**Decisão de design:** separação explícita entre a camada de dados (`data.py`), as regras de negócio (`dados.py`) e a interface (`interface.py`) — a mesma lógica de separação de responsabilidades foi evoluída e formalizada na versão PHP.

---

## 🛠 Tech Stack

- **Python 3.x**
- **JSON** — persistência de dados
- **Git & GitHub** — versionamento

---

## ✨ Funcionalidades

- Cadastro guiado de produtos (nome, categoria, NCM, preço, unidade, estoque, status ativo/inativo)
- Geração automática de ID sequencial e timestamp de cadastro
- Consulta fiscal por produto × regime tributário × região de destino
- Retorno estruturado: CFOP, CST, código de tributação, ICMS, IPI, PIS, COFINS
- Dados persistidos em JSON — portáveis e consultáveis sem banco de dados

---

## 🚀 Como Usar

```bash
git clone https://github.com/edinorneto/cadastro-consulta.git
cd cadastro-consulta
python main.py
```

**Exemplo de fluxo:**

```
Bem-vindo ao Gerenciador de Produtos e Tributos Fiscais!
1. Cadastrar novo produto
2. Consultar tributos para Nota Fiscal
3. Sair

Escolha uma opção: 2

Produtos disponíveis:
1. Ureia Agrícola | Fertilizante | R$ 1500,00 | 1000 kg

Escolha o produto: 1
Regime (1. Convênio 100/97 | 2. TTD 409): 1
Venda (1. Interna SC | 2. Externa): 2
Estado (PR, RS, MT, MS): PR

===== INFORMAÇÕES PARA SUA NOTA FISCAL =====
CFOP:  6102 – Venda interestadual nacional
CST:   7 – Importada sem similar nacional
ICMS:  6,0%  |  IPI: 0%  |  PIS: 0%  |  COFINS: 0%
```

---

## 📊 Exemplo de `cadastro_produtos.json`

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

## 🧠 Conceitos Aplicados

`Python 3.x` · `CLI Design` · `Modularização` · `Separação de responsabilidades` · `Persistência JSON` · `Regras de negócio fiscal` · `Git & GitHub`

---

## 👤 Autor

**Edinor de Souza Neto**
[LinkedIn](https://www.linkedin.com/in/edinor-de-souza-neto/) · [GitHub](https://github.com/edinorneto)

Se gostou do projeto, deixe uma ⭐ — e veja a evolução dele em [tax-rule-php](https://github.com/edinorneto/tax-rule-php)!
