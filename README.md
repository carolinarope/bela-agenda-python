# 💇‍♀️ Bela Agenda — Sistema de Gestão para Salões

Projeto desenvolvido em Python para simular um sistema de gestão
de clientes, serviços e agendamentos para salões de beleza.

O projeto está sendo desenvolvido de forma incremental, acompanhando
minha evolução em desenvolvimento backend com Python.

## 🎯 Objetivo

Construir uma aplicação prática para gerenciamento de:

- Clientes
- Serviços
- Agendamentos
- Validação de dados
- Persistência das informações

O projeto evolui progressivamente de uma implementação baseada em
funções e estruturas de dados para uma arquitetura utilizando
Programação Orientada a Objetos, APIs e banco de dados.
---

## 🛠️ Tecnologias utilizadas

- Python
- JSON
- `datetime`
- Estruturas de dados (`list` e `dict`)
- Funções
- Estruturas condicionais
- Laços de repetição
- Validação e tratamento de entradas

---

## 🚧 Versão atual — V2: Validações

Nesta versão, o sistema evoluiu da estrutura básica para uma aplicação com **validação de dados de entrada**.

### ✅ Validações implementadas

#### 📧 E-mail
- Verificação da presença de `@`
- Verificação de apenas um `@`
- Separação entre usuário e domínio
- Verificação de e-mail incompleto
- Verificação da presença de `.` no domínio
- Verificação de e-mail duplicado

#### 📱 Telefone
- Remoção de espaços e hífens
- Verificação se contém apenas números
- Validação do tamanho do telefone (10 ou 11 dígitos)

#### 📅 Data
- Validação do formato `DD/MM/AAAA`
- Verificação de datas inválidas utilizando `datetime`

#### ⏰ Hora
- Validação do formato `HH:MM`
- Verificação de horários inválidos

### 💾 Persistência

Os dados podem ser:

- Salvos em arquivos JSON
- Carregados posteriormente através do sistema

Arquivos utilizados:

- `usuarios.json`
- `servicos.json`
- `agendamentos.json`

---

## 🖥️ Funcionalidades atuais

O sistema possui um menu interativo no terminal com as seguintes opções:

1. Adicionar usuário
2. Listar usuários
3. Adicionar serviço
4. Listar serviços
5. Criar agendamento
6. Listar agendamentos por data
7. Salvar dados em JSON
8. Carregar dados de JSON
9. Sair

---

## 🛠️ Tecnologias e conceitos

- Python
- Programação estruturada
- Funções
- Estruturas condicionais
- Laços de repetição
- Listas e dicionários
- Programação Orientada a Objetos (em evolução)
- Validação de dados
- Tratamento de exceções
- JSON
- datetime
- Git
- GitHub
---

## 🗺️ Roadmap

- **Fase 1 — Fundamentos Python:** lógica, estruturas de dados,
  funções e persistência JSON — ✅ Concluído

- **Fase 2 — Validações:** validação de e-mail, telefone, data,
  hora e entradas — ✅ Concluído

- **Fase 3 — POO:** refatoração utilizando classes, encapsulamento,
  herança e polimorfismo — 🔜 Próxima etapa

- **Fase 4 — APIs:** HTTP, REST e desenvolvimento de APIs com Python

- **Fase 5 — Banco de Dados:** SQL e integração com banco relacional

- **Fase 6 — Testes:** testes automatizados e qualidade de código

- **Fase 7 — Docker:** containerização da aplicação

---

## 📌 Próximos passos

A próxima evolução do projeto será a refatoração da aplicação para **Programação Orientada a Objetos (POO)**, substituindo gradualmente a estrutura baseada apenas em funções e dicionários por classes e objetos.

Posteriormente, o sistema será integrado a um banco de dados relacional utilizando SQL.

---

## 👩‍💻 Projeto em desenvolvimento

Projeto desenvolvido como parte da minha evolução prática em **Python e desenvolvimento de software backend**.
