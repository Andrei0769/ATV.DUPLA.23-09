from models.funcionario import Funcionario

class Engenheiro(Funcionario):
    def __init__(self, cpf: str, rg: str, matricula: str, setor: str, salario: float, crea: str):
        super().__init__(cpf, rg, matricula, setor, salario)
        self.crea = crea

    def validar_dados(self):
        # Validações específicas para Engenheiro
        if not self.crea:
            raise ValueError("CREA inválido: O CREA não pode ser vazio.")
        if len(self.crea) != 10:  # Exemplo de validação de tamanho
            raise ValueError("CREA inválido: Deve conter 10 caracteres.")
