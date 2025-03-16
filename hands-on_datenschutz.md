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


## 13 Bonus: Wer ist der beste Daten-Detektiv? 🕵️‍♀️  
- Challenge: In kleinen Gruppen bestimmte Infos über eine fiktive Person suchen  
- Testen, wie viel man aus öffentlichen Quellen herausfinden kann  
