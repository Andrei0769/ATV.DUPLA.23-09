from abc import ABC, abstractmethod

class Funcionario(ABC):
    def __init__(self, cpf: str, rg: str, matricula: str, setor: str, salario: float):
        # Inicializa os atributos do funcionário
        self.cpf = cpf
        self.rg = rg
        self.matricula = matricula
        self.setor = setor
        self.salario = salario

    # Método abstrato a ser implementado nas subclasses
    @abstractmethod
    def validar_dados(self):
        pass

    def __str__(self):
        return (f"\n== Dados Funcionario == "
                f"Funcionário:\n"
                f"CPF: {self.cpf}\n"
                f"RG: {self.rg}\n"
                f"Matrícula: {self.matricula}\n"
                f"Setor: {self.setor}\n"
                f"Salário: R$ {self.salario:.2f}")
