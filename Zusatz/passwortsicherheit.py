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
 

rate = 1_000_000  # Anzahl der Kombinationen pro Sekunde (1 Million)
 


 

anzahl_kombinationen = berechne_kombinationen(max_laenge)
 

zeiten = berechne_zeit(anzahl_kombinationen, rate)
 


 

# Ausgabe der Anzahl der Kombinationen und der Zeit zum Knacken
 

for laenge, (anzahl, zeit) in enumerate(zip(anzahl_kombinationen, zeiten), start=1):
 

    print(f"Länge {laenge}: {anzahl} Kombinationen")
 

    ausgabe_zeit(zeit)
 

    print()
