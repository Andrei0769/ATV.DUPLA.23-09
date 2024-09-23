from models.juridica import Juridica

class PrestacaoServico(Juridica):
    def __init__(self, id: int, nome: str, telefone: str, email: str, endereco, cnpj: str, inscricao_estadual: str, contrato_inicio: str, contrato_fim: str):
        super().__init__(id, nome, telefone, email, endereco, cnpj, inscricao_estadual)
        self.contrato_inicio = contrato_inicio
        self.contrato_fim = contrato_fim

    def validar_dados(self):
        # Valida os dados da classe Juridica
        super().validar_dados()
        
        # Validação dos contratos
        if not self.contrato_inicio:
            raise ValueError("Data de início do contrato não pode ser vazia.")
        if not self.contrato_fim:
            raise ValueError("Data de término do contrato não pode ser vazia.")
