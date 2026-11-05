# Bela Agenda — agendamentos para salões de beleza

**Projeto Integrador do Técnico em Desenvolvimento de Sistemas — Senac, com tema escolhido por Carolina Rodrigues.**

Escolhi desenvolver a Bela Agenda para organizar clientes, serviços e agendamentos de salões de beleza. A primeira etapa acadêmica foi dedicada à estrutura do banco de dados e aos requisitos do sistema.

Como já estudava Python, implementei uma versão inicial nessa linguagem para praticar programação enquanto avançava nos estudos de Java. Este repositório reúne essa evolução em Python.

## Versão disponível: Python no terminal

A V3, em [`bela_agenda_v3.py`](bela_agenda_v3.py), utiliza orientação a objetos e um menu no terminal com Rich.

| Classe | Responsabilidade |
|---|---|
| `BelaAgenda` | Manter listas, realizar cadastros, validações e persistência |
| `Usuario` | Representar os dados de uma pessoa cliente |
| `Servico` | Representar nome, duração e preço de um serviço |
| `Agendamento` | Relacionar os IDs de cliente e serviço com data, hora e status |

### Funcionalidades atuais

- Cadastro e listagem de usuários e serviços.
- Validação básica de e-mail e verificação de duplicidade.
- Validação de telefone com 10 ou 11 dígitos.
- Validação de duração positiva e formato de data/hora.
- Criação e consulta de agendamentos.
- Salvamento e carregamento de registros em arquivos JSON locais.
- Menu interativo no terminal.

O salvamento é solicitado ao sair do menu. A versão atual ainda precisa de melhorias na verificação dos IDs dos agendamentos, nas regras de conflito de horários e na validação dos serviços.

## Evolução registrada

| Arquivo | Etapa |
|---|---|
| [`bela_agenda_v1.py`](bela_agenda_v1.py) | Primeira implementação, com lógica, funções e menu |
| [`bela_agenda_v2.py`](bela_agenda_v2.py) | Evolução das validações e da persistência |
| [`bela_agenda_v3.py`](bela_agenda_v3.py) | Organização em classes, validações e JSON |
| [`requirements.txt`](requirements.txt) | Dependência da versão atual |

## Como executar

Tenha Python 3 instalado. No terminal:

```bash
git clone https://github.com/carolinarope/bela-agenda-python.git
cd bela-agenda-python
python -m pip install -r requirements.txt
python bela_agenda_v3.py
```

Os arquivos JSON são gravados na pasta de execução quando você escolhe salvar os dados. Para experimentar o sistema, utilize dados fictícios.

## Continuidade do Projeto Integrador: Java e MySQL

A continuidade da Bela Agenda será em **Java**, conforme as próximas entregas do Projeto Integrador. Pretendo aplicar os conhecimentos praticados no [Cenaflix](https://github.com/carolinarope/Java-projetos-academicos/tree/main/Cenaflix_java_jdbc):

- Classes para representar os dados e as regras do sistema.
- Interface gráfica com **Java Swing**.
- Conexão por **JDBC** e persistência no **MySQL**.
- Organização entre telas, modelo, acesso a dados e conexão.
- Publicação do código, da estrutura do banco e das instruções de execução no GitHub.

A versão Python é a implementação inicial de aprendizagem. A versão Java será compartilhada conforme o avanço das atividades acadêmicas.

## Tecnologias da versão atual

Python · Orientação a objetos · Listas e dicionários · JSON · datetime · Rich

[Perfil da autora](https://github.com/carolinarope) · [LinkedIn](https://www.linkedin.com/in/carolina-rope/)
