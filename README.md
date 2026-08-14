# 💇‍♀️ Bela Agenda — Sistema de Gestão para Salões

O **Bela Agenda** é um projeto desenvolvido em Python com o objetivo de simular um sistema de gestão para salões de beleza.

O projeto está sendo desenvolvido de forma **incremental**, começando pela construção da lógica com Python e evoluindo posteriormente para Programação Orientada a Objetos (POO), banco de dados SQL e interface gráfica.

---

## 🎯 Objetivo

Desenvolver um sistema capaz de gerenciar:

- Usuários/clientes
- Serviços
- Agendamentos
- Validação de dados
- Persistência das informações

A proposta é construir a aplicação por etapas, fortalecendo primeiro a lógica de programação e as regras de negócio antes da evolução da arquitetura.

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

## 🧠 Conceitos praticados

Durante o desenvolvimento da V2 foram praticados conceitos fundamentais de Python:

- Criação e reutilização de funções
- Parâmetros e argumentos
- Retorno múltiplo com `return`
- Tuplas
- `if`, `elif` e `else`
- `for` e `while`
- Listas e dicionários
- Métodos de strings
- `try` e `except`
- Manipulação de arquivos
- Serialização com JSON
- Validação de entradas
- Organização modular do código

---

## 🗺️ Roadmap

- **Fase 0 — Fundamentos:** Estruturas de dados, funções, menu e persistência JSON — ✅ Concluído
- **Fase 1 — Validações:** Validação de e-mail, telefone, data, hora e duplicidade — ✅ Concluído
- **Fase 2 — POO:** Refatoração do sistema utilizando classes, encapsulamento, herança e polimorfismo — 🔜 Próxima etapa
- **Fase 3 — Banco de Dados:** Integração com banco de dados relacional e SQL
- **Fase 4 — Interface:** Desenvolvimento de interface gráfica e expansão das regras de negócio

---

## 📌 Próximos passos

A próxima evolução do projeto será a refatoração da aplicação para **Programação Orientada a Objetos (POO)**, substituindo gradualmente a estrutura baseada apenas em funções e dicionários por classes e objetos.

Posteriormente, o sistema será integrado a um banco de dados relacional utilizando SQL.

---

## 👩‍💻 Projeto em desenvolvimento

Projeto desenvolvido como parte da minha evolução prática em **Python, desenvolvimento de software e análise de dados**.
