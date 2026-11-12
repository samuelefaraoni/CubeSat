class Satellite:
    Sensori = {}

    def __init__(self, nome: str) -> None:
        self.nome = nome
        self.sensori = {}
        self.letture: list = []

    def aggiungi_sensore(self, sensore: Sensore) -> None:
        if sensore.codice in self.sensori:
            raise ValueError("Sensore gia presente")
        self.sensori[sensore.codice] = sensore
    
    def registra_lettura(self, codice_sensore: str, valore: float) -> None:
        if codice_sensore not in self.sensori:
            raise KeyError("Sensore non registrato")
    
        sensore = self.sensori[codice_sensore]
        self.letture.append({
            "sensore": codice_sensore,
            "grandezza": sensore.grandezza,
            "valore": valore,
            "unita": sensore.unità
        })

    def letture_in_allarme(self) -> list:
        allarmi: list = []
        
        for lettura in self.letture:
            if lettura["allarme"]:
                allarmi.append(lettura)
        
        return allarmi

    def riepilogo(self) -> None:
        print("Telemetria satellite:", self.nome)
        
        for lettura in self.letture:
            stato = "ALLARME" if lettura["allarme"] else "OK"
            print(lettura["sensore"], lettura["valore"], lettura["unita"], stato)