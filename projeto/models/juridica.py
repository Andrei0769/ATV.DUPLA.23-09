# models/juridica.py

# Importa a classe Pessoa, da qual Juridica irá herdar alguns atributos e métodos.
from models.pessoa import Pessoa

# Define a classe Juridica, que herda de Pessoa.
class Juridica(Pessoa):
    # Construtor da classe Juridica. Ele recebe os mesmos parâmetros de Pessoa (id, nome, telefone, email, endereco)
    # além dos atributos específicos de Juridica, como cnpj e inscricao_estadual.
    def __init__(self, id: int, nome: str, telefone: str, email: str, endereco, cnpj: str, inscricao_estadual: str):
        # Chama o construtor da classe base (Pessoa) para inicializar os atributos herdados.
        super().__init__(id, nome, telefone, email, endereco)
        # Atributos exclusivos da classe Juridica.
        self.cnpj = cnpj
        self.inscricao_estadual = inscricao_estadual

    # Método para validar os dados da classe Juridica.
    def validar_dados(self):
        # Chama o método de validação da classe base (Pessoa) para validar os dados herdados (nome, email, etc.).
        super().validar_dados()

        # Verifica se o CNPJ tem exatamente 14 dígitos.
        # Se não tiver, levanta uma exceção com a mensagem "CNPJ inválido".
        if len(self.cnpj) != 14:
            raise ValueError("CNPJ inválido: Deve conter 14 dígitos.")
