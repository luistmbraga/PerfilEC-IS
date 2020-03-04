class Exame:
    def __init__(self, idExame, idConsulta, estado, relatorio, informacaoClinica, exameCodigo):
        self.idExame = idExame
        self.estado = estado
        self.idConsulta = idConsulta
        self.relatorio = relatorio
        self.informacaoClinica = informacaoClinica
        self.exameCodigo = exameCodigo

    def toString(self):
        string = "Identificador do Exame: " + str(self.idExame) + "\n"
        string += "Estado do Exame: " + self.estado + "\n"
        string += "Consulta em que o exame foi pedido: " + str(self.idConsulta) + "\n"
        string += "Relatorio: " + str(self.relatorio) + "\n"
        string += "Informação Clínica: " + self.informacaoClinica + "\n"
        string += "Código do Exame: " + self.exameCodigo + "\n\n"
        return string