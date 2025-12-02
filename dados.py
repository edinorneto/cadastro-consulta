# tributos.py
# Módulo com base de dados tributários fictícios para qualquer produto.
# ATENÇÃO: Esta base é 100% FICTÍCIA e serve apenas para fins educacionais. NÃO use em produção real – tributos variam por lei, estado e empresa.
# As regras se aplicam a qualquer produto cadastrado (exemplo genérico para produtos agrícolas).

def obter_informacoes_tributarias(regime, regiao):
    """
    Obtém informações tributárias fictícias baseadas em regime e região.
    """
    base = {
        "ttd xx": {
            "SC": {
                "interna/sc": {

                    "CFOP": "5102 – Venda interna nacional",
                    "CST": "7 - Importada sem similar nacional",
                    "tributação do icms": "051",
                    "descricao": "Exemplo fictício de diferimento. Alíquotas zero para PIS/COFINS e IPI. Consulte legislação real.",
                    "icms": "5,0",
                    "ipi": "0",
                    "pis": "0",
                    "cofins": "0"
                },
                "externa/pr": {

                    "CFOP": "6102 – Venda interestadual nacional",
                    "CST": "7 - Importada sem similar nacional",
                    "tributação do icms": "051",
                    "descricao": "Exemplo fictício de diferimento. Alíquotas zero para PIS/COFINS e IPI. Consulte legislação real.",
                    "icms": "5,0",
                    "ipi": "0",
                    "pis": "0",
                    "cofins": "0"
                },
                "externa/rs": {

                    "CFOP": "6102 – Venda interestadual nacional",
                    "CST": "7 - Importada sem similar nacional",
                    "tributação do icms": "051",
                    "descricao": "Exemplo fictício de diferimento. Alíquotas zero para PIS/COFINS e IPI. Consulte legislação real.",
                    "icms": "5,0",
                    "ipi": "0",
                    "pis": "0",
                    "cofins": "0"
                },
                "externa/mt": {
                    
                    "CFOP": "6102 – Venda interestadual nacional",
                    "CST": "7 - Importada sem similar nacional",
                    "tributação do icms": "051",
                    "descricao": "Exemplo fictício de diferimento. Alíquotas zero para PIS/COFINS e IPI. Consulte legislação real.",
                    "icms": "5,0",
                    "ipi": "0",
                    "pis": "0",
                    "cofins": "0"
                },
                "externa/ms": {
                  
                    "CFOP": "6102 – Venda interestadual nacional",
                    "CST": "7 - Importada sem similar nacional",
                    "tributação do icms": "051",
                    "descricao": "Exemplo fictício de diferimento. Alíquotas zero para PIS/COFINS e IPI. Consulte legislação real.",
                    "icms": "5,0",
                    "ipi": "0",
                    "pis": "0",
                    "cofins": "0"
                }
            }
        },
        "convenio xx": {
            "SC": {
                "interna/sc": {
                   
                    "CFOP": "5102 – Venda interna nacional",
                    "CST": "7 - Importada sem similar nacional",
                    "tributação do icms": "040",
                    "descricao": "Exemplo fictício de isenção. Alíquotas zero para PIS/COFINS e IPI. Consulte legislação real.",
                    "icms": "0",
                    "ipi": "0",
                    "pis": "0",
                    "cofins": "0"
                },
                "externa/pr": {
                  
                    "CFOP": "6102 – Venda interestadual nacional",
                    "CST": "7 - Importada sem similar nacional",
                    "tributação do icms": "020",
                    "descricao": "Exemplo fictício de redução de base. Alíquotas zero para PIS/COFINS e IPI. Consulte legislação real.",
                    "icms": "6,0",
                    "ipi": "0",
                    "pis": "0",
                    "cofins": "0"
                },
                "externa/rs": {
                   
                    "CFOP": "6102 – Venda interestadual nacional",
                    "CST": "7 - Importada sem similar nacional",
                    "tributação do icms": "020",
                    "descricao": "Exemplo fictício de redução de base. Alíquotas zero para PIS/COFINS e IPI. Consulte legislação real.",
                    "icms": "6,0",
                    "ipi": "0",
                    "pis": "0",
                    "cofins": "0"
                },
                "externa/mt": {
                    
                    "CFOP": "6102 – Venda interestadual nacional",
                    "CST": "7 - Importada sem similar nacional",
                    "tributação do icms": "020",
                    "descricao": "Exemplo fictício de redução de base. Alíquotas zero para PIS/COFINS e IPI. Consulte legislação real.",
                    "icms": "6,0",
                    "ipi": "0",
                    "pis": "0",
                    "cofins": "0"
                },
                "externa/ms": {
                    
                    "CFOP": "6102 – Venda interestadual nacional",
                    "CST": "7 - Importada sem similar nacional",
                    "tributação do icms": "020",
                    "descricao": "Exemplo fictício de redução de base. Alíquotas zero para PIS/COFINS e IPI. Consulte legislação real.",
                    "icms": "6,0",
                    "ipi": "0",
                    "pis": "0",
                    "cofins": "0"
                }
            }
        }
    }

    try:
        return base[regime]["SC"][regiao]  
    except KeyError:
        print("Aviso: Combinação de regime/região não encontrada na base fictícia.")
        return {
            "descricao": "Informações tributárias não cadastradas para esta combinação (exemplo fictício).",
            "icms": "-",
            "ipi": "-",
            "pis": "-",
            "cofins": "-"
        }