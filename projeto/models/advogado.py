from models.funcionario import Funcionario

class Advogado(Funcionario):
    def __init__(self, cpf: str, rg: str, matricula: str, setor: str, salario: float, oab: str):
        # Inicializa o Advogado com os atributos herdados e a OAB
        super().__init__(cpf, rg, matricula, setor, salario)
        self.oab = oab

    def validar_dados(self):
        # Validações específicas para o atributo OAB
        if not self.oab:
            raise ValueError("OAB inválida: A OAB não pode ser vazia.")
        
        if len(self.oab) != 9:  # Exemplo: validação de tamanho da OAB
            raise ValueError("OAB inválida: Deve conter 9 caracteres.")
