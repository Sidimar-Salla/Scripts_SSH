import paramiko
from getpass import getpass
from time import sleep

address = '192.168.0.2'
username = 'admin'
password = 'Swnu*hgt'

# Fazendo a conexão
ssh = paramiko.SSHClient()
ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
ssh.connect(hostname=address, username=username, password=password)

# Executando comando
stdin, stdout, stderr = ssh.exec_command("enable")
sleep(.5)
stdin.close()

print(stdout.readlines())

# Encerrando conexão
ssh.close()
