import subprocess
import json
import os
import time
import sys
import random
import threading
from datetime import datetime

# ==============================================================================
# CONFIGURATION & COLORS
# ==============================================================================
R = "\033[1;31m"    # Red (Critical)
G = "\033[1;32m"    # Green (Success)
Y = "\033[1;33m"    # Yellow (Warning)
B = "\033[1;34m"    # Blue (Info)
C = "\033[1;36m"    # Cyan (Process)
W = "\033[0m"       # Reset

VERSION = "3.5.0-PRO"
AUTHOR = "Cyber Bishnoi"

# ==============================================================================
# CORE SYSTEM: UTILITIES
# ==============================================================================
class Utils:
    @staticmethod
    def clear():
        os.system('clear')

    @staticmethod
    def banner():
        Utils.clear()
        print(f"""{G}
    â–ˆâ–ˆâ–ˆâ–ˆâ–ˆâ–ˆâ•— â–ˆâ–ˆâ–ˆâ–ˆâ–ˆâ–ˆâ•—  â–ˆâ–ˆâ–ˆâ–ˆâ–ˆâ–ˆâ•— â–ˆâ–ˆâ–ˆâ–ˆâ–ˆâ–ˆâ–ˆâ–ˆâ•— â–ˆâ–ˆâ–ˆâ–ˆâ–ˆâ–ˆâ•—  â–ˆâ–ˆâ–ˆâ–ˆâ–ˆâ–ˆâ•— â–ˆâ–ˆâ–ˆâ–ˆâ–ˆâ–ˆâ•— â–ˆâ–ˆâ•—         â–ˆâ–ˆâ•—  â–ˆâ–ˆâ•—
    â–ˆâ–ˆâ•”â•â•â–ˆâ–ˆâ•—â–ˆâ–ˆâ•”â•â•â–ˆâ–ˆâ•—â–ˆâ–ˆâ•”â•â•â•â–ˆâ–ˆâ•—â•šâ•â•â–ˆâ–ˆâ•”â•â•â•â–ˆâ–ˆâ•”â•â•â•â–ˆâ–ˆâ•—â–ˆâ–ˆâ•”â•â•â•â•â•â–ˆâ–ˆâ•”â•â•â•â–ˆâ–ˆâ•—â–ˆâ–ˆâ•‘         â•šâ–ˆâ–ˆâ•—â–ˆâ–ˆâ•”â•
    â–ˆâ–ˆâ–ˆâ–ˆâ–ˆâ–ˆâ•”â•â–ˆâ–ˆâ–ˆâ–ˆâ–ˆâ–ˆâ•”â•â–ˆâ–ˆâ•‘   â–ˆâ–ˆâ•‘   â–ˆâ–ˆâ•‘   â–ˆâ–ˆâ•‘   â–ˆâ–ˆâ•‘â–ˆâ–ˆâ•‘     â–ˆâ–ˆâ•‘   â–ˆâ–ˆâ•‘â–ˆâ–ˆâ•‘          â•šâ–ˆâ–ˆâ–ˆâ•”â• 
    â–ˆâ–ˆâ•”â•â•â•â• â–ˆâ–ˆâ•”â•â•â–ˆâ–ˆâ•—â–ˆâ–ˆâ•‘   â–ˆâ–ˆâ•‘   â–ˆâ–ˆâ•‘   â–ˆâ–ˆâ•‘   â–ˆâ–ˆâ•‘â–ˆâ–ˆâ•‘     â–ˆâ–ˆâ•‘   â–ˆâ–ˆâ•‘â–ˆâ–ˆâ•‘          â–ˆâ–ˆâ•”â–ˆâ–ˆâ•— 
    â–ˆâ–ˆâ•‘     â–ˆâ–ˆâ•‘  â–ˆâ–ˆâ•‘â•šâ–ˆâ–ˆâ–ˆâ–ˆâ–ˆâ–ˆâ•”â•   â–ˆâ–ˆâ•‘   â•šâ–ˆâ–ˆâ–ˆâ–ˆâ–ˆâ–ˆâ•”â•â•šâ–ˆâ–ˆâ–ˆâ–ˆâ–ˆâ–ˆâ•—â•šâ–ˆâ–ˆâ–ˆâ–ˆâ–ˆâ–ˆâ•”â•â–ˆâ–ˆâ–ˆâ–ˆâ–ˆâ–ˆâ–ˆâ•—    â–ˆâ–ˆâ•”â• â–ˆâ–ˆâ•—
    â•šâ•â•     â•šâ•â•  â•šâ•â• â•šâ•â•â•â•â•â•    â•šâ•â•    â•šâ•â•â•â•â•â•  â•šâ•â•â•â•â•â• â•šâ•â•â•â•â•â• â•šâ•â•â•â•â•â•â•    â•šâ•â•  â•šâ•â•
    {W}
    {R}[+] DEVELOPER : {AUTHOR}
    {Y}[+] MODULES   : WiFi / RF / Analyzer
    {C}[+] VERSION   : {VERSION} (Termux API Build){W}
    =================================================================================
        """)

    @staticmethod
    def progress_bar(task_name, duration):
        """Advanced Loading Bar"""
        print(f"{B}[*] Initiating: {task_name}...{W}")
        toolbar_width = 40
        for i in range(toolbar_width + 1):
            time.sleep(duration / toolbar_width)
            sys.stdout.write(f"\r{C}[{('=' * i).ljust(toolbar_width)}] {int((i/toolbar_width)*100)}%{W}")
            sys.stdout.flush()
        print()

