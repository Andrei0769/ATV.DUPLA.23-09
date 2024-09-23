
import pytest
from models.medico import Medico
from models.endereco import Endereco
from models.enums.uf import UnidadeFederativa

def test_medico_valido():
    endereco = Endereco("Rua E", "222", "", "54321-000", "São Paulo", UnidadeFederativa.SAO_PAULO)
    medico = Medico(2, "Mariana Silva", "1133334444", "mariana@email.com", endereco, "654321")
    medico.validar_dados()  # Não deve lançar exceção

def test_medico_crm_invalido():
    endereco = Endereco("Rua E", "222", "", "54321-000", "São Paulo", UnidadeFederativa.SAO_PAULO)
    medico = Medico(2, "Mariana Silva", "1133334444", "mariana@email.com", endereco, "")
    with pytest.raises(ValueError, match="CRM inválido: O CRM não pode ser vazio."):
        medico.validar_dados()
