#!/usr/bin/env python3
import argparse
from network_info.display_net import display_network_conf
from ip.change_ip import change_ip
from mac.change_mac import change_mac
from check_ip.check_ip import check_ip

# The function that uses optparse
def main():
    # Create the parser
    parser = argparse.ArgumentParser(prog='Macchanger', description='A tool for network configuration management writting by Ephraim Norbert')

    # Define the available options
    parser.add_argument("-n", "--network", action="store_true", help="Display the current network configuration")

    parser.add_argument("-i", "--ip", metavar=("INTERFACE", "NEW_IP", "NETMASK"), nargs=3, help="Change the IP address of a network interface. Requires INTERFACE, NEW_IP, and NETMASK")

    parser.add_argument("-m", "--mac", metavar=("INTERFACE", "NEW_MAC"), nargs=2, help="Change the MAC address of a network interface. Requires INTERFACE and NEW_MAC")

    parser.add_argument("-c", "--check", metavar="INTERFACE", nargs=1, help="Check the current IP address")

    # Parse the command line options and arguments
    args = parser.parse_args()

    # Check for network configuration option
    if args.network:
        display_network_conf()

    # Check for IP change option
    elif args.ip:
        interface, new_ip, netmask = args.ip
        change_ip(interface, new_ip, netmask)

    # Check for MAC address change option
    elif args.mac:
        interface, new_mac = args.mac
        change_mac(interface, new_mac)

    # Check the current IP address
    elif args.check:
        interface = args.check[0]
        check_ip(interface)

    # If no arguments are provided, display help
    else:
        parser.print_help()

# Run the main function
if __name__ == "__main__":
    main()


        