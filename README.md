# IT-Workshop: Spieleprogrammierung und Open Source/Datenschutz

**Ein praktischer Workshop für Jugendliche – mit Linux-VM, echten Tools und viel Raum zum Selberdenken.**  
Ziel ist es, Open Source & digitale Selbstbestimmung nicht nur zu erklären, sondern **selbst erlebbar zu machen**.


## Inhalt:

- **Folien/** → Präsentationsfolien (.pdf)
- **Ressourcen/** → Zusätzliche Materialien 
- **Beispiele/** → Einfache Code-Beispiele für HTML, CSS und JavaScript
- **Tutorials/** → Schritt-für-Schritt-Anleitungen zu Hands-on
- **Hands-on/** → Materialien für die Hands-on bzw. Challenges 
- **projekt/** → Hier kommen dann die Mini-Games rein
- **links.md** → Nützliche Links und Ressourcen
- **Artikel/** → Relevante Zeitungsartikel zu Open Source und Datenschutz

## Workshop-Ablauf:



### Teil 1: Open Source und Datenschutz (15. Mai 2025)

1. **Vortrag:** Was ist Open Source und warum ist Datenschutz wichtig?
2. **Diskussion:** Einblick in aktuelle Themen und weiterführende Ressourcen
3. **Hands-on:** Viele praxisnahe Aufgaben, die die Jugendlichen direkt umsetzen können!
4. **Challenges:** Spannende, vertiefte Herausforderungen, die den Jugendlichen helfen, das Gelernte weiter zu vertiefen und anzuwenden! 


### Teil 2: Spieleprogrammierung (20. Mai 2025)

1. **Einführung:** Grundlagen von HTML, CSS und JavaScript
2. **Live-Coding:** Gemeinsam programmieren wir mit den Jugendlichen ein einfaches Mini-Game
3. **Hands-on:** Die Jugendlichen erstellen ihr eigenes Mini-Game mit der Hilfe von Duck.AI
4. **Präsentation:** Sie zeigen ihr Spiel und teilen ihre Erfahrungen

## Schnellstart (Windows)

1. **Workshop-Dateien herunterladen**  
   [Download-Link (MEGA)](https://mega.nz/folder/0EQ2RSzT#Ie8U7hp3knUAkGeIW2k5sA)

2. **Linux-VM starten**  
   Doppelklick auf die `start-vm.bat` → Die VM bootet automatisch in das vorbereitete Linux-System.

3. **Dieses Repo clonen**  
   ```bash
   git clone https://github.com/sheepfreak221/IT-Workshop
   ```
4. **Aufgaben öffnen**
    In der VM befindet sich jetzt eine Ordnerstruktur mit Beschreibungen & Anleitungen für jede Hands-on-Station.

Die VM ist weit mehr als nur ein technisches Mittel – sie ist das Herzstück des Workshop-Konzepts. Sie bietet eine einheitliche, abgeschottete Umgebung, in der alle Jugendlichen mit exakt der gleichen, stabilen Konfiguration arbeiten. Das verhindert nicht nur typische „es-geht-bei-mir-nicht“-Probleme, sondern vermittelt ganz nebenbei echte IT-Kompetenzen: Umgang mit einem vollwertigen Linux-System, Terminal-Nutzung, Dateistrukturen verstehen – und das alles hands-on, statt nur in der Theorie.


## Was ist drinnen?

In der VM befinden sich folgende Programme – alle Open Source, datenschutzfreundlich und bereit zur Benutzung:

| Kategorie        | Tools                                                                 |
|------------------|-----------------------------------------------------------------------|
| Web           | Firefox + uBlock Origin                                              |
| Passwort      | KeePassXC, `john` (John the Ripper)                                  |
| Verschlüsselung | VeraCrypt                                                    	  |
| Metadaten     | `exiftool`                            |
| Kommunikation | Pidgin + purple-facebook + OTR Plugin, Tor-Browser                   |
| CLI Tools     | `curl`, `git`, …      					 |
| Programmierung	| VS Code, Geany, Bluefish						|



## Hinweise zur VM

Die VM basiert auf **Debian (Bookworm)** und verwendet die Desktopumgebung **LXQt** für eine einfache, ressourcenschonende Benutzeroberfläche.  
Sie ist eine **amd64-VM**, die auf **QEMU** basiert und schnell auf fast jedem modernen Rechner laufen sollte – vorausgesetzt, Virtualisierung ist verfügbar und korrekt eingerichtet.

### Voraussetzungen für den VM-Betrieb

#### Windows

- Unterstützte Windows-Versionen:
  - **Windows 10/11 Pro, Education oder Enterprise**  
    _(Windows Home wird **nicht** unterstützt, da WHPX nicht verfügbar ist)_

- Voraussetzungen:
  - **Hardware-Virtualisierung (VT-x oder AMD-V)** im BIOS/UEFI aktiviert
  - **Windows-Hypervisor-Plattform aktivieren**  
    Öffne PowerShell **als Administrator** und führe aus:
    ```powershell
    dism.exe /Online /Enable-Feature /FeatureName:HypervisorPlatform /All /NoRestart
    ```
    Danach PC neu starten.

#### Linux

- QEMU sollte mit KVM-Unterstützung laufen (Kernel-basierte Virtualisierung).
- Voraussetzungen:
  - **KVM-Modul geladen** (`kvm` und `kvm_amd` bzw. `kvm_intel`)
  - Der aktuelle Benutzer muss Mitglied der Gruppe `kvm` sein:
    ```bash
    sudo usermod -aG kvm $USER
    ```
  - Test mit:
    ```bash
    kvm-ok
    ```


#### macOS (nur Intel-Macs)

- Voraussetzungen:
  - **macOS Catalina (10.15)** oder neuer (empfohlen: Big Sur oder neuer)
  - Installation von QEMU über Homebrew:
    ```bash
    brew install qemu
    ```
  - Für Hardware-Beschleunigung nutzt QEMU auf Intel-Macs entweder **HVF (Hypervisor.framework)** oder das neue **Apple Virtualization Framework** (ab Big Sur).
    QEMU verwendet HVF automatisch, wenn verfügbar. Es ist vergleichbar mit KVM/WHPX.

  - Hinweis: Auf Apple-Silicon-Macs ist diese VM **nicht lauffähig**, da sie auf die amd64-Architektur angewiesen ist.

---


### VM Screenshot

![Screenshot der VM unter Windows 10 Professional](https://raw.githubusercontent.com/sheepfreak221/IT-Workshop/refs/heads/main/Ressourcen/VM_in_Aktion.PNG)

## Beispiel-Hands-on:

**EXIF & Geodaten:** 
Fotos von öffentlichen Flickr-Profilen analysieren – enthalten sie GPS-Koordinaten? Falls ja: Adresse via OpenStreetMap herausfinden. Ein realistisches Szenario, das zeigt, wie viel private Info in Bildern steckt.

**Passwortsicherheit:** 
Theorie trifft Praxis – Passwortcheckerseiten behaupten viel, aber wie sicher sind "sichere" Passwörter wirklich? Test mit einer verschlüsselten PDF und John the Ripper.

**Sichere Passwortverwaltung:** 
Einführung in KeePassXC – Warum Passwörter, die leicht zu merken sind, oft unsicher sind und wie Passwort-Manager wie KeePassXC helfen, starke Passwörter sicher zu verwalten.

**Tracker erkennen und blocken:** 
uBlock Origin in Aktion – Tracker identifizieren, blocken, Seiten sauber halten. Macht Webseiten schneller, schöner und privater.

**Verschlüsselte Container mit VeraCrypt:** 
Einen versteckten Container erstellen und darin eine KeePass-Datenbank ablegen. So funktioniert digitale Tarnung.

**Messenger absichern:** 
Facebook-Chat in Pidgin mit OTR verschlüsseln. Was funktioniert? Was nicht? Und warum?

## Challenges: 4 Missionen, 4 Packungen Schnitten, null Unterstützung – Let's hack!

### 1. VM-Check Challenge (Hidden!!!)

**Ziel:** Wer zuerst checkt, dass er in einer VM ist, gewinnt!

**Hinweis** Wenn sie kommen sind die VMs bereits gestartet und laufen im Vollbildmodus! Diese Challenge wird auch nicht erwähnt!

### 2. EXIF-Daten Stripping Challenge
**Ziel:** Wer zuerst alle Metadaten aus einem Bild entfernt, gewinnt! 

### 3. Zip-Archiv Knacken Challenge
**Ziel:** Wer zuerst das verschlüsselte Zip-Archiv knackt, gewinnt!


### 4. VeraCrypt-Verstecken Challenge
**Ziel:** Wer zuerst einen verschlüsselten VeraCrypt-Container in einem Video versteckt, gewinnt! 

---

### Belohnung:
**4 Packungen Manner Schnitten** warten auf die Sieger der Challenges!  Eine Packung pro Gewinner!

### Regeln:
- Keine direkte Hilfe von uns!
- Nur Duck.ai zur Unterstützung erlaubt!
- Die benötigten Programme sind teilweise **nicht installiert** und müssen von den Jugendlichen selbst über `apt` installiert werden! 

---

## Zielgruppe

- Jugendliche (ca. 15–18 Jahre)
- Interessierte ohne technische Vorkenntnisse
- Schulen, Jugendzentren, Hacking Spaces

---

## Motivation

Dieser Workshop wurde aus Frust über langweilige Informatik-Einheiten geboren – und aus der Liebe zu Open Source & echter Medienbildung.  
Er soll **nicht nur warnen**, sondern **ermächtigen**: zum Selberdenken, Selbermachen, Selberschützen.

---

## Lizenz

MIT – nimm, kopiere, teile, verbessere!  
Forks & Pull Requests sind absolut willkommen 💜

---

## Autor

[sheepfreak221](https://github.com/sheepfreak221) – Nerd, Veganer, Katzenliebhaber, FOSS-Enthusiast, Security-Junkie, KI-Bastler, Sci-Fi-Liebhaber, Metalhead, Horror Geek, AI Artist & Linux forever

---

> *"Man schützt nicht, was man nicht versteht – und man versteht nichts, das man nicht selbst ausprobiert hat."*
