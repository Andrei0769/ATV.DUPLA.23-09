import pytest
from models.engenheiro import Engenheiro
from models.endereco import Endereco
from models.enums.uf import UnidadeFederativa

def test_engenheiro_valido():
    # Cria um endereço válido (ajuste os parâmetros conforme necessário)
    endereco = Endereco("Rua G", "456", "Sala 202", "54321-000", "São Paulo", UnidadeFederativa.SAO_PAULO)
    
    # Cria um engenheiro com CREA válido
    engenheiro = Engenheiro("12345678900", "12345678", "ENG001", "Engenharia", 10000.00, "1234567890")
    
    # Valida os dados do engenheiro (não deve lançar exceção)
    engenheiro.validar_dados()  

def test_engenheiro_crea_vazio():
    # Cria um engenheiro com CREA vazio
    engenheiro = Engenheiro("12345678900", "12345678", "ENG001", "Engenharia", 10000.00, "")
    
    # Verifica se a validação lança a exceção esperada
    with pytest.raises(ValueError, match="CREA inválido: O CREA não pode ser vazio."):
        engenheiro.validar_dados()

def test_engenheiro_crea_invalido():
    # Cria um engenheiro com CREA de tamanho inválido
    engenheiro = Engenheiro("12345678900", "12345678", "ENG001", "Engenharia", 10000.00, "12345")
    
    # Verifica se a validação lança a exceção esperada
    with pytest.raises(ValueError, match="CREA inválido: Deve conter 10 caracteres."):
        engenheiro.validar_dados()
