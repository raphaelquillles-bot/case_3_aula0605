import sqlite3
from src.models.sessao import Sessao # <-- Ajustado para o nome minúsculo do seu arquivo

class SessaoRepository:
    def __init__(self, db_path='cinema.db'):
        self.db_path = db_path

    def conectar(self):
        return sqlite3.connect(self.db_path)

    def buscar_por_id(self, id_sessao):
        conn = self.conectar()
        cursor = conn.cursor()
        cursor.execute("SELECT id, id_cinema, filme, publico_registrado FROM Sessao WHERE id = ?", (id_sessao,))
        linha = cursor.fetchone()
        conn.close()
        
        if linha:
            return Sessao(linha[0], linha[1], linha[2], linha[3])
        return None

    def buscar_capacidade_cinema_da_sessao(self, id_sessao):
        conn = self.conectar()
        cursor = conn.cursor()
        cursor.execute("""
            SELECT c.capacidade_publico 
            FROM Cinema c 
            JOIN Sessao s ON c.id = s.id_cinema 
            WHERE s.id = ?
        """, (id_sessao,))
        linha = cursor.fetchone()
        conn.close()
        
        if linha:
            return linha[0]
        return 0

    def atualizar_publico(self, id_sessao, novo_publico):
        conn = self.conectar()
        cursor = conn.cursor()
        cursor.execute("UPDATE Sessao SET publico_registrado = ? WHERE id = ?", (novo_publico, id_sessao))
        conn.commit()
        conn.close()