Banco de Dados: Arquivo local SQLite3 db.sqlite3
Linguagem: Python 3.8 64bits
Framework Principal: Flask
IDE*: Visual Studio Code


Ambiente 1 - HTML:
	bibliotecas: 	flask, flask_login, flask_sqlalchemy, jinja2, requests
					werkzeug.security, os, json
	Inicialização:		
		Criação de ambiente virtual: 	python -m venv env 
		PowerShell:						$env:FLASK_APP = 'Flask_Places'
										$env:FLASK_DEBUG = '1'
										$env:FLASK_RUN_PORT = '5000'
		Ngrok:							Gerar tunelamento para acessar online

Ambiente 2 - BANCO DE DADOS:
	bibliotecas:	flask, requests, os, flask_login, sqlite3, json
	Inicialização:
		Criação de ambiente virtual:	python -m venv database
		PowerShell:						python database.py (porta 5001 não tunelada)

Geocodes através de	geopy