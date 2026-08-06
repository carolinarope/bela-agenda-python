# 💇‍♀️ Bela Agenda (Sistema de Gestão para Salões)

O **Bela Agenda** é um projeto real de desenvolvimento de software em Python focado na gestão completa de salões de beleza. O objetivo final é entregar um sistema robusto com interface gráfica, banco de dados relacional (MySQL), regras de negócio avançadas (como sistema de pontuação e fidelidade) e relatórios para tomada de decisão.

O projeto está sendo construído de forma modular e incremental.

---

## 🚧 Status Atual: Fase 0 (Fundamentos e Estrutura Inicial)

Nesta primeira etapa, o foco foi construir a base lógica do sistema utilizando as estruturas de dados fundamentais do Python, garantindo que o fluxo de informação funcione perfeitamente antes da implementação de Orientação a Objetos (POO) e Banco de Dados.

### 🛠️ Funcionalidades Implementadas (CLI Version)
* **Estrutura de Dados:** Gerenciamento de clientes, serviços e agendamentos utilizando **Dicionários** e **Listas** aninhadas.
* **CRUD Completo:** Funções nativas para criar, ler e listar registros.
* **Sistema de Menu Interativo:** Navegação via terminal (CLI) construída com laços `while` e tratamento de entrada de usuário (`.strip()`).
* **Persistência de Dados (JSON):** Salvamento e carregamento de dados localmente utilizando a biblioteca `json`, garantindo que as informações não se percam ao fechar a aplicação.
* **Relacionamento Simples:** Lógica inicial de chaves estrangeiras vinculando IDs de usuários e serviços aos agendamentos.

---

## 🗺️ Roadmap de Desenvolvimento

* **Fase 0 (Agosto):** Estrutura de dados básica (Dicionários, Funções e persistência JSON) - *✅ Concluído*
* **Fase 1 (Agosto):** Validações de segurança e detecção matemática de conflitos de horário.
* **Fase 2 (Setembro):** Refatoração completa para **Programação Orientada a Objetos (POO)** (Classes, Herança, Polimorfismo).
* **Fase 3 (Outubro):** Integração com Banco de Dados Relacional (SQL).
* **Fase 4 (Futuro):** Implementação de Interface Gráfica (UI) e Regras de Negócio Avançadas (Sistema de Pontos).
