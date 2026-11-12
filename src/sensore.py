class Sensore:
    def __init__(self, codice: str, grandezza: str, unita: str, soglia_massima: float) -> None:
        self.codice = codice
        self.grandezza = grandezza
        self.unita = unita
        self.sogliaMassima = soglia_massima

    def __str__(self) -> str:
        return f"Codice: {self.codice}. Grandezza: {self.grandezza}. Unità: {self.unita}. Soglia massima: {self.sogliaMassima}"
