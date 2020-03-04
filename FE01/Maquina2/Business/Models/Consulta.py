class Consulta:
    def __init__(self, idConsulta, idUtente, nomeMedico, data):
        self.idConsulta = idConsulta
        self.idUtente = idUtente
        self.nomeMedico = nomeMedico
        self.data = data

    def toString(self):
        string = "Identificador da Consulta: " + str(self.idConsulta) + "\n"
        string += "Identificador do Utente: " + str(self.idUtente) + "\n"
        string += "Nome do Médico que atendeu: " + self.nomeMedico + "\n"
        string += "Data da Consulta: " + str(self.data) + "\n\n"
        return string