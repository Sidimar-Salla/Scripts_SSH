from pydantic import BaseModel
from typing import Optional


class CommandsProps(BaseModel):
    ip_config: Optional[str]
    gateway: Optional[str]
    netmask: Optional[str]
    vlan: Optional[str]
    vlan_nomes: Optional[str]
    mngt_vlan: Optional[int]
    fibre_port: Optional[int]
    port: Optional[str]
    vlan_port: Optional[str]
    vlan_exclude: Optional[str]


def addlistcommands(command: CommandsProps):
    """
        Parameters
        -----------
        kwargs: dict
            - Configurar IP:
                    * ip_config = IP que irá ficar o equipamento
                    * gateway = Gateway à configrar
                    * netmask = Máscara de Sub-Rede
            - Configrar Vlan:
                    * mngt_vlan = vlan para gerenciamento
                    * vlan = Números das vlan que vão ser adicionada
                    * vlan_nomes = Nomes das vlan
            - Configurar Porta de Fibra:
                    * fibre_port = Porta que foi conectada a fibra
            - configurando porta na vlan:
                    * port = Porta a ser configurado
                    * vlan_port = vlan a ser adicionado 
                    * vlan_exclude = vlan a ser excluida da porta
        """

    listCommands = []

    listCommands.append("enable")
    # listCommands.append("config")

    if command.ip_config and command.gateway and command.netmask:
        listCommands.append(
            f""" network parms {command.ip_config} {command.netmask} {command.gateway}""")

    if command.mngt_vlan and command.vlan and command.vlan_nomes:
        listCommands.append(f"network mgmt_vlan {command.mngt_vlan}")
        listCommands.append("vlan database")
        num_vlan = command.vlan.split(',')
        name_vlan = command.vlan_nomes.split(',')
        for vlan in num_vlan:
            listCommands.append(f"vlan {vlan}")
            pos_name = num_vlan.index(vlan)
            listCommands.append(
                f"vlan name {vlan} {name_vlan[pos_name]}")

    if command.fibre_port:
        listCommands.append(f"interface 1/0/{command.fibre_port}")
        listCommands.append('switchport mode trunk')
        listCommands.append('vlan participation exclude 1')

    if command.port and command.vlan_port and command.vlan_exclude:
        num_vlan = command.port.split(',')
        vlan_conf = command.vlan_port.split(',')
        vlan_del = command.vlan_exclude.split(',')
        for ports in num_vlan:
            listCommands.append(f"interface 1/0/{ports}")
            listCommands.append('switchport mode access')
            for vlan_add in vlan_conf:
                listCommands.append(f'switchport access vlan {vlan_add}')
            for vlan_exclude in vlan_del:
                listCommands.append(
                    f'vlan participation exclude {vlan_exclude}')

    return listCommands
