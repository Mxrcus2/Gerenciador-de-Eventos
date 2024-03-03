# import data e hora da biblioteca
from datetime import datetime, timedelta

hoje = datetime.now()
eventos_disponiveis = []
eventos_encerrados = []

eventos = [
    {
        "data": "2024-03-26",
        "hora": "10:00",
        "titulo": "Evento 1",
        "descricao": "Futebol",
        "status": "disponivel",
    },
    {
        "data": "2023-12-05",
        "hora": "14:00",
        "titulo": "Evento 2",
        "descricao": "Festa",
        "status": "encerrado",
    },
    {
        "data": "2024-11-20",
        "hora": "12:00",
        "titulo": "Evento 3",
        "descricao": "Show eletronico",
        "status": "disponivel",
    },
]

opcoes = {1: "Cadastro de Usuário", 2: "Cadastro de Evento", 3: "Login"}

opcoes2 = {
    1: "Festa",
    2: "Shows",
    3: "Eventos esportivos",
}

opcoes3 = {
    1: "Participar de eventos",
    2: "Ver meus eventos",
    3: "Cancelar eventos",
    4: "Deslogar",
}

print("Digite sua escolha:")
print(opcoes)

escolha = int(input("Qual opcao deseja: "))

if escolha in opcoes:
    if escolha == 1:
        print("Faca seu cadastro;")
        nome = input("Digite seu nome:")
        idade = input("Digite seu idade:")
        cpf = input("Digite seu cpf:")
        email_cadastro = input("Digite seu email:")
        senha_cadastro = input("Digite sua senha:")
        print("Cadastrado com sucesso! ")
        print(opcoes)

if escolha in opcoes:
    if escolha == 2:
        print("Selecione uma categoria:")
        input(opcoes2)
        if escolha in opcoes2:
            if escolha == 1:
                print("Caterogia: Festa")
                input("Digite o endereco")
                input("Digite a data do evento no formato dd/MM/yyyy:")
                input("Digite o horário no seguinte formato HH:mm:ss:")
                input("Digite uma descrição:")
                print("Evento cadastrado com sucesso")
                print(opcoes)
            elif escolha == 2:
                print("Caterogia: Shows")
                input("Digite o endereco:")
                input("Digite a data do evento no formato dd/MM/yyyy:")
                input("Digite o horário no seguinte formato HH:mm:ss:")
                input("Digite uma descrição:")
                print("Evento cadastrado com sucesso")
                print(opcoes)
            elif escolha == 3:
                print("Caterogia: Eventos esportivos")
                input("Digite o endereco:")
                input("Digite a data do evento no formato dd/MM/yyyy:")
                input("Digite o horário no seguinte formato HH:mm:ss:")
                input("Digite uma descrição:")
                print("Evento cadastrado com sucesso")
                print(opcoes)

if escolha in opcoes:
    if escolha == 3:
        email = input("Digite seu email:")
        senha = input("Digite sua senha:")

        with open("login teste.txt", "w") as arquivo:
            arquivo.write("email:" + email + "\n")
            arquivo.write("senha:" + senha + "\n")

        with open("login teste.txt", "r") as arquivo:
            conteudo = arquivo.read()
            email_lido = conteudo.split("\n")[0].split(":")[1].strip()
            senha_lido = conteudo.split("\n")[1].split(":")[1].strip()

        if email == email_lido and senha == senha_lido:
            print("Login realizado com sucesso")
            print(opcoes3)
        else:
            print("Login invalido")

match escolha in opcoes3:
    case 1:

        for evento in eventos:
            data_evento = datetime.strptime(
                evento["data"] + " " + evento["hora"], "%Y-%m-%d %H:%M"
            )
            if evento["status"] == "disponivel" and data_evento >= hoje:
                eventos_disponiveis.append(evento)
            elif evento["status"] == "encerrado" and data_evento < hoje:
                eventos_encerrados.append(evento)

        print("Eventos disponíveis:")
        # Adicione a indentação para as linhas dentro do loop
        for evento in eventos_disponiveis:
            # Exiba as informações do evento
            print(
                f"- {evento['titulo']}: {evento['data']} {evento['hora']} - {evento['descricao']}"
            )

        print("Eventos encerrados:")
        # Adicione a indentação para as linhas dentro do loop
        for evento in eventos_encerrados:
            # Exiba as informações do evento
            print(
                f"- {evento['titulo']}: {evento['data']} {evento['hora']} - {evento['descricao']}"
            )
