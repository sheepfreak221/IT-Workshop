# QEMU VM Startskript

Dieses Skript startet eine QEMU-VM von einem USB-Stick oder einer anderen externen Quelle. Es verwendet Windows Hypervisor Platform (WHPX) zur Beschleunigung, falls verfügbar. Nachfolgend sind die wichtigsten Konfigurationsoptionen und Anpassungsmöglichkeiten beschrieben.

## Systemvoraussetzungen
- Windows 10 oder neuer mit aktivierter Windows Hypervisor Platform (WHPX)
- QEMU installiert im Verzeichnis `qemu` auf dem gleichen Laufwerk wie das Skript
- Eine vorhandene QEMU-VM-Datei `debian_vm.qcow2`
- Das Skript muss mit Administratorrechten ausgeführt werden
- Die VM ist eine `amd64` (x86_64)-VM und läuft nicht auf ARM-basierten Macs (Apple Silicon)

## WHPX in Windows Home-Versionen
Windows Home-Versionen unterstützen **WHPX** nicht. Falls du eine Windows Home-Version verwendest, kannst du stattdessen Software-Emulation wie `-accel tcg` verwenden, was jedoch deutlich langsamer ist. Wenn du auf eine der folgenden unterstützten Versionen von Windows umsteigst, kannst du die Hardwarebeschleunigung WHPX nutzen.

### Unterstützte Windows-Versionen für WHPX:
- **Windows 10 Pro** (ab Version 1809)
- **Windows 10 Enterprise** (ab Version 1809)
- **Windows 10 Education** (ab Version 1809)
- **Windows 11 Pro**
- **Windows 11 Enterprise**
- **Windows 11 Education**

Falls du eine der unterstützten Versionen verwendest, kannst du WHPX aktivieren, wie unten beschrieben.

## Anpassungen für Systeme ohne WHPX
Falls WHPX nicht verfügbar ist oder nicht aktiviert werden kann, muss die Option `-accel whpx` entfernt oder durch eine andere Beschleunigungsmethode ersetzt werden (z. B. `-accel hax` oder `-accel tcg` für Software-Emulation).

**Änderung in der Skriptzeile:**
qemu-system-x86_64.exe -hda "%SCRIPT_DRIVE%\debian_vm.qcow2" -m 2048 -smp cores=8 -net nic,model=virtio -net user -vga virtio -display sdl,gl=on, -rtc base=localtime -usb -device usb-tablet

## Einbinden eines USB-Sticks

Um einen USB-Stick in die VM einzubinden, sind folgende Schritte nötig:

### 1. Den USB-Stick identifizieren:
Öffne eine Eingabeaufforderung mit Administratorrechten und führe den folgenden Befehl aus:

wmic diskdrive list brief

Notiere dir den Namen des USB-Geräts, z. B. \.\PhysicalDrive2.

### 2. Das QEMU-Skript anpassen:
Ergänze die folgende Zeile in der `qemu-system-x86_64.exe`-Aufrufzeile:

-drive file=\\.\PhysicalDrive2,if=none,id=usbdrive -device usb-storage,drive=usbdrive

Ersetze `PhysicalDrive2` durch das tatsächliche Gerät aus Schritt 1.

### 3. Die VM starten und USB nutzen:
Starte die VM, der USB-Stick sollte nun in der VM verfügbar sein.

## Aktivierung von WHPX

WHPX kann mit folgendem Befehl in einer Administrator-Eingabeaufforderung aktiviert werden:

DISM /Online /Enable-Feature /FeatureName:HypervisorPlatform /All /NoRestart

Nach der Aktivierung ist ein Neustart erforderlich.

## Plattformkompatibilität

Das Skript ist für Windows ausgelegt, da es WHPX als Beschleunigung verwendet. Für Linux- oder macOS-Systeme kann stattdessen `-accel kvm` (Linux) oder `-accel hvf` (macOS) verwendet werden.

Wichtig: Diese VM basiert auf der `amd64`-Architektur (x86_64) und ist nicht mit Apple Silicon (M1, M2, M3) kompatibel. Auf diesen Geräten muss entweder eine ARM-kompatible VM verwendet oder eine x86_64-Emulation wie UTM mit qemu-x86_64 eingesetzt werden.

## Fehlerbehebung

- **QEMU nicht gefunden**: Stelle sicher, dass sich `qemu-system-x86_64.exe` im Verzeichnis `%SCRIPT_DRIVE%\qemu` befindet.
- **WHPX nicht verfügbar**: Prüfe mit `systeminfo`, ob Hyper-V aktiv ist und aktiviere es ggf. in den Windows-Features.
- **USB-Stick wird nicht erkannt**: Stelle sicher, dass der USB-Stick korrekt mit dem System verbunden ist und die richtige `PhysicalDrive`-Nummer verwendet wird.
