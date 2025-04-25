from robo_explorador import RoboExplorador

class RelatorioDeMissao(RoboExplorador):
    def __init__(self, nome: str, planeta_destino: str, energia: int, leituras: tuple):
        super().__init__(nome, planeta_destino, energia)
        self.leituras = leituras

    def resumo(self):
        return [f"{tipo}: {valor}" for tipo, valor in self.leituras]

    def contagem_leituras(self):
        return len(self.leituras)
    