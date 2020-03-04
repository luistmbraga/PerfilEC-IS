class MenuRegistarUtente:
    def __init__(self, facade):
        self.facade = facade

    def printMenu(self):
        print("+---------REGISTAR UTENTE---------+")

        nome = input("Nome: ")
        sexo = self.escolherSexo()  # escolher dos varios
        moradaDoUtente = input("Morada do utente: ")
        telefoneCasa = input("Telefone de Casa: ")
        telefoneTrabalho = input("Telefone do Trabalho: ")
        estadoCivil = self.escolherEstadoCivil()  # escolher dos varios
        ssn = input("Numero de utente: ")
        cidadania = input("Cidadania: ")
        nacionalidade = input("Nacionalidade: ")

        self.facade.addUtente(nome, sexo, moradaDoUtente, telefoneCasa, telefoneTrabalho, estadoCivil, ssn,
                              cidadania, nacionalidade)

        print("Cliente Registado com sucesso !")

        return

    def escolherSexo(self):
        while True:
            print("Sexo:\n")
            print("\t1  -  Ambíguo\n")  # A
            print("\t2  -  Feminino\n")  # F
            print("\t3  -  Masculino\n")  # M
            print("\t4  -  Não Aplicável\n")  # N
            print("\t5  -  Outro\n")  # O
            print("\t6  -  Desconhecido\n")  # U

            opcao = int(input())

            if opcao == 1:
                sexo = "A"
                break
            if opcao == 2:
                sexo = "F"
                break
            if opcao == 3:
                sexo = "M"
                break
            if opcao == 4:
                sexo = "N"
                break
            if opcao == 5:
                sexo = "O"
                break
            if opcao == 6:
                sexo = "U"
                break
            else:
                print("Opcão Inválida !")

        return sexo

    def escolherEstadoCivil(self):
        while True:
            print("Estado Civil:\n")
            print("\t1  -  Casado\n")  # M
            print("\t2  -  Solteiro\n")  # S
            print("\t3  -  Divorciado\n")  # D
            print("\t4  -  Viúvo\n")  # W

            opcao = int(input())

            if opcao == 1:
                estadoCivil = "M"
                break
            if opcao == 2:
                estadoCivil = "S"
                break
            if opcao == 3:
                estadoCivil = "D"
                break
            if opcao == 4:
                estadoCivil = "W"
                break
            else:
                print("Opcão Inválida !")

        return estadoCivil
