import paramiko
from getpass import getpass
from time import sleep

address = input('Equipamento: ')
username = 'admin'
password = getpass()
ip = input('Para qual IP deseja configurar o equipamento: ')
print('''

''')

# Lista de comandos para execução
InitialConfig = [
    'enable',
    (f'network parms {ip} 255.255.255.0 192.168.0.254'),
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
    'vlan name 120 ',
    'vlan 130',
    'vlan name 130 ',
]

PortFibraConfig = [
    'enable',
    'config',
    'interface 1/0/25',
    'switchport mode trunk',
    'vlan participation exclude 1',
]

# Fazendo a conexão
ssh = paramiko.SSHClient()
ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
ssh.connect(hostname=address, username=username, password=password)

channel = ssh.invoke_shell()
out = channel.recv(9999)

# Executando comando
for command in InitialConfig:
    channel.send(f'{command}\n')
    sleep(.5)


channel.send(f'write memory confirm\n')
while not channel.recv_ready():
    sleep(2)

out = channel.recv(9999)
print(out.decode("ascii"))

# Encerrando conexão
ssh.close()
