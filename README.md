# Bela Agenda — gestão de salão de beleza

> **Projeto pessoal em desenvolvimento — produto autoral de Carolina Rodrigues.**  
> Uma solução que estou construindo para organizar clientes, serviços e agendamentos de salões de beleza, começando por uma aplicação desktop e com visão de expansão futura para outras plataformas.

A Bela Agenda não é apenas um exercício isolado de programação: é meu projeto pessoal de produto. A ideia é desenvolver, testar e evoluir uma solução para uma necessidade concreta de gestão de pequenos negócios de beleza. O sistema ainda está em desenvolvimento e as funcionalidades descritas abaixo correspondem às versões de estudo disponíveis neste repositório — não a um produto comercial já lançado.

## Visão do produto

Meu objetivo é construir a Bela Agenda gradualmente, mantendo uma identidade única para o produto enquanto evoluo sua arquitetura e suas tecnologias.

**Caminho planejado:**

1. **Base atual em Python:** consolidar regras de negócio, cadastros, validações e persistência.
2. **Próxima entrega — aplicação desktop:** transformar a experiência atual de terminal em uma interface gráfica desktop, tornando o uso mais próximo da rotina de um salão.
3. **Evolução da arquitetura:** estruturar melhor as camadas da aplicação, integrar um banco de dados relacional e separar interface, regras de negócio e persistência.
4. **Migração planejada para Java:** reimplementar gradualmente a solução em Java, preservando os requisitos e as regras de negócio da Bela Agenda. Essa etapa faz parte da minha estratégia de evolução e de preparação para integrações futuras com outras interfaces e aplicações.
5. **Visão de longo prazo — aplicativo:** estudar a expansão para uma experiência mobile e outras formas de acesso ao sistema.

A migração para Java e a futura versão em aplicativo são planos de evolução, não funcionalidades já entregues. A prioridade é construir uma base consistente e validar cada etapa antes de avançar.

## O que existe no repositório hoje

O repositório registra a evolução do projeto em Python, desde uma primeira estrutura procedural até uma versão organizada em classes.

### V3 — estrutura orientada a objetos

Arquivo: `bela_agenda_v3.py`

A versão atual em destaque trabalha com as classes:

- `BelaAgenda`: concentra operações de cadastro, validação, listagem e persistência.
- `Usuario`: representa os dados de uma pessoa cliente.
- `Servico`: representa um serviço oferecido pelo salão.
- `Agendamento`: registra cliente, serviço, data, horário e status por meio dos identificadores correspondentes.

Funcionalidades presentes no código:

- Cadastro e listagem de usuários.
- Validação básica de e-mail e verificação de e-mail já cadastrado.
- Validação de telefone com 10 ou 11 dígitos.
- Cadastro e listagem de serviços.
- Validação de duração do serviço.
- Validação de data e hora com `datetime`.
- Criação e listagem de agendamentos.
- Persistência local em arquivos JSON.
- Carregamento dos registros ao iniciar a aplicação.
- Menu interativo executado no terminal, com mensagens formatadas usando Rich.

**Importante sobre o estágio atual:** a V3 é uma aplicação de terminal (CLI). A interface desktop é a próxima direção de desenvolvimento; ela ainda não está implementada nesta versão.

### V2 — validações e persistência

Arquivo: `bela_agenda_v2.py`

Nesta etapa, pratiquei:

- Validação de e-mail e verificação de duplicidade.
- Validação de telefone.
- Validação de data e horário com `datetime`.
- Tratamento de entradas numéricas.
- Cadastro e listagem de usuários e serviços.
- Criação e consulta de agendamentos.
- Salvamento e carregamento de dados em JSON.

### Evolução desde a primeira versão

A primeira etapa foi voltada aos fundamentos de Python, lógica, funções, estruturas de dados e menus. As versões seguintes foram acrescentando validações, persistência e organização do código.

## Tecnologias e conceitos praticados

- Python
- Programação Orientada a Objetos (POO)
- Classes, objetos, atributos e métodos
- Listas e dicionários
- Validação de dados
- Tratamento de exceções
- Manipulação de arquivos
- JSON
- `datetime`
- Rich para formatação da saída no terminal

## Como executar a versão atual

É necessário ter Python instalado.

Instale a dependência utilizada pela V3:

```bash
python -m pip install rich
```

Clone o repositório:

```bash
git clone https://github.com/carolinarope/bela-agenda-python.git
cd bela-agenda-python
```

Execute a versão orientada a objetos:

```bash
python bela_agenda_v3.py
```

Para executar a versão anterior:

```bash
python bela_agenda_v2.py
```

Os arquivos JSON são criados localmente na pasta de execução quando os dados são salvos.

## Próximas melhorias planejadas

- Completar as regras de integridade dos agendamentos, verificando se os IDs de cliente e serviço existem.
- Validar melhor os dados dos serviços, incluindo preço e campos obrigatórios.
- Melhorar a organização entre interface, regras de negócio e persistência.
- Criar uma interface gráfica desktop.
- Migrar a persistência para um banco de dados relacional.
- Planejar a migração gradual das regras de negócio para Java.
- Avaliar uma futura interface mobile/aplicativo.

A lista representa o planejamento do projeto; os itens ainda não implementados não devem ser entendidos como recursos disponíveis.

## Sobre a autora

Sou estudante de Análise e Desenvolvimento de Sistemas e de Desenvolvimento de Sistemas. A Bela Agenda é meu projeto pessoal de longo prazo, no qual pratico programação e transformo aprendizados em etapas de um produto com propósito definido.

Quero evoluir a solução com responsabilidade: entender os fundamentos, testar as regras, melhorar a experiência de uso e documentar cada etapa. Este repositório acompanha essa construção.

**Repositório:** [github.com/carolinarope/bela-agenda-python](https://github.com/carolinarope/bela-agenda-python)
