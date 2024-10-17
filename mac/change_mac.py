import subprocess

# Function to change mac address
def change_mac(interface, new_mac):
    try:
        subprocess.run(f"sudo ifconfig {interface} down", shell=True)
        subprocess.run(f"sudo ifconfig {interface} hw ether {new_mac}", shell=True)
        subprocess.run(f"sudo ifconfig {interface} up", shell=True)
        print(f"MAC address for {interface} changed to {new_mac}")
    except Exception as e:
        print(f"Error changing MAC address: {str(e)}")