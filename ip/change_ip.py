import subprocess

# function to change IP address
def change_ip(interface, new_ip, netmask):
    try:
        result = subprocess.run(f"sudo ifconfig {interface} {new_ip} netmask {netmask}", shell=True, capture_output=True, text=True)
        if result.returncode == 0:
            print(f"IP address of {interface} changed to {new_ip}/{netmask}")
        else:
            print(f"Error changing IP address: {result.stderr}")
    except Exception as e:
        print(f"Error: {str(e)}")