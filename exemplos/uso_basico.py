# -*- coding: utf-8 -*-
#
# Copyright (c) 2026 Edilson Aguiais — Licenca MIT
#
"""Exemplos minimos de uso do sgs-peritos (foco pericial: taxas de juros)."""

import sgs_peritos as sgs
from sgs_peritos import catalogo


def main() -> None:
    print("=== Taxas medias de juros - Pessoa Fisica ===")
    catalogo.listar("juros_pf")

    print("\n=== Credito pessoal NAO consignado PF (% a.m.) - ultimos 12 meses ===")
    print(sgs.get(catalogo.codigo("pf_pessoal_nao_consignado_mensal"), last=12))

    print("\n=== Comparativo consignado PF (mensal) - ultimo valor de cada ===")
    chaves = [k for k in catalogo.buscar("consignado") if k.endswith("_mensal")]
    codigos = {k.replace("pf_", "").replace("_mensal", ""): catalogo.codigo(k) for k in chaves}
    print(sgs.get(codigos, last=1))

    print("\n=== Aquisicao de veiculos PF: anual + mensal (2024 em diante) ===")
    print(
        sgs.get(
            {
                "veiculo_aa": catalogo.codigo("pf_veiculos_anual"),
                "veiculo_am": catalogo.codigo("pf_veiculos_mensal"),
            },
            start="2024-01-01",
        )
    )

    print("\n=== Indices macro (correcao monetaria) - ultimo valor ===")
    print(sgs.get(catalogo.codigo("ipca_12m"), last=1))


if __name__ == "__main__":
    main()
