from datetime import date


class Inscrição:
    def __init__(self, Inscrição_nome:str, Inscrição_Sobrenome:str, Inscrição_Nascimetno:date, Inscrição_Cpf:str, Inscrição_Endereço:str, Inscrição_Cidade:str, Inscrição_Ingresso:str, Inscrição_Curso:str) -> None:
        self.Inscrição_nome = str
        self.Inscrição_Sobrenome = str
        self.Inscrição_Nascimento = date
        self.Incrição_Cpf = str
        self.Inscrição_Endereço = str
        self.Inscrição_Cidade = str,
        self.Inscrição_Ingresso = str
        self.Inscrição_Curso = str
    
    def obter_Inscrição(self)-> None:
        print("Insira os seus dados para realizar a inscrição:")