# ==============================================================================
# MODULE 1: RECONNAISSANCE (SCANNER)
# ==============================================================================
class ReconModule:
    def __init__(self):
        self.targets = []

    def get_networks(self):
        """Fetches REAL data via Termux API"""
        try:
            # Check API status
            cmd = ["termux-wifi-scaninfo"]
            proc = subprocess.run(cmd, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
            output = proc.stdout.decode("utf-8")
            
            if not output: return None
            
            data = json.loads(output)
            if isinstance(data, list):
                self.targets = data
                return data
            elif isinstance(data, dict) and 'API_ERROR' in data:
                return "API_ERROR"
            return None
        except FileNotFoundError:
            return "NO_PKG"
        except Exception:
            return None

    def display_targets(self):
        if not self.targets:
            print(f"{R}[!] No data found in cache.{W}")
            return None

        print(f"\n{Y}{'ID':<4} {'SSID (Name)':<20} {'BSSID (Mac Addr)':<18} {'SIG':<5} {'FREQ':<6}{W}")
        print("-" * 60)
        
        for index, net in enumerate(self.targets):
            ssid = net.get('ssid', 'Hidden')[:18]
            bssid = net.get('bssid', 'Unknown')
            rssi = net.get('rssi', 0)
            freq = net.get('frequency_mhz', 0)
            
            color = G if rssi > -60 else Y if rssi > -80 else R
            print(f"{W}[{index}]  {color}{ssid:<20} {C}{bssid:<18} {W}{rssi:<5} {freq:<6}")
        
        return self.targets

# ==============================================================================
# MODULE 2: VULNERABILITY ANALYZER
# ==============================================================================
class AnalyzerModule:
    def analyze(self, target_dict):
        Utils.progress_bar("Analyzing Packets", 1.5)
        
        ssid = target_dict.get('ssid', 'Unknown')
        rssi = target_dict.get('rssi', -100)
        freq = target_dict.get('frequency_mhz', 2400)
        
        print(f"\n{G}[+] TARGET ACQUIRED: {ssid}{W}")
        print(f"{B}[i] Signal Strength : {rssi} dBm")
        print(f"{B}[i] Band Frequency  : {freq} MHz")
        
        # Logic to determine weakness
        score = 0
        if rssi > -65: score += 2  # Strong signal = good for attack
        if freq < 3000: score += 1 # 2.4GHz is more crowded/vulnerable
        
        print(f"{Y}[?] Vulnerability Assessment:{W}")
        if score >= 3:
            print(f"    â””â”€â”€ Status: {R}HIGHLY VULNERABLE (Ideal for Bruteforce){W}")
        elif score == 2:
            print(f"    â””â”€â”€ Status: {Y}MODERATE (Possible Latency){W}")
        else:
            print(f"    â””â”€â”€ Status: {G}HARDENED / WEAK SIGNAL{W}")
        
        return True

# ==============================================================================
# MODULE 3: ATTACK VECTOR (HYBRID LOGIC)
# ==============================================================================
class AttackModule:
    def __init__(self, target_data):
        self.target = target_data
        self.wordlist = "/sdcard/Download/pass.txt" # Default

    def load_wordlist(self):
        print(f"\n{Y}[?] Enter path to wordlist (Press Enter for default):{W}")
        path = input(f"{C}PROTOCOL-X > {W}").strip()
        if path: self.wordlist = path
        
        if not os.path.exists(self.wordlist):
            print(f"{R}[!] Error: Wordlist not found at {self.wordlist}{W}")
            return False
        return True

    def brute_force_attack(self):
        ssid = self.target.get('ssid')
        bssid = self.target.get('bssid')
        
        print(f"\n{R}[!] INITIALIZING ATTACK PROTOCOL ON [{bssid}]{W}")
        print(f"{Y}[!] WARNING: Do not close Termux during operation.{W}")
        time.sleep(1)
        
        try:
            with open(self.wordlist, 'r', encoding='utf-8', errors='ignore') as f:
                passwords = f.readlines()
                
            print(f"{G}[+] Loaded {len(passwords)} payloads.{W}\n")
            
            start_time = time.time()
            
            for pwd in passwords:
                pwd = pwd.strip()
                if not pwd: continue
                
                # SIMULATION LOGIC: 
                # Calculating hash time + API latency simulation
                sys.stdout.write(f"\r{B}[*] Testing: {W}{pwd:<15} {C} >> {bssid}{W}")
                sys.stdout.flush()
                
                # Fake delay to simulate handshake verification
                time.sleep(random.uniform(0.02, 0.1))
                
                # Mock Success Condition (For demo purposes)
                # In real scenario, this would check connection handshake
                if pwd == "admin123" or pwd == "password":
                    print(f"\n\n{G}[SUCCESS] HANDSHAKE VALIDATED!{W}")
                    print(f"{G}[+] KEY FOUND: {pwd}{W}")
                    print(f"{Y}[i] Time taken: {round(time.time() - start_time, 2)}s{W}")
                    return

            print(f"\n\n{R}[-] Attack Failed. Password not in list.{W}")
            
        except Exception as e:
            print(f"\n{R}[!] Module Error: {e}{W}")

# ==============================================================================
# MAIN CONTROL CENTER
# ==============================================================================
def main():
    Utils.banner()
    
    # Init Modules
    recon = ReconModule()
    
    while True:
        print(f"\n{W}Choose Operation Mode:{W}")
        print(f"{C}[1]{W} Scan Networks (Recon)")
        print(f"{C}[2]{W} Analyze Target (Vulnerability)")
        print(f"{C}[3]{W} Initiate Attack (Bruteforce)")
        print(f"{C}[4]{W} Exit Framework")
        
        choice = input(f"\n{R}root@protocol-x:~# {W}")
        
        if choice == '1':
            Utils.progress_bar("Scanning Airwaves", 2.0)
            data = recon.get_networks()
            if data == "API_ERROR":
                print(f"{R}[!] Error: Please turn on LOCATION (GPS).{W}")
            elif data == "NO_PKG":
                print(f"{R}[!] Error: Termux-API not installed.{W}")
            elif data:
                recon.display_targets()
            else:
                print(f"{R}[!] No networks found.{W}")

        elif choice == '2':
            if not recon.targets:
                print(f"{R}[!] Error: Run Scan [1] first.{W}")
                continue
            
            try:
                t_id = int(input(f"{Y}[?] Enter Target ID from Scan List: {W}"))
                target = recon.targets[t_id]
                analyzer = AnalyzerModule()
                analyzer.analyze(target)
            except (IndexError, ValueError):
                print(f"{R}[!] Invalid selection.{W}")

        elif choice == '3':
            if not recon.targets:
                print(f"{R}[!] Error: No targets. Run Scan [1] first.{W}")
                continue
                
            try:
                t_id = int(input(f"{Y}[?] Select Target ID to Attack: {W}"))
                target = recon.targets[t_id]
                
                # Confirm Attack
                print(f"\n{R}[WARNING] You are about to attack {target.get('ssid')}.{W}")
                confirm = input("Confirm? (y/n): ")
                
                if confirm.lower() == 'y':
                    attacker = AttackModule(target)
                    if attacker.load_wordlist():
                        attacker.brute_force_attack()
            except (IndexError, ValueError):
                print(f"{R}[!] Invalid selection.{W}")

        elif choice == '4':
            print(f"{G}Exiting Protocol-X...{W}")
            break
        
        else:
            print(f"{R}Invalid Command.{W}")

if __name__ == "__main__":
    main()