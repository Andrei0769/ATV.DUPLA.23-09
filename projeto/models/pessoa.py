# models/pessoa.py

from models.endereco import Endereco
from abc import ABC, abstractmethod

class Pessoa(ABC):
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

    def __str__(self):
        return (f"\nDados Pessoa:\n"
                f"ID: {self.id}\n"
                f"Nome: {self.nome}\n"
                f"Telefone: {self.telefone}\n"
                f"Email: {self.email}\n"
                f"Endereço: {str(self.endereco)}") 
