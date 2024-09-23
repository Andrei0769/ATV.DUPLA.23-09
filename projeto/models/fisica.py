# models/fisica.py
from models.pessoa import Pessoa
from models.enums import Sexo, EstadoCivil

class Fisica(Pessoa):
    def __init__(self, id: int, nome: str, telefone: str, email: str, endereco, sexo: Sexo, estado_civil: EstadoCivil, data_nascimento: str):
        super().__init__(id, nome, telefone, email, endereco)
        self.sexo = sexo
        self.estado_civil = estado_civil
        self.data_nascimento = data_nascimento

    def validar_dados(self):
        super().validar_dados()
        if not self.data_nascimento:
            raise ValueError("Data de nascimento inválida.")
