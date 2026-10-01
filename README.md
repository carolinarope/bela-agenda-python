# Bela Agenda — Sistema de Gestão para Salões (Python)

Projeto pessoal desenvolvido em Python para praticar a construção de um sistema de gestão de clientes, serviços e agendamentos para salões de beleza.

O projeto foi evoluído em etapas. Começou com uma estrutura procedural e, posteriormente, passou por uma refatoração para Programação Orientada a Objetos (POO). O repositório registra esse processo de aprendizagem.

## Objetivo

Praticar a implementação de funcionalidades comuns em um sistema de agendamentos:

- Cadastro e listagem de clientes.
- Cadastro e listagem de serviços.
- Criação e consulta de agendamentos.
- Validação de entradas.
- Persistência e recuperação de dados.

## Versão documentada — V3: POO

A versão V3 organiza responsabilidades em classes:

- `BelaAgenda`: coordena as operações do sistema.
- `Usuario`: representa os dados de um cliente.
- `Servico`: representa um serviço oferecido.
- `Agendamento`: representa a relação entre cliente e serviço, incluindo informações do agendamento.

A aplicação utiliza métodos e atributos para organizar os dados e as operações, além de persistir informações localmente em arquivos JSON.

### Persistência

Os dados são armazenados em arquivos JSON. A implementação trabalha com conversão entre objetos e dicionários para salvar e reconstruir os registros quando a aplicação é iniciada.

## Etapas anteriores

### V2 — Validações e persistência

- Validação de formato de e-mail e verificação de duplicidade.
- Validação de telefone.
- Validação de datas com `datetime`.
- Validação de horários.
- Tratamento de entradas numéricas com exceções.
- Salvamento e carregamento de dados em JSON.

### V1 — Fundamentos

A primeira etapa foi utilizada para praticar lógica, funções, estruturas de dados e navegação por menus.

## Tecnologias e conceitos praticados

- Python
- Funções e modularização
- Classes e objetos
- Encapsulamento e composição
- Listas e dicionários
- Validação de dados
- Tratamento de exceções
- JSON e manipulação de arquivos
- `datetime`
- Git e GitHub

## Como executar

1. Clone o repositório.
2. Abra a pasta do projeto em sua IDE.
3. Verifique as dependências utilizadas nos arquivos do projeto.
4. Execute o arquivo principal da versão desejada.

## Próximas melhorias

As próximas etapas podem incluir regras mais completas de integridade dos agendamentos, integração com banco de dados relacional e exposição de funcionalidades por API. Esses itens são possibilidades de evolução, não funcionalidades já concluídas nesta versão.

## Sobre o projeto

Este é um projeto de estudo e portfólio pessoal. Seu propósito é demonstrar a evolução prática em Python e a aplicação gradual de conceitos de desenvolvimento de software.
