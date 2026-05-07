-- schema.sql
CREATE TABLE IF NOT EXISTS Cinema (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    nome TEXT NOT NULL,
    capacidade_publico INTEGER NOT NULL
);

CREATE TABLE IF NOT EXISTS Sessao (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    id_cinema INTEGER,
    filme TEXT NOT NULL,
    publico_registrado INTEGER DEFAULT 0,
    FOREIGN KEY (id_cinema) REFERENCES Cinema(id)
);

-- Inserindo dados de teste
INSERT INTO Cinema (nome, capacidade_publico) VALUES ('Cine Tarde', 100);
INSERT INTO Sessao (id_cinema, filme, publico_registrado) VALUES (1, 'O Senhor dos Anéis', 50);