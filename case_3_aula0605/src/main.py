# src/main.py
import sqlite3
import os

# Repare que aqui importamos as classes com as Iniciais Maiúsculas!
from src.repositories.sessaorepository import SessaoRepository
from src.services.sessaoservice import SessaoService
from src.controllers.sessaocontroller import SessaoController
from src.views.sessaoview import SessaoView

def inicializar_banco():
    # Lê o schema.sql e cria o arquivo cinema.db se não existir
    if not os.path.exists('cinema.db'):
        conn = sqlite3.connect('cinema.db')
        with open('schema.sql', 'r', encoding='utf-8') as f:
            conn.executescript(f.read())
        conn.close()
        print("Banco de dados criado com dados de teste!")

if __name__ == "__main__":
    inicializar_banco()
    
    # "Montando" a arquitetura do sistema (Injeção de Dependências)
    repository = SessaoRepository(db_path='cinema.db')
    service = SessaoService(repository)
    controller = SessaoController(service)
    view = SessaoView(controller)
    
    # Rodando o sistema
    view.exibir_menu_registro()