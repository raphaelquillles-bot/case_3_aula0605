# src/models/sessao.py

class Sessao:
    def __init__(self, id_sessao, id_cinema, filme, publico_registrado):
        self.id_sessao = id_sessao
        self.id_cinema = id_cinema
        self.filme = filme
        self.publico_registrado = publico_registrado