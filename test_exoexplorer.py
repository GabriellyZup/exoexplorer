
import pytest
from robo_explorador import RoboExplorador
from relatorio_de_missao import RelatorioDeMissao

def test_robo_explorador_str():
    robo = RoboExplorador("Xablau", "Marte", 87)
    assert str(robo) == "Robô Xablau - Destino: Marte - Energia: 87%"

def test_robo_explorador_energia_invalida():
    with pytest.raises(ValueError):
        RoboExplorador("Xablau", "Marte", 150)

def test_relatorio_de_missao_heranca():
    relatorio = RelatorioDeMissao("Xablau", "Marte", 87, (("temperatura", -50), ("radiação", 2.5)))
    assert isinstance(relatorio, RoboExplorador)

def test_relatorio_de_missao_resumo():
    leituras = (("temperatura", -50), ("radiação", 2.5))
    relatorio = RelatorioDeMissao("Xablau", "Marte", 87, leituras)
    assert relatorio.resumo() == ["temperatura: -50", "radiação: 2.5"]

def test_relatorio_de_missao_contagem_leituras():
    leituras = (("temperatura", -50), ("radiação", 2.5))
    relatorio = RelatorioDeMissao("Xablau", "Marte", 87, leituras)
    assert relatorio.contagem_leituras() == 2
    

