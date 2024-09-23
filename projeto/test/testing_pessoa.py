# tests/pessoa/test_pessoa.py
import pytest
from models.pessoa import Pessoa
from models.endereco import Endereco
from models.enums.uf import UnidadeFederativa

def test_pessoa_valida():
    endereco = Endereco("Rua A", "123", "Apto 101", "12345-678", "São Paulo", UnidadeFederativa.SAO_PAULO)
    pessoa = Pessoa(1, "João Silva", "11999999999", "joao@email.com", endereco)
    pessoa.validar_dados()  # Não deve lançar exceção

def test_pessoa_nome_invalido():
    endereco = Endereco("Rua A", "123", "Apto 101", "12345-678", "São Paulo", UnidadeFederativa.SAO_PAULO)
    pessoa = Pessoa(1, "", "11999999999", "joao@email.com", endereco)
    with pytest.raises(ValueError, match="Nome inválido"):
        pessoa.validar_dados()
