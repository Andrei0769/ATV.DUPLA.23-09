from models.pessoa import Pessoa

class Juridica(Pessoa):
    def __init__(self, id: int, nome: str, telefone: str, email: str, endereco, cnpj: str, inscricao_estadual: str):
        # Inicializa os atributos herdados de Pessoa e os exclusivos de Juridica
        super().__init__(id, nome, telefone, email, endereco)
        self.cnpj = cnpj
        self.inscricao_estadual = inscricao_estadual

    def validar_dados(self):
        # Valida os dados herdados de Pessoa
        super().validar_dados()

        # Validação específica para o CNPJ
        if len(self.cnpj) != 14:
            raise ValueError("CNPJ inválido: Deve conter 14 dígitos.")
