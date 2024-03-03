# import data e hora da biblioteca
from datetime import datetime, timedelta

# import json da biblioteca
import json
from unittest import case

# import para random id
import uuid

hoje = datetime.today()
isLogged = False
dadosUsuario = []
dadosEventos = []


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
            return data.strftime("%d/%m/%Y")
        # Retorna somente a parte da data (dia, mês e ano)
        except ValueError:
            print("Formato de data inválido. Tente novamente.")
            continue


def verificar_disponibilidade():
    hora = datetime.strptime(hora, "%H:%M").time()
    data = datetime.strptime(data, "%d/%m/%Y").date()


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
opcoes3Values = opcoes3.keys()
opcoes2Values = opcoes2.keys()
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
            print("Faca seu cadastro;")
            nome = input("Digite seu nome:")
            idade = input("Digite seu idade:")
            cpf = input("Digite seu cpf:")
            email_cadastro = input("Digite seu email:")
            senha_cadastro = input("Digite sua senha:")
            print("Cadastro feito com sucesso!")

            # tentar
            try:
                # ler o conteúdo do arquivo
                with open("cadastro de pessoa.json", "r") as arquivo:
                    # ler o conteúdo da variavel arquivo e armazena na variavel (arquivosCopiados)
                    arquivosCopiados = arquivo.read()
                    # se arquivosCopiados tiver conteudo remove espaco em branco do comeco/final da string
                    if arquivosCopiados.strip():
                        # se tiver conteudo converte de string para json e armazena na variavel (dados_existente)
                        dados_existente = json.loads(arquivosCopiados)
                    else:
                        # se tiver vazia define (dados_existente) como uma array vazia
                        dados_existente = []
            except:
                # define como uma lista vazia se uma excecao for lancada
                dados_existente = []
            # array novo_cadastro
            novo_cadastro = {
                "id": str(uuid.uuid4()),
                "nome": nome,
                "idade": idade,
                "cpf": cpf,
                "email": email_cadastro,
                "senha": senha_cadastro,
                "eventos": [],
            }

            # adicionar o (novo cadastro) aos dados existentes
            dados_existente.append(novo_cadastro)
            # abre o arquivo no modo de escrita na variavel arquivo
            with open("cadastro de pessoa.json", "w") as arquivo:
                # converte (dados_existente) em um objeto json e grava na variavel arquivo
                json.dump(dados_existente, arquivo)
        # se escolha for = 2
        elif escolha == "2":
            email = input("Digite seu email:")
            senha = input("Digite sua senha:")
            # tentar
            try:
                # ler o conteudo do arquivo
                with open("cadastro de pessoa.json", "r") as arquivo:
                    # ler o conteúdo da variavel arquivo e armazena na variavel (arquivosCopiados)
                    arquivosCopiados = arquivo.read()
                    # se arquivosCopiados tiver conteudo remove espaco em branco do comeco/final da string
                    if arquivosCopiados.strip():
                        # se tiver conteudo em (arquivosCopiados) converte de string para json e armazena na variavel (dados_existente)
                        dados_existente = json.loads(arquivosCopiados)
                    else:
                        # se tiver vazia define (dados_existente) como uma array vazia
                        dados_existente = []
            except:
                # define como uma lista vazia se uma excecao for lancada
                dados_existente = []
            # loop por cada item na lista (dados_existente) cada item e atributo a variavel usuario
            for usuario in dados_existente:
                # verifica se o email fornecido e igual ao email armazenado em usuario[email] o mesmo acontece com a senha
                if email == usuario["email"] and senha == usuario["senha"]:
                    # se for igual isLogged se torna True com um login bem sucedido
                    isLogged = True
                    dadosUsuario = usuario
                    # quebra do looping for
                    break
            # se isLogged for igual falso login invalido
            if isLogged == False:
                print("Erro")
                print("Usuário não encontrado!")
        # se digitar um numero que nao esta entre 1 e 2
        else:
            print("Digite um valor válido!")
    # quando isLogged se tornar True apos o login
    else:
        # mostra um bem vindo personalizado com nome dentro da variavel usuario
        print(f"Bem-vindo {usuario['nome']}")
        print(opcoes3)

        evento = print("--------------------------------------")
        evento = input("Selecione uma função:")

        if evento not in opcoes3Values:
            print("Digite um número válido!.")
        # corresponde evento
        match evento:
            case "1":
                # caso escolha 1
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

                print("Evento cadastrado com sucesso")
        # tentar
        try:
            # ler o conteúdo
            with open("cadastro de evento.json", "r") as arquivo:
                # ler o conteúdo da variavel arquivo e armazena na variavel (CopyFiles)
                copyFiles = arquivo.read()
            # se copyFiles tiver conteudo remove espaco em branco do comeco/final da string
            if copyFiles.strip():
                # se tiver conteudo em (CopyFiles) converte de string para json e armazena na variavel (LiveData)
                liveData = json.loads(copyFiles)
            else:
                # se tiver vazia define (LiveData) como uma array vazia
                liveData = []
        except:
            # define como uma lista vazia se uma excecao for lancada
            liveData = []
            # cadastro de evento em uma array
        cadastro_evento = {
                "id": str(uuid.uuid4()),
                "endereco": local,
                "data": data,
                "hora": hora,
                "categoria": categoria,
                "descricao": descricaoEvento,
        }
            # adiciona (cadastro_evento) dentro de liveData
        liveData.append(cadastro_evento)
            # abre o arquivo no modo de escrita na variavel arquivo
        with open("cadastro de evento.json", "w") as arquivo:
                # converte (liveData) em um objeto json e grava na variavel arquivo
            json.dump(liveData, arquivo)

            case "2":
                for evento in liveData:
                    print(f"Seus eventos: {evento['endereco']}, {evento['data']}, {evento['hora']}, {evento['categoria']}, {evento['descricao']}")
        disponibilidade = verificar_disponibilidade(data, hora)
        if hoje >= data:
            print("Evento disponivel!")
        elif hoje == data:
            print("Evento em andamento!")
        else:
            print("Evento encerrado!")

        # case "3":
        # for evento in liveData:
        # print(f"Eventos para serem cancelados: {evento['endereco']}")
        # escolha = str(input("Digite qual evento voce deseja cancelar:"))

    # try:
    # if escolha in liveData:
    # del liveData[liveData.index(escolha)]
    # print("Evento cancelado com sucesso")
    # else:
    # print("Entrada inválida. Digite um nome válido.")
    # except IndexError:
    # print("Evento não encontrado. Verifique o nome digitado.")

    # case "4":
    # isLogged = False
