# -*- coding: utf-8 -*-
#
# Catalogo de codigos SGS para pericia — curadoria
# Copyright (c) 2026 Edilson Aguiais — Licenca MIT
#
"""
Catalogo curado de codigos do SGS (Banco Central) para PERICIA.

O CORE deste catalogo sao as TAXAS MEDIAS DE JUROS POR MODALIDADE
(operacoes de credito com recursos livres). E o numero que o perito precisa
para recalcular um contrato pela media praticada pelo mercado — em vez de
aceitar a taxa pactuada/divulgada pela instituicao financeira.

Todos os codigos foram VALIDADOS em 05/06/2026 contra o catalogo OFICIAL de
dados abertos do BCB (campo ``title`` de
https://dadosabertos.bcb.gov.br/api/3/action/package_search?fq=codigo_sgs:{CODE})
e conferidos pela equivalencia ``(1 + mensal/100) ** 12 - 1 ≈ anual``.

Cada modalidade tem o par ANUAL (% a.a.) e MENSAL (% a.m.).

Como localizar/checar qualquer outro codigo:
  - Localizador oficial: https://www3.bcb.gov.br/sgspub/
  - Nome oficial da serie: o endpoint package_search acima
  - Ultimo valor: https://api.bcb.gov.br/dados/serie/bcdata.sgs.{CODE}/dados/ultimos/1?formato=json
"""

from __future__ import annotations

from typing import Dict, NamedTuple


class SerieInfo(NamedTuple):
    codigo: int
    descricao: str
    unidade: str       # "% a.a." | "% a.m." | "%" | "R$" | "% a.d."
    frequencia: str    # diaria | mensal | anual


# =====================================================================
#  TAXAS MEDIAS DE JUROS — PESSOA FISICA (o nucleo pericial)
#  Operacoes de credito com recursos livres. Par anual/mensal.
# =====================================================================
TAXAS_JUROS_PF: Dict[str, SerieInfo] = {
    "pf_total_anual": SerieInfo(20740, "PF - Total", "% a.a.", "mensal"),
    "pf_total_mensal": SerieInfo(25462, "PF - Total", "% a.m.", "mensal"),

    "pf_cheque_especial_anual": SerieInfo(20741, "PF - Cheque especial", "% a.a.", "mensal"),
    "pf_cheque_especial_mensal": SerieInfo(25463, "PF - Cheque especial", "% a.m.", "mensal"),

    "pf_pessoal_nao_consignado_anual": SerieInfo(20742, "PF - Credito pessoal nao consignado", "% a.a.", "mensal"),
    "pf_pessoal_nao_consignado_mensal": SerieInfo(25464, "PF - Credito pessoal nao consignado", "% a.m.", "mensal"),

    "pf_nao_consignado_composicao_dividas_anual": SerieInfo(20743, "PF - Nao consignado vinculado a composicao de dividas", "% a.a.", "mensal"),
    "pf_nao_consignado_composicao_dividas_mensal": SerieInfo(25465, "PF - Nao consignado vinculado a composicao de dividas", "% a.m.", "mensal"),

    "pf_consignado_privado_anual": SerieInfo(20744, "PF - Consignado setor privado (CLT)", "% a.a.", "mensal"),
    "pf_consignado_privado_mensal": SerieInfo(25466, "PF - Consignado setor privado (CLT)", "% a.m.", "mensal"),

    "pf_consignado_publico_anual": SerieInfo(20745, "PF - Consignado setor publico (servidor)", "% a.a.", "mensal"),
    "pf_consignado_publico_mensal": SerieInfo(25467, "PF - Consignado setor publico (servidor)", "% a.m.", "mensal"),

    "pf_consignado_inss_anual": SerieInfo(20746, "PF - Consignado INSS (aposentados e pensionistas)", "% a.a.", "mensal"),
    "pf_consignado_inss_mensal": SerieInfo(25468, "PF - Consignado INSS (aposentados e pensionistas)", "% a.m.", "mensal"),

    "pf_consignado_total_anual": SerieInfo(20747, "PF - Consignado total", "% a.a.", "mensal"),
    "pf_consignado_total_mensal": SerieInfo(25469, "PF - Consignado total", "% a.m.", "mensal"),

    "pf_pessoal_total_anual": SerieInfo(20748, "PF - Credito pessoal total (consignado + nao consignado)", "% a.a.", "mensal"),
    "pf_pessoal_total_mensal": SerieInfo(25470, "PF - Credito pessoal total (consignado + nao consignado)", "% a.m.", "mensal"),

    "pf_veiculos_anual": SerieInfo(20749, "PF - Aquisicao de veiculos", "% a.a.", "mensal"),
    "pf_veiculos_mensal": SerieInfo(25471, "PF - Aquisicao de veiculos", "% a.m.", "mensal"),

    "pf_outros_bens_anual": SerieInfo(20750, "PF - Aquisicao de outros bens", "% a.a.", "mensal"),
    "pf_outros_bens_mensal": SerieInfo(25472, "PF - Aquisicao de outros bens", "% a.m.", "mensal"),

    "pf_aquisicao_bens_total_anual": SerieInfo(20751, "PF - Aquisicao de bens total", "% a.a.", "mensal"),
    "pf_aquisicao_bens_total_mensal": SerieInfo(25473, "PF - Aquisicao de bens total", "% a.m.", "mensal"),

    "pf_leasing_veiculos_anual": SerieInfo(20752, "PF - Arrendamento mercantil de veiculos", "% a.a.", "mensal"),
    "pf_leasing_veiculos_mensal": SerieInfo(25474, "PF - Arrendamento mercantil de veiculos", "% a.m.", "mensal"),

    "pf_leasing_outros_bens_anual": SerieInfo(20753, "PF - Arrendamento mercantil de outros bens", "% a.a.", "mensal"),
    "pf_leasing_outros_bens_mensal": SerieInfo(25475, "PF - Arrendamento mercantil de outros bens", "% a.m.", "mensal"),

    "pf_leasing_total_anual": SerieInfo(20754, "PF - Arrendamento mercantil total", "% a.a.", "mensal"),
    "pf_leasing_total_mensal": SerieInfo(25476, "PF - Arrendamento mercantil total", "% a.m.", "mensal"),

    "pf_desconto_cheques_anual": SerieInfo(20755, "PF - Desconto de cheques", "% a.a.", "mensal"),
    "pf_desconto_cheques_mensal": SerieInfo(25480, "PF - Desconto de cheques", "% a.m.", "mensal"),

    "pf_cartao_rotativo_anual": SerieInfo(22022, "PF - Cartao de credito rotativo", "% a.a.", "mensal"),
    "pf_cartao_rotativo_mensal": SerieInfo(25477, "PF - Cartao de credito rotativo", "% a.m.", "mensal"),

    "pf_cartao_parcelado_anual": SerieInfo(22023, "PF - Cartao de credito parcelado", "% a.a.", "mensal"),
    "pf_cartao_parcelado_mensal": SerieInfo(25478, "PF - Cartao de credito parcelado", "% a.m.", "mensal"),

    "pf_cartao_total_anual": SerieInfo(22024, "PF - Cartao de credito total", "% a.a.", "mensal"),
    "pf_cartao_total_mensal": SerieInfo(25479, "PF - Cartao de credito total", "% a.m.", "mensal"),
}

