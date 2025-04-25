from robo_explorador import RoboExplorador
from relatorio_de_missao import RelatorioDeMissao

def main():
    # Cria um robô explorador
    robo = RoboExplorador("Curiosity", "Marte", 90)
    print(robo)

    # Cria um relatório de missão com leituras
    leituras = (("temperatura", -60), ("radiação", 3.2), ("pressão", 0.7))
    relatorio = RelatorioDeMissao("Curiosity", "Marte", 90, leituras)
    print("\nResumo das leituras:")
    for linha in relatorio.resumo():
        print(linha)
    print(f"\nTotal de leituras: {relatorio.contagem_leituras()}")

if __name__ == "__main__":
    main()
    