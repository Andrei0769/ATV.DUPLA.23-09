from models.juridica import Juridica

class Fornecedor(Juridica):
    def __init__(self, id: int, nome: str, telefone: str, email: str, endereco, cnpj: str, inscricao_estadual: str, produto: str):
        super().__init__(id, nome, telefone, email, endereco, cnpj, inscricao_estadual)
        self.produto = produto

    def validar_dados(self):
        # Valida os dados da classe Juridica
        super().validar_dados()

        # Validação do produto
        if not self.produto:
            raise ValueError("Produto não pode ser vazio.")
