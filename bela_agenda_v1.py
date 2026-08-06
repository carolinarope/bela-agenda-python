import json

usuarios = [
    {"id": 1, "nome": "Maria Aparecida", "email": "mariaap@...", "telefone": "999991111"}
]
servicos = [
    {"id": 1, "nome": "Progressiva", "preco": 300, "duracao": 180}
]
agendamentos = []


def adicionar_usuario(nome,email,telefone):
    novo_id = len(usuarios) + 1
 
    novo_usuario = {
    "id": novo_id,
    "nome": nome,
    "email": email,
    "telefone": telefone
    }


    usuarios.append(novo_usuario)
    print ("Usuário cadastrado com sucesso!")


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

        opcao = (input("Insira uma opção: ")).strip()

        if opcao == "1":
            nome_digitado = input("Nome: ")
            email_digitado = input("Email: ")
            telefone_digitado = input("Telefone: ")


            adicionar_usuario( nome_digitado,email_digitado,telefone_digitado ) 

        elif opcao == "2":
                print("\nListando Usuários..")
                listar_usuarios()
        elif  opcao == "3":
            nome_digitado = input("Nome: ")
            preco_digitado = (input("Preco: "))
            duracao_digitado = (input("Duração: "))

            adicionar_servico(nome_digitado,preco_digitado,duracao_digitado )

            print("Serviço adicionado com sucesso")

        elif opcao == "4":
             print("\nListando Serviços..")
             listar_servicos()

        elif opcao == "5":
             
             id_us = int(input("Id Usuário: "))
             id_s = int(input("Id Serviço"))
             data_agendamento = input("Data (DD/MM/AAAA): ")
             hora_agendamento = input("Hora (HH:MM): ")

             criar_agendamento(id_us,id_s,data_agendamento,hora_agendamento)

        elif opcao == "6":
            print("\n--- BUSCAR AGENDAMENTOS ---")
            data_busca = input("Qual data deseja buscar (DD/MM/AAAA)? ")

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



def listar_usuarios():
    for u in usuarios:
        print(u)

def adicionar_servico(nome,preco,duracao):

    novo_id = len(servicos) + 1
    novo_servico = {
           
        "id": novo_id,
        "nome": nome,
        "preco": preco,
        "duracao": duracao
    }        
    servicos.append(novo_servico)

def listar_servicos():
    for u in servicos:
            print(u)

def criar_agendamento(id_usuario,id_servico,data,hora):

    novo_id = len(agendamentos) + 1
    novo_agendamento = {
        "id_agendamento": novo_id,
        "id_us": id_usuario,
        "id_s": id_servico,
        "data":data,
        "hora": hora,
        "status":"Agendado"
    }
    agendamentos.append(novo_agendamento)
    print("Agendamento criado com sucesso!")



def listar_agendamentos_por_data(data_pesquisada):
    print(f"\n--- Agendamentos para o dia {data_pesquisada} ---")
    
    encontrou = False 
    
    for a in agendamentos:
        
        if a["data"] == data_pesquisada:
            print(a) 
            encontrou = True
            
    if encontrou == False:
        print("Nenhum agendamento para esta data.")


def salvar_dados_json():
  
    with open("usuarios.json", "w") as arquivo:
        json.dump(usuarios, arquivo, indent=4)
        
  
    with open("servicos.json", "w") as arquivo:
        json.dump(servicos, arquivo, indent=4)
        
    
    with open("agendamentos.json", "w") as arquivo:
        json.dump(agendamentos, arquivo, indent=4)
        
    print("\033[32mDados salvos com sucesso nos arquivos JSON!\033[m")

def carregar_dados_json():
   
    global usuarios, servicos, agendamentos
    
    try:
        
        with open("usuarios.json", "r") as arquivo:
            usuarios = json.load(arquivo)
            
        with open("servicos.json", "r") as arquivo:
            servicos = json.load(arquivo)
            
        with open("agendamentos.json", "r") as arquivo:
            agendamentos = json.load(arquivo)
            
        print("\033[32mDados carregados com sucesso!\033[m")
        
    except FileNotFoundError:
        
        print("\033[33mArquivos JSON não encontrados. Começando com os dados padrão.\033[m")   
if __name__ == "__main__":
    menu()