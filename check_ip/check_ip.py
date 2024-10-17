import subprocess
import re

# Check the current IP address
def check_ip(interface):
    try:
        result = subprocess.run(f"ip addr show {interface}", shell=True, capture_output=True, text=True)
        if result.returncode == 0:
            # Regrex to extract IP address from the result

            ip_pattern = r"inet (\d+\.\d+\.\d+\.\d+)"
            ip_match = re.search(ip_pattern, result.stdout)
            if ip_match:
                print(f" [+] IP Address of {interface}: {ip_match.group(1)}")
            else:
                print(f" [-] No IP address found for {interface}.")
        else:
            print(f"Error getting IP address: {result.stderr}")
    
    except Exception as e:
        print(f"Error: {str(e)}")