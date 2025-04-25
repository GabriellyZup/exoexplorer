class RoboExplorador:
    def __init__(self, nome: str, planeta_destino: str, energia: int):
        self.nome = nome
        self.planeta_destino = planeta_destino
        if not (0 <= energia <= 100):
            raise ValueError("Energia deve estar entre 0 e 100")
        self.energia = energia

    def __str__(self):
        return f"Robô {self.nome} - Destino: {self.planeta_destino} - Energia: {self.energia}%"
    