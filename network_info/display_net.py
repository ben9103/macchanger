import subprocess

# function to display to current network configuration
def display_network_conf():
    try:
        result = subprocess.run(f"ifconfig", shell=True, capture_output=True, text=True)
        if result.returncode == 0:
            print(result.stdout)
        else:
            print(result.stderr)
    except Exception as e:
        print(f"Error: {str(e)}")