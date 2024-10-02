# models/fisica.py
from models.pessoa import Pessoa
from models.enums import Sexo, EstadoCivil
from abc import ABC, abstractmethod

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

    def __str__(self):
        return (f"\nPessoa Física:\n"
                f"ID: {self.id}\n"
                f"Nome: {self.nome}\n"
                f"Telefone: {self.telefone}\n"
                f"Email: {self.email}\n"
                f"Sexo: {self.sexo.name}\n"  # Assume que Sexo é um Enum
                f"Estado Civil: {self.estado_civil.name}\n"  # Assume que EstadoCivil é um Enum
                f"Data de Nascimento: {self.data_nascimento}")
