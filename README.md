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

