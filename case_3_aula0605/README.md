# Sistema de Gestão de Rede de Cinemas

## Contextualização do Problema
Uma rede de cinemas possui diversas unidades espalhadas por diferentes cidades e estados. Cada cinema possui características próprias (como capacidade de público e endereço) e exibe simultaneamente vários filmes em cartaz, organizados em sessões ao longo do dia.

Este sistema foi desenvolvido para resolver os seguintes desafios de gestão:
* Controle dos filmes em exibição por cinema.
* Organização das sessões, respeitando a duração dos filmes e intervalos.
* Registro diário do público de cada sessão.
* Totalização de público por sessão, por filme e por cinema.
* Consulta de informações sobre o catálogo (elenco, diretores e gêneros).

---

## 1. Levantamento de Requisitos e Regras de Negócio

### Requisitos Funcionais (RF)
* **RF01:** O sistema deve permitir o cadastro de Cinemas, Filmes e Sessões.
* **RF02:** O sistema deve permitir registrar a quantidade de público presente em uma sessão.
* **RF03:** O sistema deve gerar a totalização de público (por sessão, filme e cinema).
* **RF04:** O sistema deve permitir a consulta de filmes em cartaz e seus detalhes (elenco, diretor, gênero).

### Regras de Negócio (RN)
* **RN01:** O público registrado em uma sessão não pode ultrapassar a capacidade máxima do cinema/sala.
* **RN02:** Deve haver um intervalo obrigatório (ex: 30 minutos) entre as sessões na mesma sala para limpeza.
* **RN03:** Uma sessão não pode ser sobreposta a outra na mesma sala.

---

## 2. Diagrama de Casos de Uso (Visão Geral)
Abaixo, a representação das principais interações dos atores com o sistema.

```mermaid
flowchart LR
    %% Atores
    Funcionario([Funcionário / Administrador])
    Espectador([Espectador])

    %% Casos de Uso
    UC1(Cadastrar Cinema)
    UC2(Gerenciar Filmes e Catálogo)
    UC3(Agendar Sessão)
    UC4(Registrar Público da Sessão)
    UC5(Consultar Totalização de Público)
    UC6(Consultar Filmes em Cartaz)

    %% Relações
    Funcionario --> UC1
    Funcionario --> UC2
    Funcionario --> UC3
    Funcionario --> UC4
    Funcionario --> UC5
    
    Espectador --> UC6

    classDiagram
    class Cinema {
        +String nome
        +String enderecoCompleto
        +int capacidadePublico
    }

    class Filme {
        +String titulo
        +int duracaoMinutos
        +String sinopse
    }

    class Sessao {
        +DateTime dataHoraInicio
        +DateTime dataHoraFim
        +int publicoRegistrado
    }

    class Profissional {
        +String nome
        +String papelCinegrafico
    }

    class Genero {
        +String descricao
    }

    Cinema "1" -- "0..*" Sessao : possui
    Filme "1" -- "0..*" Sessao : exibido em
    Filme "1..*" -- "1..*" Genero : classificado como
    Filme "1..*" -- "1..*" Profissional : possui (Elenco/Diretor)

    stateDiagram-v2
    [*] --> SelecionarCinema
    SelecionarCinema --> SelecionarSessao
    SelecionarSessao --> InformarQuantidadePublico
    InformarQuantidadePublico --> ValidarCapacidade
    
    state ValidarCapacidade {
        direction LR
        Validando --> CapacidadeExcedida: if (público > capacidade)
        Validando --> CapacidadePermitida: if (público <= capacidade)
    }
    
    CapacidadeExcedida --> InformarQuantidadePublico : Exibir Erro
    CapacidadePermitida --> SalvarRegistro
    SalvarRegistro --> [*]

    sequenceDiagram
    actor Funcionario
    participant View (Interface)
    participant Controller
    participant Service
    participant Repository
    participant SQLite (Database)

    Funcionario->>View (Interface): Inserir dados (ID Sessão, Qtd Público)
    View (Interface)->>Controller: registrarPublico(idSessao, qtd)
    Controller->>Service: processarRegistro(idSessao, qtd)
    
    Service->>Repository: buscarSessaoECapacidade(idSessao)
    Repository->>SQLite (Database): SELECT * FROM Sessao ...
    SQLite (Database)-->>Repository: Dados da Sessão e Cinema
    Repository-->>Service: Objeto Sessao
    
    Service->>Service: Validar RN01 (Capacidade Máxima)
    Service->>Repository: atualizarPublico(idSessao, qtd)
    Repository->>SQLite (Database): UPDATE Sessao SET publico = ...
    SQLite (Database)-->>Repository: OK
    Repository-->>Service: Sucesso
    Service-->>Controller: Sucesso
    Controller-->>View (Interface): Exibir Mensagem("Público registrado com sucesso")
    View (Interface)-->>Funcionario: Confirmação Visual