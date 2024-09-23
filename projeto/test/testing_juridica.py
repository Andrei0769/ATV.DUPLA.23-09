# tests/juridica/test_juridica.py

# Importa o pytest, uma biblioteca de testes para criar e executar testes unitários em Python.
import pytest
# Importa a classe Juridica do módulo models.juridica para instanciar objetos de pessoa jurídica.
from models.juridica import Juridica
# Importa a classe Endereco do módulo models.endereco, que será usada para definir o endereço da pessoa jurídica.
from models.endereco import Endereco
# Importa o enum UnidadeFederativa, que contém os estados (UFs) do Brasil, para atribuir a unidade federativa correta no endereço.
from models.enums.uf import UnidadeFederativa
# Função de teste para validar uma pessoa jurídica com dados corretos.
def test_juridica_valida():
    # Cria um objeto Endereco com informações fictícias.
    endereco = Endereco("Rua C", "789", "", "54321-987", "Salvador", UnidadeFederativa.BAHIA)
    # Cria um objeto Juridica (pessoa jurídica) com dados válidos.
    pessoa_juridica = Juridica(
        1,  # ID da pessoa jurídica
        "Empresa ABC",  # Nome da empresa
        "7133334444",  # Telefone da empresa
        "contato@empresa.com",  # Email da empresa
        endereco,  # Endereço da empresa
        "12345678000199",  # CNPJ válido com 14 dígitos
        "123456789"  # Inscrição estadual
    )
    # Chama o método validar_dados para garantir que os dados estão corretos.
    # Se os dados forem válidos, nenhuma exceção será lançada.
    pessoa_juridica.validar_dados()
# Função de teste para verificar se um CNPJ inválido (com menos de 14 dígitos) levanta a exceção correta.
def test_juridica_cnpj_invalido():
    # Cria um objeto Endereco com dados fictícios, igual ao anterior.
    endereco = Endereco("Rua C", "789", "", "54321-987", "Salvador", UnidadeFederativa.BAHIA)
    # Cria um objeto Juridica com um CNPJ inválido (apenas 3 dígitos, em vez de 14).
    pessoa_juridica = Juridica(
        1,  # ID da pessoa jurídica
        "Empresa ABC",  # Nome da empresa
        "7133334444",  # Telefone da empresa
        "contato@empresa.com",  # Email da empresa
        endereco,  # Endereço da empresa
        "123",  # CNPJ inválido com menos de 14 dígitos
        "123456789"  # Inscrição estadual
    )
    # Usa pytest.raises para verificar se uma exceção do tipo ValueError é levantada com a mensagem correta.
    # Neste caso, a exceção deve conter a mensagem "CNPJ inválido: Deve conter 14 dígitos".
    with pytest.raises(ValueError, match="CNPJ inválido: Deve conter 14 dígitos"):
        # Chama o método validar_dados, que deve lançar a exceção por causa do CNPJ inválido.
        pessoa_juridica.validar_dados()
