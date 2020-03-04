class Utente:
    def __init__(self, idUtente, morada, telefoneCasa, telefoneTrabalho, nome, sexo, estadoCivil, ssn, nacionalidade,
                 cidadania):
        self.idUtente = idUtente
        self.morada = morada
        self.telefoneCasa = telefoneCasa
        self.telefoneTrabalho = telefoneTrabalho
        self.nome = nome
        self.sexo = sexo
        self.estadoCivil = estadoCivil
        self.ssn = ssn
        self.nacionalidade = nacionalidade
        self.cidadania = cidadania

    def toString(self):
        string = "Identificador: " + str(self.idUtente) + "\n"
        string += "Morada: " + self.morada + "\n"
        string += "Telefone de Casa: " + self.telefoneCasa + "\n"
        string += "Telefone do Trabalho: " + self.telefoneTrabalho + "\n"
        string += "Nome: " + self.nome + "\n"
        string += "Sexo: " + self.sexo + "\n"
        string += "Estado Civil: " + self.estadoCivil + "\n"
        string += "Número de Utente de Saúde: " + self.ssn + "\n"
        string += "Nacionalidade: " + self.nacionalidade + "\n"
        string += "Cidadania: " + self.cidadania + "\n\n"
        return string
