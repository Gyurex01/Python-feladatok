# Create a simple IF function that compares nativeVLAN and dataVLAN values and prints result.
def compare(nativeVLAN, dataVLAN):
    if nativeVLAN == dataVLAN:
        print("The native VLAN and data VLAN are the same.")
    else:
        print("The native VLAN and data VLAN are different.")

# Example usage:
nativeVLAN = 20
dataVLAN = 20

compare(nativeVLAN, dataVLAN)