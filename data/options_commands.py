InitialConfig = [
    'enable',
    #  (f'network parms {ip} 255.255.255.0 192.168.0.254'),
    ''
]

VlanConfig = [
    'enable',
    'config',
    'network mgmt_vlan 100'
    'vlan database',
    'vlan 100',
    'vlan name 100 Servidores',
    'vlan 120',
    'vlan name 120 Wifi_Visitantes',
    'vlan 130',
    'vlan name 130 Wifi_Devices',
]

PortFibraConfig = [
    'enable',
    'config',
    'interface 1/0/25',
    'switchport mode trunk',
    'vlan participation exclude 1',
]
