from models.fisica import Fisica

class Cliente(Fisica):
    def __init__(self, id: int, nome: str, telefone: str, email: str, endereco, sexo, estado_civil, data_nascimento: str, protocolo_atendimento: int):
        # Inicializa o Cliente com os atributos herdados e o protocolo de atendimento
        super().__init__(id, nome, telefone, email, endereco, sexo, estado_civil, data_nascimento)
        self.protocolo_atendimento = protocolo_atendimento

    def validar_dados(self):
        # Chama as validações da classe base Fisica
        super().validar_dados()

        # Validação específica para o protocolo de atendimento
        if not isinstance(self.protocolo_atendimento, int) or self.protocolo_atendimento <= 0:
            raise ValueError("Protocolo de atendimento inválido: Deve ser um número inteiro positivo.")

    def __str__(self):
        return (f"\n== Dados Cliente == "
                f"ID: {self.id}\n"
                f"Nome: {self.nome}\n"
                f"Telefone: {self.telefone}\n"
                f"Email: {self.email}\n"
                f"Endereço: {self.endereco}\n"
                f"Sexo: {self.sexo}\n"
                f"Estado Civil: {self.estado_civil}\n"
                f"Data de Nascimento: {self.data_nascimento}\n"
                f"Protocolo de Atendimento: {self.protocolo_atendimento}")
