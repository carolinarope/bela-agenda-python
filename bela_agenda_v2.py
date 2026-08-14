import json

from datetime import datetime


# -----------------------------------------------------------------------------
#                           VALIDAÇÕES
# -----------------------------------------------------------------------------

def validar_email(email):

    if "@" not in email:
        return False, f'\033[31m ERRO Email não possui @\033[m'

    if email.count("@") != 1:
        return False, f'\033[31m ERRO Email deve possuir apenas um @ \033[m'

    usuario, dominio = email.split("@")

    if not usuario or not dominio:
        return False, f'\033[31m ERRO Email incompleto\033[m'

    if "." not in dominio:
        return False, f'\033[31m ERRO dominio precisa de .\033[m'

    return True, "\033[32mEmail válido\033[m"


# -----------------------------------------------------------------------------

def validar_telefone(telefone):

    telefone_limpo = telefone.replace("-", "").replace(" ", "")

    if not telefone_limpo.isdigit():
        return False, f'\033[31m ERRO Telefone deve conter apenas numeros\033[m'

    if len(telefone_limpo) < 10 or len(telefone_limpo) > 11:
        return False, f'\033[31m ERRO Telefone deve conter 10 ou 11 digtos \033[m'

    return True, "\033[32mTelefone válido\033[m"


# -----------------------------------------------------------------------------

def email_ja_existe(email, usuarios):

    for usuario in usuarios:

        if usuario["email"] == email:
            return True

    return False


# -----------------------------------------------------------------------------

def validar_data(data):

    try:
        datetime.strptime(data, "%d/%m/%Y")
        return True, "\033[32mData válida\033[m"

    except ValueError:
        return False, f'\033[31m ERRO Data invalida, use DD/MM/AAAA \033[m'


# -----------------------------------------------------------------------------

def validar_hora(hora):

    try:
        datetime.strptime(hora, "%H:%M")
        return True, "\033[32mHora válida\033[m"

    except ValueError:
        return False, f'\033[31m ERRO Hora invalida, use HH:MM (00:00-23:59) \033[m'


# -----------------------------------------------------------------------------
#                           DADOS INICIAIS
# -----------------------------------------------------------------------------

usuarios = [
    {
        "id": 1,
        "nome": "Carolina Rodrigues",
        "email": "carolinarope@gmail.com",
        "telefone": "999991111"
    }
]

servicos = [
    {
        "id": 1,
        "nome": "Progressiva",
        "preco": 300,
        "duracao": 180
    }
]

agendamentos = []


# -----------------------------------------------------------------------------
#                             USUÁRIOS
# -----------------------------------------------------------------------------

def adicionar_usuario(nome, email, telefone, usuarios):

    valido, mensagem = validar_email(email)

    if not valido:
        print(mensagem)
        return

    if email_ja_existe(email, usuarios):
        print("\033[31m ERRO Email ja existe \033[m")
        return

    valido, mensagem = validar_telefone(telefone)

    if not valido:
        print(mensagem)
        return

    novo_id = len(usuarios) + 1

    novo_usuario = {
        "id": novo_id,
        "nome": nome,
        "email": email,
        "telefone": telefone
    }

    usuarios.append(novo_usuario)

    print(f'\033[32mUsuário {nome} cadastrado com sucesso!\033[m')


# -----------------------------------------------------------------------------

def listar_usuarios():

    for u in usuarios:
        print(u)


# -----------------------------------------------------------------------------
#                               SERVIÇOS
# -----------------------------------------------------------------------------

def adicionar_servico(nome, preco, duracao):

    novo_id = len(servicos) + 1

    novo_servico = {
        "id": novo_id,
        "nome": nome,
        "preco": preco,
        "duracao": duracao
    }

    servicos.append(novo_servico)


# -----------------------------------------------------------------------------

def listar_servicos():

    for u in servicos:
        print(u)


# -----------------------------------------------------------------------------
#                           AGENDAMENTOS
# -----------------------------------------------------------------------------

def criar_agendamento(id_usuario, id_servico, data, hora):

    valido, mensagem = validar_data(data)

    if not valido:
        print(mensagem)
        return

    valido, mensagem = validar_hora(hora)

    if not valido:
        print(mensagem)
        return

    novo_id = len(agendamentos) + 1

    novo_agendamento = {
        "id_agendamento": novo_id,
        "id_us": id_usuario,
        "id_s": id_servico,
        "data": data,
        "hora": hora,
        "status": "Agendado"
    }

    agendamentos.append(novo_agendamento)

    print("Agendamento criado com sucesso!")


