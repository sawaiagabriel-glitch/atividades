import pytest
from frete import calcular_frete


def test_frete_gratis_padrao():
    assert calcular_frete(
        valor_carrinho=250.0,
        regiao="Sudeste"
    ) == 0.0


def test_frete_gratis_regiao_norte():
    assert calcular_frete(
        valor_carrinho=300.0,
        regiao="Norte"
    ) == 0.0


def test_cobrar_taxa_abaixo_limite():
    assert calcular_frete(
        valor_carrinho=150.0,
        regiao="Sudeste"
    ) == 20.0


def test_valor_carrinho_invalido():
    with pytest.raises(
        ValueError,
        match="Valor de carrinho inválido"
    ):
        calcular_frete(
            valor_carrinho=0.0,
            regiao="Sudeste"
        )