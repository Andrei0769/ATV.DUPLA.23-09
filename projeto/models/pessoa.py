# models/pessoa.py
from models.endereco import Endereco

class Pessoa:
    def __init__(self, id: int, nome: str, telefone: str, email: str, endereco: Endereco):
        self.id = id
        self.nome = nome
        self.telefone = telefone
        self.email = email
        self.endereco = endereco

    def validar_dados(self):
        if not self.nome:
            raise ValueError("Nome inválido: O nome não pode ser vazio.")
        if "@" not in self.email:
            raise ValueError("E-mail inválido: Formato de e-mail incorreto.")