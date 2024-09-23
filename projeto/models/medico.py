from models.funcionario import Funcionario

class Medico(Funcionario):
    def __init__(self, cpf: str, rg: str, matricula: str, setor: str, salario: float, crm: str):
        super().__init__(cpf, rg, matricula, setor, salario)
        self.crm = crm

    def validar_dados(self):
        # Validações específicas para Médico
        if not self.crm:
            raise ValueError("CRM inválido: O CRM não pode ser vazio.")
        if len(self.crm) != 6:  # Exemplo de validação de tamanho
            raise ValueError("CRM inválido: Deve conter 6 caracteres.")
