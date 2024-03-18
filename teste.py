# import data e hora da biblioteca
from datetime import datetime, timedelta

# import json da biblioteca
import json
import os

# import para random id
import uuid

from errorType import CustomError

isLogged = False
dadosUsuario = {}
usuario_id = str(uuid.uuid4())


def obter_categoria():
    while True:
        try:
            categoria = int(input("selecione uma categoria: "))
            if categoria not in opcoes2Values:
                raise ValueError
            return opcoes2[categoria]
        except ValueError:
            print("Digite uma categoria valida!")
            continue


def obter_data():
    while True:
        try:
            data_input = input("Digite a data (DD/MM/AAAA): ")
            data = datetime.strptime(data_input, "%d/%m/%Y").date()
            # Retorna somente a parte da data (dia, mês e ano)
            return data.strftime("%d/%m/%Y")
        except ValueError:
            print("Formato de data inválido. Tente novamente.")
            continue


def login(email, senha, dados_existente):
    if email in dados_existente["usersById"]:
        if dados_existente["usersById"][email]["senha"] == senha:
            return True, dados_existente["usersById"][email]
        else:
            print("Senha Incorreta. Tente novamente!")
            return False, None
    else:
        print("Usuário não encontrado. Tente novamente!")
        return False, None


opcoes = {
    1: "Cadastro de Usuário",
    2: "Login",
}

opcoes2 = {
    1: "Festa",
    2: "Shows",
    3: "Eventos esportivos",
}

