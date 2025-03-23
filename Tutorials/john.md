# Anleitung zum Knacken eines PDF-Passworts mit John the Ripper (Windows)

## Schritt 1: John the Ripper herunterladen und installieren

1. **John the Ripper herunterladen**:
   - Gehe zur [John the Ripper-Website](https://www.openwall.com/john/) und lade die neueste Version für Windows herunter. Du kannst die "Community Enhanced" Version verwenden, die oft die neuesten Funktionen enthält.

2. **Entpacken**:
   - Entpacke die heruntergeladene ZIP-Datei in ein Verzeichnis deiner Wahl, z. B. `C:\John`.

## Schritt 2: Python und erforderliche Pakete installieren

1. **Python installieren** (falls noch nicht installiert):
   - Lade Python von der [offiziellen Website](https://www.python.org/downloads/) herunter und installiere es. Achte darauf, die Option "Add Python to PATH" während der Installation auszuwählen.

2. **Benötigte Pakete installieren**:
   - Öffne die Eingabeaufforderung (cmd) und installiere die benötigten Pakete mit `pip`:
     ```bash
     pip install pyhanko==0.20.1
     ```

## Schritt 3: PDF-Datei vorbereiten

1. **PDF-Datei**: Stelle sicher, dass du die PDF-Datei, deren Passwort du knacken möchtest, zur Hand hast.

## Schritt 4: PDF-Hash mit `pdf2john.py` extrahieren

1. **`pdf2john.py` verwenden**:
   - Navigiere zu dem Verzeichnis, in dem du John the Ripper entpackt hast:
     ```bash
     cd C:\John\run
     ```
   - Führe das Skript `pdf2john.py` aus, um den Hash der PDF-Datei zu extrahieren:
     ```bash
     python pdf2john.py "C:\Pfad\zu\deiner\datei.pdf" > hash.txt
     ```
   - Ersetze `C:\Pfad\zu\deiner\datei.pdf` durch den tatsächlichen Pfad zu deiner PDF-Datei.

## Schritt 5: Passwort mit John the Ripper knacken

1. **John the Ripper starten**:
   - In der Eingabeaufforderung, während du im `run`-Verzeichnis bist, führe den folgenden Befehl aus, um das Passwort zu knacken:
     ```bash
     john --format=pdf hash.txt
     ```

2. **Fortschritt überwachen**:
   - John the Ripper wird nun versuchen, das Passwort zu knacken. Du kannst den Fortschritt in der Eingabeaufforderung sehen.

## Schritt 6: Geknacktes Passwort anzeigen

1. **Passwort anzeigen**:
   - Wenn John das Passwort erfolgreich geknackt hat, kannst du es mit folgendem Befehl anzeigen:
     ```bash
     john --show --format=pdf hash.txt
     ```

## Schritt 7: Sicheres Entfernen

- Wenn du mit dem Knacken des Passworts fertig bist, schließe die Eingabeaufforderung.

## Hinweis

- Achte darauf, dass du nur Passwörter von PDF-Dateien knacken darfst, für die du die Erlaubnis hast. Das Knacken von Passwörtern ohne Erlaubnis ist illegal und unethisch.
- Die Geschwindigkeit, mit der John das Passwort knackt, hängt von der Komplexität des Passworts und der Leistung deines Systems ab.