# -----------------------------------------------------------------------------

def listar_agendamentos_por_data(data_pesquisada):

    print(f"\n--- Agendamentos para o dia {data_pesquisada} ---")

    encontrou = False

    for a in agendamentos:

        if a["data"] == data_pesquisada:
            print(a)
            encontrou = True

    if encontrou == False:
        print("Nenhum agendamento para esta data.")


# -----------------------------------------------------------------------------
#                             JSON
# -----------------------------------------------------------------------------

def salvar_dados_json():

    with open("usuarios.json", "w") as arquivo:
        json.dump(usuarios, arquivo, indent=4)

    with open("servicos.json", "w") as arquivo:
        json.dump(servicos, arquivo, indent=4)

    with open("agendamentos.json", "w") as arquivo:
        json.dump(agendamentos, arquivo, indent=4)

    print("\033[31mDados salvos com sucesso nos arquivos JSON!\033[m")


# -----------------------------------------------------------------------------

def carregar_dados_json():

    global usuarios, servicos, agendamentos

    try:

        with open("usuarios.json", "r") as arquivo:
            usuarios = json.load(arquivo)

        with open("servicos.json", "r") as arquivo:
            servicos = json.load(arquivo)

        with open("agendamentos.json", "r") as arquivo:
            agendamentos = json.load(arquivo)

        print("\033[31mDados carregados com sucesso!\033[m")

    except FileNotFoundError:

        print(
            "\033[33mArquivos JSON não encontrados. "
            "Começando com os dados padrão.\033[m"
        )


# -----------------------------------------------------------------------------
#                             MENU
# -----------------------------------------------------------------------------

def menu():

    while True:

        print("\033[34m--- Bela Agenda ---\033[m")
        print("1 - Adicionar usuário")
        print("2 - Listar usuários")
        print("3 - Adicionar serviço")
        print("4 - Listar serviços")
        print("5 - Criar agendamento")
        print("6 - Listar agendamentos por data")
        print("7 - Salvar dados em JSON")
        print("8 - Carregar dados de JSON")
        print("9 - Sair")

        opcao = input("Insira uma opção: ").strip()

        if opcao == "1":

            nome_digitado = input("Nome: ").strip()
            email_digitado = input("Email: ").strip()
            telefone_digitado = input("Telefone: ").strip()

            adicionar_usuario(
                nome_digitado,
                email_digitado,
                telefone_digitado,
                usuarios
            )

        elif opcao == "2":

            print("\nListando Usuários..")
            listar_usuarios()

        elif opcao == "3":
            try:
                nome_digitado = input("Nome: ").strip()
                preco_digitado = float(input("Preço: ").strip())
                duracao_digitado = int(input("Duração (minutos): ").strip())

                adicionar_servico(
                    nome_digitado,
                    preco_digitado,
                    duracao_digitado
                )
                print("\033[32mServiço adicionado com sucesso\033[m")
            except ValueError:
                print("\033[31m ERRO: Preço deve ser decimal e duração número inteiro.\033[m")

        elif opcao == "4":

            print("\nListando Serviços..")
            listar_servicos()

        elif opcao == "5":
              try:
                  id_us = int(input("Id Usuário: "))
                  id_s = int(input("Id Serviço: "))
  
                  data_agendamento = input(
                      "Data (DD/MM/AAAA): "
                  ).strip()
  
                  hora_agendamento = input(
                      "Hora (HH:MM): "
                  ).strip()
  
                  criar_agendamento(
                      id_us,
                      id_s,
                      data_agendamento,
                      hora_agendamento
                  )
              except ValueError:
                  print("\033[31m ERRO: Os IDs de usuário e serviço devem ser numéricos.\033[m")
        elif opcao == "6":

            print("\n--- BUSCAR AGENDAMENTOS ---")

            data_busca = input(
                "Qual data deseja buscar (DD/MM/AAAA)? "
            )

            listar_agendamentos_por_data(data_busca)

        elif opcao == "7":

            print("\nSalvando os dados...")
            salvar_dados_json()

        elif opcao == "8":

            print("\nCarregando os dados...")
            carregar_dados_json()

        elif opcao == "9":

            print("\nSaindo do sistema...")
            break

        else:

            print("\033[31mOpção inválida! Tente novamente.\033[m")


# -----------------------------------------------------------------------------
#                           EXECUÇÃO
# -----------------------------------------------------------------------------

if __name__ == "__main__":
    menu()