opcoes3 = {
    1: "Cadastrar evento",
    2: "Ver meus eventos",
    3: "Cancelar eventos",
    4: "Deslogar",
}
# retorna todas as chaves da array
opcoes3Values = list(opcoes3.keys())
opcoes2Values = list(opcoes2.keys())
# enquanto for verdadeiro
while True:
    # se isLogged for = Falso
    if isLogged == False:
        print("-----------------------------------------------")
        print("Digite sua escolha:")
        print(opcoes)
        escolha = input("Qual opcao deseja: ")
        # se escolha for igual a 1
        if escolha == "1":

            # tentar
            try:
                # Verificar se o arquivo JSON existe e não está vazio
                if (
                    os.path.exists("cadastro_de_pessoa.json")
                    # verifica se o arquivo json existe e se o tamanho e maior que 0
                    and os.path.getsize("cadastro_de_pessoa.json") > 0
                ):
                    # ler o conteúdo do arquivo
                    with open("cadastro_de_pessoa.json", "r") as arquivo:
                        # ler o conteúdo da variavel arquivo e armazena na variavel (dados_existente)
                        dados_existente = json.load(arquivo)
                else:
                    # Se o arquivo estiver vazio, inicializar dados_existente o objeto usersById e o array allUsersById
                    dados_existente = {"usersById": {}, "allUsersById": []}

                # Definir o novo usuário
                print("Faca seu cadastro;")
                nome = input("Digite seu nome:")
                idade = input("Digite seu idade:")
                email_cadastro = input("Digite seu email:")
                if (
                    dados_existente["usersById"]
                    and dados_existente["usersById"][email_cadastro]
                ):
                    raise CustomError("Email ja existente!")
                senha_cadastro = input("Digite sua senha:")
                cpf = input("Digite seu cpf:")

                novo_cadastro = {
                    "id": str(uuid.uuid4()),
                    "nome": nome,
                    "idade": idade,
                    "cpf": cpf,
                    "email": email_cadastro,
                    "senha": senha_cadastro,
                    "eventos": {
                        "eventsById": {},
                        "allEventsById": [],
                    },
                }

                # Adicionar o novo cadastro ao objeto usersById
                dados_existente["usersById"][novo_cadastro["email"]] = novo_cadastro
                # adicionar o ID do novo cadastro aos dados existentes
                dados_existente["allUsersById"].append(novo_cadastro["id"])
                # abre o arquivo no modo de escrita na variavel arquivo
                with open("cadastro_de_pessoa.json", "w") as arquivo:
                    # converte (dados_existente) em um objeto json e grava na variavel arquivo
                    json.dump(dados_existente, arquivo, indent=4)

                print("Cadastro feito com sucesso!")
            except CustomError as erro:
                print("Não foi possível criar o cadastro:", erro)
                continue
        # se escolha for = 2
        elif escolha == "2":
            email = input("Digite seu email:")
            senha = input("Digite sua senha:")
            # tentar
            try:
                # ler o conteudo do arquivo
                with open("cadastro_de_pessoa.json", "r") as arquivo:
                    # ler o conteúdo do arquivo e armazenar na variável dados_existente
                    dados_existente = json.load(arquivo)

                isLogged, userData = login(email, senha, dados_existente)

                if isLogged:
                    print("Login bem sucedido!")
                    dadosUsuario = userData
                else:
                    print("Falha no login.")

            except Exception as e:
                print("Não foi possível se conectar ao banco de dados:", e)
    else:
        # mostra um bem vindo personalizado com nome dentro da variavel usuario
        print(f"Bem-vindo {dadosUsuario['nome']}")
        print(opcoes3)

        evento = print("--------------------------------------")
        evento = int(input("Selecione uma função:"))

        if evento not in opcoes3Values:
            print("Digite um número válido!.")
            continue
        else:
            # corresponde evento
            match evento:
                # caso escolha 1
                case 1:
                    try:
                        with open("cadastro_de_pessoa.json", "r") as arquivo:
                            # ler o conteúdo da variavel arquivo e armazena na variavel (dados_existente)
                            dados_existente = json.load(arquivo)

                        local = input("Digite o endereco:")
                        # pegar funcao (obter_data)
                        data = obter_data()
                        print(data)
                        hora = input("Digite o horário no seguinte formato (HH:mm:):")
                        print(opcoes2)
                        # pegar funcao (obter_categoria)
                        categoria = obter_categoria()
                        print(f"Voce selecionou a categoria: {categoria}")
                        descricaoEvento = input("Digite uma descrição:")
                        eventoId = str(uuid.uuid4())
                        cadastro_evento = {
                            "isDeleted": False,
                            "id": eventoId,
                            "endereco": local,
                            "data": data,
                            "hora": hora,
                            "categoria": categoria,
                            "descricao": descricaoEvento,
                        }
                        user_email = dadosUsuario["email"]
                        userEvents = dados_existente["usersById"][user_email]["eventos"]
                        # se nao tiver nada em eventsById, volta como um dicionario vazio
                        if not userEvents["eventsById"]:
                            userEvents["eventsById"] = {}
                        userEvents["eventsById"][eventoId] = cadastro_evento
                        # adiciona o eventoId dentro da array allEventsById
                        userEvents["allEventsById"].append(eventoId)
                        dadosUsuario = dados_existente["usersById"][user_email]
                        with open("cadastro_de_pessoa.json", "w") as arquivo:
                            # converte (dados_existente) em um objeto json e grava na variavel arquivo
                            json.dump(dados_existente, arquivo, indent=4)

                        print("Evento cadastrado com sucesso")
                    except CustomError as erro:
                        print("Não foi possível criar o evento:", erro)
                        continue

                case 2:
                    print("--------------------------------------")
                    print("Seus eventos:")
                    total_de_eventos_cadastrados = 0
                    # se o tamanho d eventos for 0
                    if len(dadosUsuario["eventos"]) > 0:
                        # O loop for itera sobre os eventos do usuário, armazenando o ID do evento (eventoId) e o dicionário do evento (evento) em cada iteração
                        for eventoId, evento in dadosUsuario["eventos"][
                            "eventsById"
                        ].items():
                            if evento["isDeleted"] == True:
                                continue
                            hoje = datetime.today()
                            # Converte a string da hora para datetime
                            evento_hora_datetime = datetime.strptime(
                                evento["data"] + " " + evento["hora"], "%d/%m/%Y %H:%M"
                            )

                            if hoje > evento_hora_datetime:
                                print(
                                    f"Evento - {eventoId} - {evento['endereco']} - Encerrado!"
                                )
                            elif hoje == evento_hora_datetime:
                                print(
                                    f"Evento - {eventoId} - {evento['endereco']} - Em Andamento!"
                                )
                            else:
                                print(
                                    f"Evento - {eventoId} - {evento['endereco']} - Disponível!"
                                )
                            total_de_eventos_cadastrados += 1

                        print("--------------------------------------")
                    else:
                        print("Nenhum evento cadastrado.")
                        print("--------------------------------------")
                    if total_de_eventos_cadastrados == 0:
                        print("Nenhum evento cadastrado!")
                        print("--------------------------------------")
                case 3:
                    print("--------------------------------------")
                    eventoId = input("Digite um id para ser cancelado: ")
                    # se nao tiver evento disponivel em evento id
                    if not dadosUsuario["eventos"]["eventsById"][eventoId]:
                        print("Evento nao encontrado")
                        continue
                    with open("cadastro_de_pessoa.json", "r") as arquivo:
                        # ler o conteúdo da variavel arquivo e armazena na variavel (dados_existente)
                        dados_existente = json.load(arquivo)
                    user_email = dadosUsuario["email"]
                    evento = dados_existente["usersById"][user_email]["eventos"][
                        "eventsById"
                    ][eventoId]
                    evento["isDeleted"] = True
                    with open("cadastro_de_pessoa.json", "w") as arquivo:
                        json.dump(dados_existente, arquivo, indent=4)
                    print(f"Evento {evento['endereco']} cancelado com sucesso")
                    dadosUsuario["eventos"]["eventsById"][eventoId] = evento

                case 4:
                    isLogged = False
                    dadosUsuario = {}
