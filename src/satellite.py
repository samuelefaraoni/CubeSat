class Satellite:
    Sensori = {}

    def __init__(self, nome: str) -> None:
        self.nome = nome
        self.sensori = {}
        self.letture: list = []
