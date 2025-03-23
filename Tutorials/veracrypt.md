# Anleitung zur Verschlüsselung einer Partition auf einem USB-Stick mit VeraCrypt (Windows)

## Schritt 1: USB-Stick vorbereiten

1. **USB-Stick anschließen**: Stecke deinen USB-Stick in den Computer.

2. **Datenträgerverwaltung öffnen**:
   - Drücke `Windows + R`, um das Ausführen-Fenster zu öffnen.
   - Gib `diskmgmt.msc` ein und drücke `Enter`, um die Datenträgerverwaltung zu öffnen.

## Schritt 2: USB-Stick partitionieren

1. **USB-Stick identifizieren**: Finde deinen USB-Stick in der Liste der Datenträger. Achte darauf, dass du den richtigen Datenträger auswählst.

2. **Partitionen erstellen**:
   - **Verschlüsselte Partition**:
     - Klicke mit der rechten Maustaste auf den nicht zugewiesenen Speicherplatz oder auf die Partition des USB-Sticks und wähle `Volume erstellen`.
     - Wähle `Primäres Volume` und klicke auf `Weiter`.
     - Setze die Größe auf 256 MB und klicke auf `Weiter`.
     - Wähle ein Dateisystem (z. B. `FAT32`) und klicke auf `Fertigstellen`.
   - **Unverschlüsselte Partition**:
     - Klicke mit der rechten Maustaste auf den verbleibenden nicht zugewiesenen Speicherplatz und wähle `Volume erstellen`.
     - Wähle `Primäres Volume` und klicke auf `Weiter`.
     - Setze die Größe für die unverschlüsselte Partition und wähle ein Dateisystem (z. B. `FAT32`) und klicke auf `Fertigstellen`.

## Schritt 3: VeraCrypt installieren

1. **VeraCrypt herunterladen**:
   - Gehe zur [VeraCrypt-Website](https://www.veracrypt.fr/en/Downloads.html) und lade die neueste Version herunter.

2. **VeraCrypt installieren**:
   - Führe die heruntergeladene Datei aus und folge den Installationsanweisungen.

## Schritt 4: Verschlüsselte Partition erstellen

1. **VeraCrypt starten**:
   - Öffne VeraCrypt.

2. **Neue verschlüsselte Partition erstellen**:
   - Klicke auf `Create Volume`.
   - Wähle `Encrypt a non-system partition/drive` und klicke auf `Next`.

3. **Partition auswählen**:
   - Wähle `Standard VeraCrypt volume` und klicke auf `Next`.
   - Wähle die 256 MB Partition aus, die du zuvor erstellt hast.

4. **Verschlüsselungseinstellungen**:
   - Wähle die gewünschten Verschlüsselungs- und Hash-Algorithmen (Standard ist in der Regel ausreichend) und klicke auf `Next`.

5. **Passwort festlegen**:
   - Gib ein sicheres Passwort für die Verschlüsselung ein und klicke auf `Next`.

6. **Formatierung**:
   - Wähle das Dateisystem (z. B. `FAT` oder `exFAT`) und klicke auf `Format`.

7. **Volume erstellen**: Warte, bis der Vorgang abgeschlossen ist, und klicke auf `Exit`.

## Schritt 5: Zugriff auf die verschlüsselte Partition

1. **VeraCrypt starten**.
2. **Volume einbinden**:
   - Wähle die verschlüsselte Partition aus und klicke auf `Mount`.
   - Gib das Passwort ein, wenn du dazu aufgefordert wirst.

3. **Zugriff auf die verschlüsselte Partition**: Die verschlüsselte Partition wird nun als Laufwerk im Datei-Explorer angezeigt.

## Schritt 6: Sicheres Entfernen

- Wenn du mit der Arbeit auf der verschlüsselten Partition fertig bist, stelle sicher, dass du sie in VeraCrypt aushängst, bevor du den USB-Stick sicher entfernst.

## Hinweis

- Achte darauf, dass du das Passwort für die verschlüsselte Partition sicher aufbewahrst. Wenn du das Passwort vergisst, kannst du nicht mehr auf die Daten zugreifen.
- Die unverschlüsselte Partition ist für jeden zugänglich, der den USB-Stick hat. Stelle sicher, dass du keine sensiblen Daten dort speicherst.
