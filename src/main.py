from sensore import Sensore
from satellite import Satellite


def main() -> None:
    satellite = Satellite("CubeSat Aurora")
    satellite.aggiungi_sensore(Sensore("TEMP01", "temperatura", "C", 45))
    satellite.aggiungi_sensore(Sensore("BAT01", "tensione batteria", "V", 8.4))
    satellite.aggiungi_sensore(Sensore("GYR01", "velocita angolare", "deg/s", 12))
    satellite.aggiungi_sensore(Sensore("ALT01", "altitudine", "km", 1000))

    satellite.registra_lettura("TEMP01", 31.5)
    satellite.registra_lettura("TEMP01", 45.0)
    satellite.registra_lettura("BAT01", 8.6)
    satellite.registra_lettura("GYR01", 4.2)
    satellite.registra_lettura("ALT01", 1000.1)
    satellite.riepilogo()
    print("Letture in allarme:", satellite.letture_in_allarme())

    try:
        satellite.registra_lettura("GPS-99", 1.0)
    except KeyError as errore:
        print(errore)


if __name__ == "__main__":
    main()