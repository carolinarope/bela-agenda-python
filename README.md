# 💇‍♀️ Bela Agenda — Sistema de Gestão para Salões

Projeto desenvolvido em Python para simular um sistema de gestão de clientes, serviços e agendamentos para salões de beleza.

O projeto está sendo desenvolvido de forma incremental, acompanhando minha evolução em desenvolvimento backend com Python. A aplicação evolui progressivamente de uma implementação baseada em funções soltas para uma arquitetura utilizando Programação Orientada a Objetos (POO).

---

## 🎯 Objetivo

Construir uma aplicação prática para gerenciamento de:
- Usuários/Clientes
- Serviços oferecidos
- Agendamentos integrados
- Validação de regras de negócio
- Persistência das informações

---

## 🚧 Versão atual — V3: Programação Orientada a Objetos (POO)

Nesta versão, a arquitetura do sistema foi completamente refatorada. Saímos de uma estrutura baseada em funções e dicionários soltos para uma modelagem robusta utilizando Classes e Objetos.

### 🧩 Classes Implementadas
- `BelaAgenda`: Classe gerenciadora principal ("cérebro" do sistema), responsável por instanciar objetos, cruzar dados e executar validações encapsuladas.
- `Usuario`: Molde de entidade para armazenar os dados e IDs dos clientes.
- `Servico`: Molde de entidade que define nome, duração e preço dos tratamentos.
- `Agendamento`: Classe que utiliza **Composição** para relacionar o ID de um Usuário ao ID de um Serviço, gerando um status de marcação.

### 💾 Persistência Avançada em JSON
Os dados continuam sendo salvos nos arquivos `usuarios.json`, `servicos.json` e `agendamentos.json`, mas agora o sistema utiliza técnicas avançadas como:
- Uso do atributo mágico `__dict__` para serializar os objetos.
- Desempacotamento de dicionários (`**kwargs`) para recriar objetos na leitura.
- *List Comprehension* para otimização do fluxo de salvamento.

---

## ✅ Versões Anteriores (Legado)

### V2: Validações de Entrada
- **E-mail:** Verificação de formatação, regras de `@` e `.` e bloqueio de duplicidade.
- **Telefone:** Tratamento de strings (remoção de hífens) e limitação a 10 ou 11 dígitos.
- **Data e Hora:** Validação estrita de calendário usando a biblioteca `datetime`.
- **Tratamento de Exceções:** Uso de `try/except` para bloquear quebras de sistema (ValueError) em menus numéricos.

---

## 🛠️ Tecnologias e Conceitos Aplicados

- Python (Fundamentos e POO)
- Classes, Objetos, Atributos e Métodos
- Composição entre classes
- Tratamento de exceções (`try/except`)
- Listas, Dicionários e *List Comprehension*
- Biblioteca `json` para persistência
- Biblioteca `datetime` para formatação temporal
- Formatação de terminal com a biblioteca `rich`
- Git & GitHub (Controle de versionamento)

---

## 🗺️ Roadmap de Evolução

- **Fase 1 — Fundamentos:** Estruturas de dados, funções e menu interativo — ✅ Concluído
- **Fase 2 — Validações:** Tratamento de erros, formatação de e-mail/telefone/datas — ✅ Concluído
- **Fase 3 — POO:** Refatoração da arquitetura para Classes e Objetos — ✅ Concluído
- **Fase 4 — Integridade e Relacionamento:** Aprimorar a busca de objetos e travas de segurança entre agendamentos — 🔜 Próxima etapa
- **Fase 5 — Banco de Dados:** SQL e integração com banco relacional (MySQL).
- **Fase 6 — APIs:** HTTP, REST e desenvolvimento de APIs com Python.

---

## 👩‍💻 Sobre a Desenvolvedora

Projeto desenvolvido como parte da minha trilha de estudos práticos e evolução técnica em **Python, Arquitetura de Software e Desenvolvimento Backend**.