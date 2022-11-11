import paramiko
from getpass import getpass
from time import sleep

address = '192.168.1.25'
username = 'admin'
password = 'Swnu*hgt'
ip = input('Para qual IP deseja configurar o equipamento: ')

# Fazendo a conexão
ssh = paramiko.SSHClient()
ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
ssh.connect(hostname=address, username=username, password=password)

channel = ssh.invoke_shell()
out = channel.recv(9999)

# Executando comando
comands = [

]

for command in comands:
  channel.send(f'{command}\n')
  sleep(.5)

while not channel.recv_ready():
    sleep(2)

out = channel.recv(9999)
print(out.decode("ascii"))

# Encerrando conexão
ssh.close()
