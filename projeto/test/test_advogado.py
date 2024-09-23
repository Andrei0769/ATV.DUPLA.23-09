import pytest
from models.advogado import Advogado
from models.endereco import Endereco
from models.enums.uf import UnidadeFederativa

def test_advogado_valido():
    # Cria um endereço válido (ajuste os parâmetros conforme necessário)
    endereco = Endereco("Rua F", "333", "", "65432-000", "Rio de Janeiro", UnidadeFederativa.RIO_DE_JANEIRO)
    
    # Cria um advogado com OAB válido
    advogado = Advogado("12345678900", "12345678", "ADV001", "Jurídico", 12000.00, "123456789")
    
    # Valida os dados do advogado (não deve lançar exceção)
    advogado.validar_dados()  

def test_advogado_oab_vazia():
    # Cria um advogado com OAB vazia
    advogado = Advogado("12345678900", "12345678", "ADV001", "Jurídico", 12000.00, "")
    
    # Verifica se a validação lança a exceção esperada
    with pytest.raises(ValueError, match="OAB inválida: A OAB não pode ser vazia."):
        advogado.validar_dados()

def test_advogado_oab_invalido():
    # Cria um advogado com OAB de tamanho inválido
    advogado = Advogado("12345678900", "12345678", "ADV001", "Jurídico", 12000.00, "12345678")  # 8 caracteres
    
    # Verifica se a validação lança a exceção esperada
    with pytest.raises(ValueError, match="OAB inválida: Deve conter 9 caracteres."):
        advogado.validar_dados()
