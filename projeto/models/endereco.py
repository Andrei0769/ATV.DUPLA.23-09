# models/endereco.py
from models.enums import UnidadeFederativa

class Endereco:
    def __init__(self, logradouro: str, numero: str, complemento: str, cep: str, cidade: str, uf: UnidadeFederativa):
        self.logradouro = logradouro
        self.numero = numero
        self.complemento = complemento
        self.cep = cep
        self.cidade = cidade
        self.uf = uf

    def __str__(self):
        return (f"\n== Dados Endereço == "
                f"\n{self.logradouro}, \n{self.numero}, \n{self.complemento}, "
                f"{self.cidade} - \n{self.uf}, \n{self.cep}")
