import getpass
import telnetlib

HOST = "192.168.0.34"
user = input("Enter your remote account: ")
password = getpass.getpass()

tn = telnetlib.Telnet(HOST)

tn.read_until(b"User: ")
tn.write(user.encode('ascii') + b"\n")
if password:
    tn.read_until(b"Password: ")
    tn.write(password.encode('ascii') + b"\n")

if tn:
    print('Conectou')

print(tn.read_all().decode('ascii'))
