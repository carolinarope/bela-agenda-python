import json
from rich import print
from datetime import datetime
class BelaAgenda:
    '''
    Classe para gerenciar o agendamento de serviços.
    '''
    def __init__(self):
        self.usuarios = []
        self.servicos = []
        self.agendamentos = []


    def validar_email(self, email):
        '''
        Função para validar o formato do email.
        '''

        if "@" not in email or "." not in email:
            return False,'[red]Email inválido. Certifique-se de que o email contém "@" e "."[/]'

        if email.count("@") != 1:
            return False,'[red]Email inválido. Certifique-se de que o email contém apenas um "@"[/]'

        if email.startswith("@") or email.endswith("@"):
            return False,'[red]Email inválido. Certifique-se de que o email não começa ou termina com "@"[/]'

        if email.startswith(".") or email.endswith("."):
            return False,'[red]Email inválido. Certifique-se de que o email não começa ou termina com "."[/]'

        if ".." in email:
            return False,'[red]Email inválido. Certifique-se de que o email não contém ".."[/]' 

        return True,'[green]Email válido.[/]'


    def email_existe(self, email):
        '''
        Função para verificar se o email já existe na lista de usuários.
        '''

        for usuario in self.usuarios:
            if usuario.email == email:
                return True,'[red]Email já cadastrado.[/]'
        return False,'[green]Email disponível.[/]'


    def validar_telefone(self, telefone):
        '''
        Função para validar o formato do telefone.
        '''

        if not telefone.isdigit():
            return False,'[red]Telefone inválido. Certifique-se de que o telefone contém apenas números.[/]'

        if len(telefone) < 10 or len(telefone) > 11:
            return False,'[red]Telefone inválido. Certifique-se de que o telefone contém 10 ou 11 dígitos.[/]'
    
        return True,'[green]Telefone válido.[/]'    


    def validar_data_hora(self, data_hora):
        '''
        Função para validar o formato da data e hora.
        '''

        try:
            datetime.strptime(data_hora, "%d/%m/%Y %H:%M")
            return True,'[green]Data e hora válidas.[/]'
        except ValueError:
            return False,'[red]Data e hora inválidas. Certifique-se de que o formato está correto (dd/mm/yyyy hh:mm).[/]'       


    def validar_duracao(self, duracao):
        '''
        Função para validar o formato da duração.
        '''

        try:
            duracao_int = int(duracao)
            if duracao_int <= 0:
                return False,'[red]Duração inválida. Certifique-se de que a duração é um número positivo.[/]'
            return True,'[green]Duração válida.[/]'
        except ValueError:
            return False,'[red]Duração inválida. Certifique-se de que a duração é um número inteiro.[/]'


    def adicionar_usuario(self, nome, email, telefone):
        '''
        Função para adicionar um novo usuário.
        '''
    
        valido,msg = self.validar_email(email) #validação do email
        if not valido:
            return False,msg  


        if self.email_existe(email)[0]:
            return False,'[red]Email já cadastrado.[/]'

        
        valido,msg = self.validar_telefone(telefone) #validação do telefone
        if not valido:
            return False,msg   

    
        novo_id_usuario = len(self.usuarios) + 1

        usuario = Usuario(novo_id_usuario, nome, email, telefone) 

        self.usuarios.append(usuario)
        return True,'[green]Usuário adicionado com sucesso.[/]'


    def listar_usuarios(self):
        '''
        Função para listar todos os usuários.
        '''

        if not self.usuarios:
            return '[yellow]Nenhum usuário cadastrado.[/]'
        
        usuarios_str = "[bold]Lista de Usuários:[/]\n"
        for usuario in self.usuarios:
            usuarios_str += f"ID: {usuario.id_usuario}, Nome: {usuario.nome}, Email: {usuario.email}, Telefone: {usuario.telefone}\n"

        return usuarios_str


    def adicionar_servico(self, nome, duracao, preco):
        '''
        Função para adicionar um novo serviço.
        '''

        valido,msg = self.validar_duracao(duracao)
        if not valido:
            return False,msg  

        novo_id_servico = len(self.servicos) + 1
        
        servico = Servico(novo_id_servico, nome, duracao, preco)
        self.servicos.append(servico)

        return True,'[green]Serviço adicionado com sucesso.[/]'

    
    def listar_servicos(self):
        '''
        Função para listar todos os serviços.
        '''

        if not self.servicos:
            return '[yellow]Nenhum serviço cadastrado.[/]'
        
        servicos_str = "[bold]Lista de Serviços:[/]\n"
        for servico in self.servicos:
            servicos_str += f"ID: {servico.id_servico}, Nome: {servico.nome}, Duração: {servico.duracao}, Preço: {servico.preco}\n"

        return servicos_str

    def adicionar_agendamento(self, id_usuario, id_servico, data_hora):
        '''
        Função para adicionar um novo agendamento.
        '''

        valido,msg = self.validar_data_hora(data_hora)
        if not valido:
            return False,msg  

        novo_id_agendamento = len(self.agendamentos) + 1
        
        agendamento = Agendamento(novo_id_agendamento, id_usuario, id_servico, data_hora,status="Agendado")
        self.agendamentos.append(agendamento)

        return True,'[green]Agendamento adicionado com sucesso.[/]' 


    def salvar_dados(self):
        '''
        Função para salvar os dados em arquivos JSON.
        '''

        with open('usuarios.json', 'w') as f:
            json.dump([usuario.__dict__ for usuario in self.usuarios], f, indent=4)

        with open('servicos.json', 'w') as f:
            json.dump([servico.__dict__ for servico in self.servicos], f, indent=4)

        with open('agendamentos.json', 'w') as f:
            json.dump([agendamento.__dict__ for agendamento in self.agendamentos], f, indent=4)


    def carregar_dados(self):
        '''
        Função para carregar os dados de arquivos JSON.
        '''

        try:
            with open('usuarios.json', 'r') as f:
                usuarios_data = json.load(f)
                self.usuarios = [Usuario(**usuario) for usuario in usuarios_data]
        except FileNotFoundError:
            self.usuarios = []

        try:
            with open('servicos.json', 'r') as f:
                servicos_data = json.load(f)
                self.servicos = [Servico(**servico) for servico in servicos_data]
        except FileNotFoundError:
            self.servicos = []

        try:
            with open('agendamentos.json', 'r') as f:
                agendamentos_data = json.load(f)
                self.agendamentos = [
    Agendamento(
        agendamento["id_agendamento"],
        int(agendamento["id_usuario"]),
        int(agendamento["id_servico"]),
        agendamento["data_hora"],
        agendamento.get("status", "Pendente")
    )
    for agendamento in agendamentos_data
]
                
        except FileNotFoundError:
            self.agendamentos = []
   
    
            
