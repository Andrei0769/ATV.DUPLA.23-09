# tests/fisica/test_fisica.py

# Importa o pytest, que é uma biblioteca utilizada para criar e executar testes em Python.
import pytest

# Importa a classe Fisica do módulo models.fisica, que será usada para criar instâncias de pessoa física.
from models.fisica import Fisica

# Importa a classe Endereco do módulo models.endereco, usada para definir o endereço de uma pessoa.
from models.endereco import Endereco

# Importa os enums (tipos enumerados) Sexo, EstadoCivil e UnidadeFederativa (UF) para atribuir valores padronizados.
from models.enums.sexo import Sexo
from models.enums.estado_civil import EstadoCivil
from models.enums.uf import UnidadeFederativa

# Função de teste para validar uma pessoa física com dados corretos.
def test_fisica_valida():
    # Cria um objeto Endereco com informações fictícias.
    endereco = Endereco("Rua B", "456", "", "12345-789", "Rio de Janeiro", UnidadeFederativa.RIO_DE_JANEIRO)
    
    # Cria um objeto Fisica (pessoa física) com todos os dados válidos.
    pessoa_fisica = Fisica(
        1,  # ID da pessoa física
        "Maria Oliveira",  # Nome da pessoa física
        "21988887777",  # Telefone
        "maria@email.com",  # Email
        endereco,  # Endereço da pessoa física
        Sexo.FEMININO,  # Sexo da pessoa (Enum)
        EstadoCivil.SOLTEIRO,  # Estado civil da pessoa (Enum)
        "01/01/1995"  # Data de nascimento
    )

    # Chama o método validar_dados para verificar se os dados estão corretos.
    # Se os dados forem válidos, nenhuma exceção será levantada.
    pessoa_fisica.validar_dados()

# Função de teste para verificar uma pessoa física com data de nascimento inválida.
def test_fisica_data_nascimento_invalida():
    # Cria um objeto Endereco com dados fictícios, idêntico ao anterior.
    endereco = Endereco("Rua B", "456", "", "12345-789", "Rio de Janeiro", UnidadeFederativa.RIO_DE_JANEIRO)
    
    # Cria um objeto Fisica, mas com a data de nascimento inválida (vazia).
    pessoa_fisica = Fisica(
        1,  # ID da pessoa física
        "Maria Oliveira",  # Nome da pessoa física
        "21988887777",  # Telefone
        "maria@email.com",  # Email
        endereco,  # Endereço
        Sexo.FEMININO,  # Sexo (Enum)
        EstadoCivil.SOLTEIRO,  # Estado civil (Enum)
        ""  # Data de nascimento vazia, o que é inválido
    )

    # Usa pytest.raises para verificar se a exceção ValueError é lançada com a mensagem correta.
    # Neste caso, a mensagem "Data de nascimento inválida" deve ser levantada.
    with pytest.raises(ValueError, match="Data de nascimento inválida"):
        # Chama o método validar_dados que deverá lançar a exceção por causa da data inválida.
        pessoa_fisica.validar_dados()
