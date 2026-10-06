"""
PLANO (passo 1)
===============

Problema: calculadora de frete de uma loja virtual. O valor do frete depende
da modalidade de entrega escolhida pelo cliente e do peso do pedido (kg).

Casos que vou testar (três variações de comportamento):
  1. Frete PADRÃO   -> R$ 10,00 fixos + R$ 2,00 por kg.
  2. Frete EXPRESSO -> R$ 20,00 fixos + R$ 3,50 por kg.
  3. RETIRADA na loja -> sempre R$ 0,00, qualquer que seja o peso.
  Casos extras: peso negativo gera ValueError; modalidade desconhecida gera
  ValueError.

Padrão de projeto escolhido: Strategy.
  Por quê: cada modalidade de entrega é um algoritmo de cálculo diferente e
  intercambiável. Na fase verde o código naturalmente vira um if/elif por
  modalidade; com Strategy cada regra fica em sua própria classe, e adicionar
  uma nova modalidade (ex.: "agendada") não exige alterar a calculadora
  (princípio aberto/fechado).

Tempo planejado por fase (total 120 min):
  - Plano: 10 min
  - Red (escrever testes e vê-los falhar): 10 min
  - Green (implementação mais direta): 10 min
  - Refactor (aplicar Strategy): 60 min
  - Autoavaliação: 10 min
  - Folga/envio: 20 min

Uso de IA: usei o Claude Code para refatoração, e revisei cada fase antes de commitar.
"""

import pytest

from frete import calcular_frete


def test_frete_padrao_cobra_taxa_fixa_mais_dois_reais_por_kg():
    assert calcular_frete("padrao", 5) == pytest.approx(20.00)


def test_frete_expresso_cobra_taxa_fixa_mais_tres_e_cinquenta_por_kg():
    assert calcular_frete("expresso", 4) == pytest.approx(34.00)


def test_retirada_na_loja_e_gratuita_independente_do_peso():
    assert calcular_frete("retirada", 100) == pytest.approx(0.00)


def test_peso_negativo_e_rejeitado():
    with pytest.raises(ValueError):
        calcular_frete("padrao", -1)


def test_modalidade_desconhecida_e_rejeitada():
    with pytest.raises(ValueError):
        calcular_frete("teletransporte", 1)