class Usuario:
    '''
    Classe para representar um usuário do sistema.
    '''

    def __init__(self,id_usuario, nome, email, telefone):
        self.id_usuario = id_usuario
        self.nome = nome
        self.email = email
        self.telefone = telefone


class Servico:
    '''
    Classe para representar um serviço do sistema.
    '''

    def __init__(self, id_servico, nome, duracao, preco):
        self.id_servico = id_servico
        self.nome = nome
        self.duracao = duracao
        self.preco = preco        


class Agendamento:
    '''
    Classe para representar um agendamento do sistema.
    '''

    def __init__(self, id_agendamento,id_usuario, id_servico, data_hora, status="Pendente"):
        self.id_agendamento = id_agendamento
        self.id_usuario = id_usuario
        self.id_servico = id_servico
        self.data_hora = data_hora
        self.status = status  # Status inicial do agendamento


agenda=BelaAgenda()
agenda.carregar_dados()


def menu():
    while True:
        print("[bold cyan]Bem-vindo ao Sistema de Agendamento Bela Agenda [/]")
        print("[bold]Selecione uma opção:[/]")
        print("1. Adicionar Usuário")
        print("2. Listar Usuários")
        print("3. Adicionar Serviço")
        print("4. Listar Serviços")
        print("5. Adicionar Agendamento")
        print("6. Listar Agendamentos")
        print("7. Sair")

        opcao = input("Digite o número da opção desejada: ").strip()

        if opcao not in ["1", "2", "3", "4", "5", "6", "7"]:
            print("[red]Opção inválida. Por favor, selecione uma opção válida.[/]")
            continue
    
        if opcao == "1":
            print("[bold]Adicionar Usuário[/]")
            nome = input("Digite o nome : ").strip()
            email = input("Digite o email : ").strip()
            telefone = input("Digite o telefone (apenas números): ").strip()
            sucesso,msg = agenda.adicionar_usuario(nome, email, telefone)
            print(msg)


        if opcao == "2":
            print(agenda.listar_usuarios())

        if opcao == "3":
            print("[bold]Adicionando Serviço:[/]")
            nome = input("Digite o nome do serviço: ").strip()
            duracao = input("Digite a duração do serviço (em minutos): ").strip()
            preco = input("Digite o preço do serviço: ").strip()
            sucesso,msg = agenda.adicionar_servico(nome, duracao, preco)
            print(msg)


        if opcao == "4":
            print(agenda.listar_servicos())


        if opcao == "5":
            print("[bold]Adicionando Agendamento:[/]")
           
            if not agenda.usuarios:
                    print("[yellow]Nenhum usuário cadastrado. Por favor, adicione um usuário antes de agendar.[/]")
                    continue
            if not agenda.servicos:
                    print("[yellow]Nenhum serviço cadastrado. Por favor, adicione um serviço antes de agendar.[/]")
                    continue
            try:
                id_usuario = int(input("Digite o ID do usuário: ").strip())
                id_servico = int(input("Digite o ID do serviço: ").strip())
                data_hora = input("Digite a data e hora do agendamento (dd/mm/yyyy hh:mm): ").strip()

                sucesso,msg = agenda.adicionar_agendamento(id_usuario, id_servico, data_hora)
                print(msg)

            except ValueError:
                print("[red]ID inválido. Certifique-se de que os IDs são números inteiros.[/]")
                

        if opcao == "6":
            if not agenda.agendamentos:
                print("[yellow]Nenhum agendamento cadastrado.[/]")

            else:
                print("[bold]Lista de Agendamentos:[/]")
                
                for agendamento in agenda.agendamentos:
                    usuario = next((u for u in agenda.usuarios if u.id_usuario == agendamento.id_usuario), None)
                    servico = next((s for s in agenda.servicos if s.id_servico == agendamento.id_servico), None)

                    if usuario and servico:
                        print(f"ID: {agendamento.id_agendamento}, Usuário: {usuario.nome}, Serviço: {servico.nome}, Data e Hora: {agendamento.data_hora}, Status: {agendamento.status}")

                    else:
                        print(f"[red]Erro ao encontrar usuário ou serviço para o agendamento ID: {agendamento.id_agendamento}[/]")  

               
        if opcao == "7":
            print("[bold green]Saindo do sistema. Até logo![/]")

            salvar = input("Deseja salvar os dados antes de sair? (s/n): ").strip().lower()
            
            if salvar == "s":
                agenda.salvar_dados()
                print("[green]Dados salvos com sucesso![/]")
            break

if __name__ == "__main__":
    menu()