# =====================================================================
#  TAXAS MEDIAS DE JUROS — PESSOA JURIDICA
# =====================================================================
TAXAS_JUROS_PJ: Dict[str, SerieInfo] = {
    "pj_total_anual": SerieInfo(20718, "PJ - Total", "% a.a.", "mensal"),
    "pj_total_mensal": SerieInfo(25437, "PJ - Total", "% a.m.", "mensal"),

    "pj_desconto_duplicatas_anual": SerieInfo(20719, "PJ - Desconto de duplicatas e recebiveis", "% a.a.", "mensal"),
    "pj_desconto_duplicatas_mensal": SerieInfo(25438, "PJ - Desconto de duplicatas e recebiveis", "% a.m.", "mensal"),

    "pj_desconto_cheques_anual": SerieInfo(20720, "PJ - Desconto de cheques", "% a.a.", "mensal"),
    "pj_desconto_cheques_mensal": SerieInfo(25439, "PJ - Desconto de cheques", "% a.m.", "mensal"),

    "pj_antecipacao_cartao_anual": SerieInfo(20721, "PJ - Antecipacao de faturas de cartao de credito", "% a.a.", "mensal"),
    "pj_antecipacao_cartao_mensal": SerieInfo(25440, "PJ - Antecipacao de faturas de cartao de credito", "% a.m.", "mensal"),

    "pj_capital_giro_ate_365_anual": SerieInfo(20722, "PJ - Capital de giro ate 365 dias", "% a.a.", "mensal"),
    "pj_capital_giro_ate_365_mensal": SerieInfo(25441, "PJ - Capital de giro ate 365 dias", "% a.m.", "mensal"),

    "pj_capital_giro_acima_365_anual": SerieInfo(20723, "PJ - Capital de giro acima de 365 dias", "% a.a.", "mensal"),
    "pj_capital_giro_acima_365_mensal": SerieInfo(25442, "PJ - Capital de giro acima de 365 dias", "% a.m.", "mensal"),

    "pj_capital_giro_rotativo_anual": SerieInfo(20724, "PJ - Capital de giro rotativo", "% a.a.", "mensal"),
    "pj_capital_giro_rotativo_mensal": SerieInfo(25443, "PJ - Capital de giro rotativo", "% a.m.", "mensal"),

    "pj_capital_giro_total_anual": SerieInfo(20725, "PJ - Capital de giro total", "% a.a.", "mensal"),
    "pj_capital_giro_total_mensal": SerieInfo(25444, "PJ - Capital de giro total", "% a.m.", "mensal"),

    "pj_conta_garantida_anual": SerieInfo(20726, "PJ - Conta garantida", "% a.a.", "mensal"),
    "pj_conta_garantida_mensal": SerieInfo(25445, "PJ - Conta garantida", "% a.m.", "mensal"),

    "pj_cheque_especial_anual": SerieInfo(20727, "PJ - Cheque especial", "% a.a.", "mensal"),
    "pj_cheque_especial_mensal": SerieInfo(25446, "PJ - Cheque especial", "% a.m.", "mensal"),

    "pj_veiculos_anual": SerieInfo(20728, "PJ - Aquisicao de veiculos", "% a.a.", "mensal"),
    "pj_veiculos_mensal": SerieInfo(25447, "PJ - Aquisicao de veiculos", "% a.m.", "mensal"),

    "pj_outros_bens_anual": SerieInfo(20729, "PJ - Aquisicao de outros bens", "% a.a.", "mensal"),
    "pj_outros_bens_mensal": SerieInfo(25448, "PJ - Aquisicao de outros bens", "% a.m.", "mensal"),

    "pj_aquisicao_bens_total_anual": SerieInfo(20730, "PJ - Aquisicao de bens total", "% a.a.", "mensal"),
    "pj_aquisicao_bens_total_mensal": SerieInfo(25449, "PJ - Aquisicao de bens total", "% a.m.", "mensal"),

    "pj_leasing_veiculos_anual": SerieInfo(20731, "PJ - Arrendamento mercantil de veiculos", "% a.a.", "mensal"),
    "pj_leasing_veiculos_mensal": SerieInfo(25450, "PJ - Arrendamento mercantil de veiculos", "% a.m.", "mensal"),

    "pj_leasing_outros_bens_anual": SerieInfo(20732, "PJ - Arrendamento mercantil de outros bens", "% a.a.", "mensal"),
    "pj_leasing_outros_bens_mensal": SerieInfo(25451, "PJ - Arrendamento mercantil de outros bens", "% a.m.", "mensal"),

    "pj_leasing_total_anual": SerieInfo(20733, "PJ - Arrendamento mercantil total", "% a.a.", "mensal"),
    "pj_leasing_total_mensal": SerieInfo(25452, "PJ - Arrendamento mercantil total", "% a.m.", "mensal"),

    "pj_vendor_anual": SerieInfo(20734, "PJ - Vendor", "% a.a.", "mensal"),
    "pj_vendor_mensal": SerieInfo(25453, "PJ - Vendor", "% a.m.", "mensal"),

    "pj_compror_anual": SerieInfo(20735, "PJ - Compror", "% a.a.", "mensal"),
    "pj_compror_mensal": SerieInfo(25454, "PJ - Compror", "% a.m.", "mensal"),

    "pj_acc_anual": SerieInfo(20736, "PJ - Adiantamento sobre contratos de cambio (ACC)", "% a.a.", "mensal"),
    "pj_acc_mensal": SerieInfo(25458, "PJ - Adiantamento sobre contratos de cambio (ACC)", "% a.m.", "mensal"),

    "pj_financ_importacoes_anual": SerieInfo(20737, "PJ - Financiamento a importacoes", "% a.a.", "mensal"),
    "pj_financ_importacoes_mensal": SerieInfo(25459, "PJ - Financiamento a importacoes", "% a.m.", "mensal"),

    "pj_financ_exportacoes_anual": SerieInfo(20738, "PJ - Financiamento a exportacoes", "% a.a.", "mensal"),
    "pj_financ_exportacoes_mensal": SerieInfo(25460, "PJ - Financiamento a exportacoes", "% a.m.", "mensal"),

    "pj_repasse_externo_anual": SerieInfo(20739, "PJ - Repasse externo", "% a.a.", "mensal"),
    "pj_repasse_externo_mensal": SerieInfo(25461, "PJ - Repasse externo", "% a.m.", "mensal"),

    "pj_cartao_rotativo_anual": SerieInfo(22019, "PJ - Cartao de credito rotativo", "% a.a.", "mensal"),
    "pj_cartao_rotativo_mensal": SerieInfo(25455, "PJ - Cartao de credito rotativo", "% a.m.", "mensal"),

    "pj_cartao_parcelado_anual": SerieInfo(22020, "PJ - Cartao de credito parcelado", "% a.a.", "mensal"),
    "pj_cartao_parcelado_mensal": SerieInfo(25456, "PJ - Cartao de credito parcelado", "% a.m.", "mensal"),

    "pj_cartao_total_anual": SerieInfo(22021, "PJ - Cartao de credito total", "% a.a.", "mensal"),
    "pj_cartao_total_mensal": SerieInfo(25457, "PJ - Cartao de credito total", "% a.m.", "mensal"),
}

