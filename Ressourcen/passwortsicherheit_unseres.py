# Definiere den Zeichensatz
zeichensatz_laenge = 94

# Funktion zur Berechnung der Anzahl der Kombinationen für jede Länge
def berechne_kombinationen(max_laenge):
    kombinationen = []
    for laenge in range(1, max_laenge + 1):
        anzahl = zeichensatz_laenge ** laenge
        kombinationen.append(anzahl)
    return kombinationen

# Funktion zur Berechnung der Zeit zum Knacken der Passwörter
def berechne_zeit(kombinationen, rate):
    zeiten = []
    for anzahl in kombinationen:
        zeit_in_sekunden = anzahl / rate
        zeiten.append(zeit_in_sekunden)
    return zeiten

# Funktion zur Ausgabe der Zeit in der sinnvollsten Einheit
def ausgabe_zeit(zeit):
    if zeit < 1:
        print(f"  Zeit zum Knacken: {zeit:.2f} Sekunden")
    elif zeit < 60:
        print(f"  Zeit zum Knacken: {zeit:.2f} Sekunden")
    elif zeit < 3600:  # weniger als 1 Stunde
        minuten = zeit / 60
        print(f"  Zeit zum Knacken: {minuten:.2f} Minuten")
    elif zeit < 86400:  # weniger als 1 Tag
        stunden = zeit / 3600
        print(f"  Zeit zum Knacken: {stunden:.2f} Stunden")
    elif zeit < 604800:  # weniger als 1 Woche
        tage = zeit / 86400
        print(f"  Zeit zum Knacken: {tage:.2f} Tage")
    elif zeit < 2629743:  # weniger als 1 Monat
        wochen = zeit / 604800
        print(f"  Zeit zum Knacken: {wochen:.2f} Wochen")
    elif zeit < 31556926:  # weniger als 1 Jahr
        monate = zeit / 2629743  # Durchschnittliche Tage pro Monat
        print(f"  Zeit zum Knacken: {monate:.2f} Monate")
    else:
        jahre = zeit / 31556926  # Durchschnittliche Tage pro Jahr
        print(f"  Zeit zum Knacken: {jahre:.2f} Jahre")

# Hauptprogramm
max_laenge = 22

# Rate für die CPU (1 Million Kombinationen pro Sekunde)
rate_cpu = 1_000_000  

# RTX 5090 (104.8 TFLOPS für FP32)
rate_rtx_5090 = 104_800_000_000_000  # 104.8 TFLOPS

# RX 6700 XT (13.21 TFLOPS für FP32)
rate_rx_6700_xt = 13_210_000_000_000  # 13.21 TFLOPS

# Berechnungen für Kombinationsanzahl und Zeit
anzahl_kombinationen = berechne_kombinationen(max_laenge)

# Berechne Zeit für CPU
zeiten_cpu = berechne_zeit(anzahl_kombinationen, rate_cpu)

# Berechne Zeit für RTX 5090
zeiten_rtx_5090 = berechne_zeit(anzahl_kombinationen, rate_rtx_5090)

# Berechne Zeit für RX 6700 XT
zeiten_rx_6700_xt = berechne_zeit(anzahl_kombinationen, rate_rx_6700_xt)

# Ausgabe der Anzahl der Kombinationen und der Zeit zum Knacken für CPU, RTX 5090 und RX 6700 XT
for laenge, (anzahl, zeit_cpu, zeit_rtx_5090, zeit_rx_6700_xt) in enumerate(zip(anzahl_kombinationen, zeiten_cpu, zeiten_rtx_5090, zeiten_rx_6700_xt), start=1):
    print(f"Länge {laenge}: {anzahl} Kombinationen")
    print("  CPU:")
    ausgabe_zeit(zeit_cpu)
    print("  RTX 5090:")
    ausgabe_zeit(zeit_rtx_5090)
    print("  RX 6700 XT:")
    ausgabe_zeit(zeit_rx_6700_xt)
    print()
