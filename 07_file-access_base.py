'''
Read lines from 'devices.txt' and print the content like:
Cisco 819 Router
Cisco 881 Router
Cisco 888 Router
Cisco 1100 Router
Cisco 4321 Router
Cisco 4331 Router
Cisco 4351 Router
Cisco 2960 Catalyst Switch
Cisco 3850 Catalyst Switch
Cisco 7700 Nexus Switch
Cisco Meraki MS220-8 Cloud Managed Switch
Cisco Meraki MX64W Security Appliance
Cisco Meraki MX84 Security Appliance
Csico Meraki MC74 VoIP Phone
Cisco 3860 Catalyst Switch

Insert datas into a new list!
Print list!
'''
f = open('devices.txt')
devices = f.read()
print(devices)
f.close()