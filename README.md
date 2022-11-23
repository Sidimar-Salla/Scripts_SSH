# Scripts_SSH

Sistema usado para fazer configurações automáticas em switch's Datacom.
Ele se conecta por ssh no switch e executa os comandos de configuração.

# 📋 Pré-Requisitos

Python 3.10.8
Dash 2.7.0
Paramiko 2.12.0
Pydantic 1.10.2

# 🚀 Instalação

- Instalar o Python;
- Abro o terminar;
- Crie um Ambiente Virtual (Virtual Environment):

        python -m venv venv

- Com isso um ambiente virtual chamado de venv irá ser criado em sua máquina;
- Inicie o seu "venv"

        Windows: ./venv/scripts/activate
        Linux: source venv/bin/activate
        Mac: source venv/bin/activate

- Após esse comando seu terminar estará dentro do "venv";
- Agora você irá ter que instalar as bibliotecas usadas:

        pip install dash
        pip install paramiko
        pip install pydantic

- Feita essas instalações seu ambiente está pronto para executar a aplicação.
- Para executar basta usar o comando:

        python app.py

- E sua aplicação já está rodando.

# ⌨️ Acessando

Para acessar, basta abrir o navegador de sua preferencia e colocar o seguinte URL.

          http://127.0.0.1:8050/

Basta usar e aproveitar. :)