# Taxa media geral (todas as operacoes com recursos livres)
TAXAS_JUROS_GERAL: Dict[str, SerieInfo] = {
    "geral_total_anual": SerieInfo(20717, "Total geral (recursos livres)", "% a.a.", "mensal"),
    "geral_total_mensal": SerieInfo(25436, "Total geral (recursos livres)", "% a.m.", "mensal"),
}

# =====================================================================
#  INDICES E TAXAS MACRO (correcao monetaria / referencia)
# =====================================================================
INDICES_MACRO: Dict[str, SerieInfo] = {
    "selic_meta": SerieInfo(432, "Meta Selic definida pelo Copom", "% a.a.", "diaria"),
    "selic_diaria": SerieInfo(11, "Taxa Selic diaria", "% a.d.", "diaria"),
    "selic_mes_anualizada": SerieInfo(4189, "Selic acumulada no mes anualizada (base 252)", "% a.a.", "mensal"),
    "selic_acum_mes": SerieInfo(4390, "Selic acumulada no mes", "% a.m.", "mensal"),
    "cdi_diaria": SerieInfo(12, "Taxa CDI diaria", "% a.d.", "diaria"),
    "cdi_acum_mes": SerieInfo(4391, "CDI acumulada no mes", "% a.m.", "mensal"),
    "ipca_mensal": SerieInfo(433, "IPCA - variacao mensal", "%", "mensal"),
    "ipca_12m": SerieInfo(13522, "IPCA - acumulado em 12 meses", "%", "mensal"),
    "inpc_mensal": SerieInfo(188, "INPC - variacao mensal", "%", "mensal"),
    "igpm_mensal": SerieInfo(189, "IGP-M - variacao mensal", "%", "mensal"),
    "dolar_ptax_compra": SerieInfo(1, "Dolar dos EUA (PTAX) - compra", "R$", "diaria"),
}

