# IT-Workshop: Spieleprogrammierung und Open Source/Datenschutz

**Ein praktischer Workshop für Jugendliche – mit Linux-VM, echten Tools und viel Raum zum Selberdenken.**  
Ziel ist es, Open Source & digitale Selbstbestimmung nicht nur zu erklären, sondern **selbst erlebbar zu machen**.


## Inhalt:

- **Folien/** → Präsentationsfolien (.pdf)
- **Ressourcen/** → Zusätzliche Materialien (für z.B. Hands-on) 
- **Beispiele/** → Einfache Code-Beispiele für HTML, CSS und JavaScript
- **Tutorials/** → Schritt-für-Schritt-Anleitungen zu Hands-on
- **projekt/** → Hier kommen dann eure Mini-Games rein
- **links.md** → Nützliche Links und Ressourcen
- **Artikel/** → Relevante Zeitungsartikel zu Open Source und Datenschutz

## Workshop-Ablauf:



### Teil 1: Open Source und Datenschutz

1. **Vortrag:** Was ist Open Source und warum ist Datenschutz wichtig?
2. **Diskussion:** Einblick in aktuelle Themen und weiterführende Ressourcen


### Teil 2: Spieleprogrammierung

1. **Einführung:** Grundlagen von HTML, CSS und JavaScript
2. **Live-Coding:** Gemeinsam programmieren wir ein einfaches Mini-Game
3. **Hands-on:** Du erstellst dein eigenes Mini-Game mit der Hilfe von Duck.AI
4. **Präsentation:** Zeige dein Spiel und teile deine Erfahrungen

## 🚀 Schnellstart

1. **Linux-VM starten**  
   Doppelklick auf die `start-vm.bat` → Die VM bootet automatisch in das vorbereitete Linux-System.

2. **Dieses Repo clonen**  
   ```bash
   git clone https://github.com/sheepfreak221/IT-Workshop
   ```
3. **Aufgaben öffnen**  
   In der VM findest du jetzt eine Ordnerstruktur mit Beschreibungen & Anleitungen für jede Hands-on-Station.


## Was ist drinnen?

In der VM befinden sich folgende Programme – alle Open Source, datenschutzfreundlich und bereit zur Benutzung:

| Kategorie        | Tools                                                                 |
|------------------|-----------------------------------------------------------------------|
| Web           | Firefox + uBlock Origin                                              |
| Passwort      | KeePassXC, `john` (John the Ripper)                                  |
| Verschlüsselung | VeraCrypt                                                    	  |
| Metadaten     | `exiftool`                            |
| Kommunikation | Pidgin + purple-facebook + OTR Plugin, Tor-Browser                   |
| CLI Tools     | `curl`, `git`, `john`, …      					 |
| Programmierung	| VS Code, Geany, Bluefish						|



Die VM basiert auf **Debian (Bookworm)** und verwendet die Desktopumgebung **LXQt** für eine einfache, ressourcenschonende Benutzeroberfläche.
Sie ist eine **amd64-VM**, die auf QEMU basiert und schnell auf fast jedem modernen Rechner laufen sollte. Um die VM auszuführen, stelle sicher, dass **Hyper-V** sowie **Intel VT-x** (für Intel-Prozessoren) oder **AMD-V** (für AMD-Prozessoren) auf deinem Computer aktiviert sind.


## Beispiel-Hands-on:

**EXIF & Geodaten:**  
Fotos mit GPS-Koordinaten analysieren und Orte auf OpenStreetMap finden.

**Passwörter knacken:**  
Eine verschlüsselte PDF mit John the Ripper analysieren und sehen, warum Wörterbuchpasswörter gefährlich sind.

**Sichere Passwortverwaltung:**  
Einführung in KeePassXC und warum man Passwörter nicht im Kopf behalten sollte.

**Tracker erkennen und blocken:**  
Mit uBlock Origin Tracker identifizieren und blockieren – sicher surfen leicht gemacht.

**Verschlüsselte Container mit VeraCrypt:**  
Partitionen verschlüsseln & versteckte Volumes verstehen.

**Messenger absichern:**  
Facebook-Chat in Pidgin via OTR – was geht, was nicht?

---

## Zielgruppe

- Jugendliche (ca. 15–18 Jahre)
- Interessierte ohne technische Vorkenntnisse
- Schulen, Jugendzentren, Hacking Spaces

---

## Motivation

Dieser Workshop wurde aus Frust über langweilige IT-Einheiten geboren – und aus der Liebe zu Open Source & echter Medienbildung.  
Er soll **nicht nur warnen**, sondern **ermächtigen**: zum Selberdenken, Selbermachen, Selberschützen.

---

## Lizenz

MIT – nimm, kopiere, teile, verbessere!  
Forks & Pull Requests sind absolut willkommen 💜

---

## Autor

[Sheepfreak221](https://github.com/sheepfreak221) – Nerd, Veganer, Security-Enthusiast, Katzenliebhaber, KI-Bastler & Linux forever

---

> *"Man schützt nicht, was man nicht versteht – und man versteht nichts, das man nicht selbst ausprobiert hat."*
