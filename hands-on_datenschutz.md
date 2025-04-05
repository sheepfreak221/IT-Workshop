# Praktische Datenschutz-Experimente für den Workshop  

## 1 Fake-Facebook-Account erstellen  
- Einen Fake-Account mit erfundenen Daten anlegen  
- Testen, welche Prüfungen Facebook durchführt (Handynummer, Gesichtserkennung etc.)  
- Beobachten, wie lange es dauert, bis der Account gesperrt wird  
- Quiz: „Welche Daten werden überprüft?“  

## 2 Webseiten-Tracking mit Blacklight analysieren  
- Lieblingsseiten mit [Blacklight](https://themarkup.org/blacklight) scannen  
- Herausfinden, welche Tracker & Fingerprinting-Methoden genutzt werden  
- Vorher/Nachher-Vergleich mit uBlock Origin oder Pi-hole  

## 3 Persönliche Daten bei Google & Facebook abrufen *(Alternative: Nur Datenschutz-Einstellungen checken!)*  
- **Google Takeout** nutzen, um gespeicherte Daten zu sehen *(wenn genug Zeit ist)*  
- **Facebook-Archiv** abrufen und auswerten  
- Alternative: **Nur die Datenschutz-Einstellungen checken!** (Was wird überhaupt gespeichert?)  
- Falls nichts gespeichert ist → Screenshots öffentlicher Beispiele nutzen  

## 4 Google Maps Zeitachse & Standort-Tracking prüfen  
- Alle schauen nach, ob ihre **Google Maps Zeitachse** ([Link](https://www.google.com/maps/timeline)) Standorte gespeichert hat  
- iPhone-Nutzer: **„Wichtige Orte“ unter Standortdienste** checken  
- Falls getrackt: Zeigen, wie man es deaktiviert  

## 5 Browser-Fingerprinting testen  
- Mit [amiunique.org](https://amiunique.org) oder [coveryourtracks.eff.org](https://coveryourtracks.eff.org) prüfen, wie einzigartig der eigene Browser ist  
- Verschiedene Browser & Einstellungen vergleichen (z. B. mit/ohne uBlock, Tor etc.)  

## 6 Metadaten aus Bildern auslesen & testen  
- Bild mit GPS-Daten erstellen  
- Metadaten mit **ExifTool** oder Online-Viewern auslesen  
- Test: Wird die Info entfernt, wenn man das Bild über …  
  - WhatsApp  
  - Telegram (normal vs. als Datei)  
  - Signal  
  - E-Mail  
  - Cloud-Dienste (Google Drive, Dropbox, etc.)  
  … verschickt?  

## 7 Reverse Image Search ausprobieren  
- Bilder über **Google Reverse Image Search** oder **Yandex** hochladen  
- Testen, ob sie irgendwo im Netz gefunden werden  
- Bewusstsein schaffen, dass gepostete Bilder oft rückverfolgbar sind  

## 8 Datenschutz-Fails in Social Media simulieren  
- Fake-Beiträge oder „harmlose“ Posts untersuchen  
- Welche Infos kann man daraus ableiten? (Standort, Gewohnheiten, Freunde …)
  
## 9 VPN & Tor vs. normales Surfen vergleichen  
- Unterschiedliche IP-Adressen testen (WhatIsMyIP, DNS-Leaks, WebRTC-Leaks)  
- Vergleich: Surfen mit und ohne VPN oder Tor  

## 10 Passwort-Sicherheit testen  
- Eigene Passwörter mit [haveibeenpwned.com](https://haveibeenpwned.com) prüfen  
- Passwort-Manager vs. wiederverwendete Passwörter erklären  
- Quiz: „Wie lange dauert es, dein Passwort zu knacken?“  

## 11. App-Tracker & Berechtigungen analysieren  

1. **Webseite aufrufen:**  
   [Exodus Privacy](https://exodus-privacy.eu.org/en/)  
   - App-Namen eingeben und Analyse laden.  

2. **Tracker prüfen:**  
   - Welche Tracker gibt es? (Analytics, Werbung, Identifikation)  
   - Welche findest du bedenklich?  

3. **Berechtigungen checken:**  
   - Welche Rechte fordert die App? (Kamera, Kontakte, Standort, etc.)  
   - Sind alle notwendig?  

4. **Reflexion:**  
   - Würdest du die App noch nutzen?  
   - Gibt es Alternativen?  
   - Wie kannst du deine Privatsphäre schützen?

## 12. Negativbeispiel: Facebook Messenger mit Pidgin absichern (nicht mehr möglich)

**Ziel:**  
Verstehen, wie Unternehmen APIs einschränken, um externe Clients zu blockieren, und welche Auswirkungen das auf Datenschutz-Tools hat.

**Hintergrund:**  
Bis zum 26. Februar 2025 konnte man sich mit Pidgin und dem Plugin *purple-facebook* über das XMPP-Protokoll mit dem Facebook Messenger verbinden.  
Zusätzlich konnte man mit *OTR (Off-the-Record Messaging)* und *Tor* für Anonymität und Ende-zu-Ende-Verschlüsselung sorgen.  

**Problem:**  
Facebook hat am 26. Februar 2025 die API abgeschaltet. Seitdem ist es nicht mehr möglich, sich über Drittanbieter-Clients mit dem Messenger zu verbinden.  
Das bedeutet, dass Datenschutzfreundliche Lösungen wie Pidgin + OTR + Tor für Facebook nicht mehr funktionieren.  

**Hands-on:**  
1. **Analyse des Problems**  
   - Versuche, dich mit Pidgin und *purple-facebook* anzumelden.  
   - Beobachte die Fehlermeldung.  
   - Überprüfe die API-Dokumentation von Meta, um zu sehen, welche Änderungen vorgenommen wurden.  

2. **Diskussion: Konsequenzen für die Nutzer**  
   - Warum sperrt Facebook externe Clients aus?  
   - Welche Alternativen gibt es?  
   - Welche Messenger respektieren Datenschutz und Interoperabilität?  

**Erkenntnis:**  
Big Tech schränkt offene Schnittstellen zunehmend ein, um Nutzer an ihre eigenen Apps zu binden und alternative Clients auszuschließen.  
Das erschwert datenschutzfreundliche Lösungen und zwingt Nutzer dazu, unsichere oder überwachende Plattformen zu verwenden.  

## 13. PDF-Passwort mit John the Ripper knacken (vergleich mit pdfcrack?)

### Ziel
Ein Passwort für eine PDF-Datei knacken.

### Durchführung
1. **John the Ripper installieren**: sudo apt update && sudo apt install build-essential git libssl-dev zlib1g-dev && git clone https://github.com/openwall/john.git && cd john/src && ./configure && make
2. **PDF-Hash extrahieren**: cd ../run && python3 ../tools/pdf2john.py deine_datei.pdf > hash.txt
3. **Passwort mit Passwortliste knacken**: ./john --format=pdf --wordlist=~/Downloads/german.txt hash.txt
4. **Ergebnisse überprüfen**: ./john --show hash.txt
5. **Brute-Force-Angriff (optional)**: ./john --format=pdf --incremental hash.txt

### Ergebnis
Das Passwort wurde erfolgreich geknackt.

## 14. Zugriff auf gesperrte Internetadressen

In diesem Hands-On werden wir versuchen, auf eine Reihe von gesperrten Internetadressen zuzugreifen. Die Teilnehmer sollen die folgenden Schritte durchführen:

### Schritt 1: Zugriff auf gesperrte Internetadressen

Versucht, die folgenden Internetadressen in eurem Browser aufzurufen:

- [kinox.to](http://kinox.to)
- [burningseries.to](http://burningseries.to)
- [de.rt.com](http://de.rt.com)
- [serienstream.to](http://serienstream.to)

Notiert euch, ob der Zugriff erfolgreich war oder ob eine Fehlermeldung angezeigt wird.

### Schritt 2: Zugriff über Tor

Jetzt werden wir versuchen, die gleichen Adressen über das Tor-Netzwerk aufzurufen. 

1. Ladet den [Tor Browser](https://www.torproject.org/download/) herunter und installiert ihn.
2. Öffnet den Tor Browser und gebt die oben genannten Adressen ein.
3. Notiert euch, ob der Zugriff erfolgreich war.

### Schritt 3: Zugriff über einen anderen DNS-Server

In diesem Schritt werden wir einen alternativen DNS-Server verwenden, um auf die gesperrten Adressen zuzugreifen. Wir werden Cloudflare's DNS-Server verwenden.

1. Ändert die DNS-Einstellungen eures Geräts auf die folgenden Werte:
   - Primärer DNS: `1.1.1.1`
   - Sekundärer DNS: `1.0.0.1`
   
   (Die genauen Schritte zum Ändern der DNS-Einstellungen hängen von eurem Betriebssystem ab. Bitte sucht nach Anleitungen für euer spezifisches System.)

2. Versucht erneut, die oben genannten Adressen in eurem Browser aufzurufen.
3. Notiert euch, ob der Zugriff erfolgreich war.

### Abschlussdiskussion

Diskutiert in der Gruppe, welche Methoden erfolgreich waren und welche nicht. Welche Herausforderungen habt ihr beim Zugriff auf die gesperrten Seiten erlebt?

## 15 Movie-Time!!! Ingrid Brodnig über TikTok  

### Wer ist Ingrid Brodnig?  
Ingrid Brodnig ist eine österreichische Journalistin und Publizistin. Sie verfasst eine regelmäßige Kolumne für die Tageszeitung *Der Standard* und setzt sich intensiv mit digitalen Themen auseinander – insbesondere mit Fake News, Algorithmen und Meinungsbildung im Netz.  

### Video: "Wien heute" über TikTok-Radikalisierung  
Die ORF-Sendung *Wien heute* spricht über den Selbstversuch der Satireplattform *Die Tagespresse*:  
**"Selbstversuch: So radikalisiert TikTok österreichische Teenager"**.  

#### Hands-on: Diskutiert folgende Fragen  
1. **Algorithmus und Radikalisierung:**  
   - Wie beeinflusst der TikTok-Algorithmus die Meinungsbildung?  
   - Welche Mechanismen führen dazu, dass extreme Inhalte verstärkt werden?  

2. **Echokammer & Filterblase:**  
   - Warum ist es problematisch, wenn Nutzer nur mehr einseitige Inhalte sehen?  
   - Welche Folgen kann das für die Gesellschaft haben?  

3. **Eigene Erfahrungen:**  
   - Habt ihr selbst schon erlebt, dass euch TikTok sehr ähnliche oder immer extremere Inhalte empfohlen hat?  
   - Welche Strategien gibt es, um aus einer Filterblase auszubrechen?  

### Fazit  
TikTok optimiert Inhalte für maximale Watchtime – mit potenziell gefährlichen Konsequenzen. Diskutiert, wie wir als Nutzer bewusster mit dem Algorithmus umgehen können.  

## 16 Bonus: Wer ist der beste Daten-Detektiv? 
- Challenge: In kleinen Gruppen bestimmte Infos über eine fiktive Person suchen  
- Testen, wie viel man aus öffentlichen Quellen herausfinden kann  

# Hands-on: Bilder strippen

In diesem Hands-on lernen wir, wie man Metadaten (Exif-Daten) aus Bildern ausliest und versteht, welche Informationen darin versteckt sein können. Besonders spannend sind GPS-Tags, die wir umrechnen und auf OpenStreetMap anzeigen lassen.

## Voraussetzungen
- Ein Debian-basiertes System (z. B. Ubuntu oder Debian selbst)
- `exiftool` installiert (falls noch nicht installiert, mit `sudo apt install libimage-exiftool-perl` nachholen)
- Beispielbilder mit Exif-Daten (werden bereitgestellt)

## Einführung
Digitalkameras und Smartphones speichern beim Fotografieren viele Informationen mit dem Bild, darunter:
- Kameramodell
- Aufnahmedatum und -zeit
- GPS-Koordinaten (falls aktiviert)
- Belichtungseinstellungen
- Software-Version

Diese Informationen sind hilfreich, können aber auch Datenschutzrisiken bergen.

## Teil 1: Exif-Daten auslesen
### 1.1 Metadaten eines Bildes anzeigen
Öffne ein Terminal und führe folgenden Befehl aus:
```sh
exiftool beispielbild.jpg
```
Dieser Befehl zeigt alle gespeicherten Metadaten des Bildes an.

### 1.2 Nur GPS-Informationen anzeigen
```sh
exiftool -gps* beispielbild.jpg
```
Falls GPS-Daten vorhanden sind, werden sie angezeigt, z. B.:
```
GPS Latitude                    : 48 deg 12' 34.56" N
GPS Longitude                   : 16 deg 22' 10.78" E
```

## Teil 2: GPS-Daten umrechnen und auf OpenStreetMap anzeigen
Falls ihr GPS-Koordinaten gefunden habt, müsst ihr sie in Dezimalgrad umwandeln.

### 2.1 Umrechnung in Dezimalgrad
Die Umrechnung erfolgt nach folgender Formel:
```
Grad + (Minuten / 60) + (Sekunden / 3600)
```
Beispiel:
```
48° 12' 34.56" N = 48 + (12 / 60) + (34.56 / 3600) = 48.2096°
16° 22' 10.78" E = 16 + (22 / 60) + (10.78 / 3600) = 16.3697°
```
Falls die Koordinate ein `S` oder `W` enthält, wird das Vorzeichen negativ:
- `N` → positiv
- `S` → negativ
- `E` → positiv
- `W` → negativ

### 2.2 OpenStreetMap aufrufen
Nachdem ihr die Dezimalwerte berechnet habt, könnt ihr die Koordinaten in OpenStreetMap aufrufen:

Öffnet einen Browser und gebt folgende URL ein:
```
https://www.openstreetmap.org/?mlat=48.2096&mlon=16.3697&zoom=15
```
Ersetzt die Werte entsprechend euren berechneten Koordinaten.

## Teil 3: Metadaten entfernen (Strippen)
Um Metadaten aus einem Bild zu entfernen, benutzt folgenden Befehl:
```sh
exiftool -all= -overwrite_original beispielbild.jpg
```
Dadurch werden sämtliche Metadaten gelöscht.

## Fazit
In diesem Hands-on habt ihr gelernt:
✅ Wie man Exif-Daten aus Bildern ausliest
✅ Wie man GPS-Daten in OpenStreetMap visualisiert
✅ Wie man Metadaten sicher entfernt

Jetzt seid ihr bereit, eure eigenen Bilder zu checken und zu entscheiden, welche Daten ihr behalten wollt! 🚀