# Catalogo completo (uniao de todos os grupos)
CATALOGO: Dict[str, SerieInfo] = {
    **TAXAS_JUROS_GERAL,
    **TAXAS_JUROS_PF,
    **TAXAS_JUROS_PJ,
    **INDICES_MACRO,
}

GRUPOS: Dict[str, Dict[str, SerieInfo]] = {
    "juros_geral": TAXAS_JUROS_GERAL,
    "juros_pf": TAXAS_JUROS_PF,
    "juros_pj": TAXAS_JUROS_PJ,
    "indices_macro": INDICES_MACRO,
}


def codigo(chave: str) -> int:
    """Retorna o codigo SGS a partir da chave do catalogo.

    >>> from sgs_peritos import catalogo
    >>> catalogo.codigo("pf_veiculos_mensal")
    25471
    """
    return CATALOGO[chave].codigo


def buscar(termo: str) -> Dict[str, SerieInfo]:
    """Busca chaves cuja descricao contenha ``termo`` (case-insensitive).

    >>> catalogo.buscar("consignado")   # todas as modalidades de consignado
    """
    t = termo.lower()
    return {k: v for k, v in CATALOGO.items() if t in v.descricao.lower()}


def listar(grupo: str | None = None) -> None:
    """Imprime o catalogo (ou um grupo) formatado.

    grupo: ``juros_geral`` | ``juros_pf`` | ``juros_pj`` | ``indices_macro``
    (None imprime tudo).
    """
    fonte = CATALOGO if grupo is None else GRUPOS[grupo]
    largura = max(len(k) for k in fonte)
    for chave, info in fonte.items():
        print(
            f"{chave:<{largura}}  {info.codigo:>6}  "
            f"{info.descricao} ({info.unidade})"
        )
