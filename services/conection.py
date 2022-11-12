import paramiko
from getpass import getpass
from time import sleep


class ConectionSSH:

    def SSHConection(**kawrgs):
        '''
            hostname: IP do equipamento (num)
            username: Nome do Usuário (str)
            password: Senha do Usuário (num|str)
            listCommands: Lista de comandos a serem realizados (list)

        '''
        # Fazendo a conexão
        ssh = paramiko.SSHClient()
        ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
        ssh.connect(
            hostname=kawrgs.get('hostname'),
            username=kawrgs.get('username'),
            password=kawrgs.get('password'))

        channel = ssh.invoke_shell()
        out = channel.recv(9999)

        # Executando comando
        for command in kawrgs.get('listCommands'):
            channel.send(f'{command}\n')
            sleep(.5)

        channel.send(f'write memory confirm\n')
        while not channel.recv_ready():
            sleep(2)

        out = channel.recv(9999)
        print(out.decode("ascii"))

        # Encerrando conexão
        ssh.close()
