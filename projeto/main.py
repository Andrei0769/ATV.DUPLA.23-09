# Andrei Luiz de Jesus Souza Almeida 
# Caio Vinicius Mascarenhas

import os 

os.system("cls || clear")

# main.py
from models.endereco import Endereco
from models.enums import UnidadeFederativa, Sexo, EstadoCivil
from models.fisica import Fisica
from models.juridica import Juridica

# Criar um endereço
endereco = Endereco("Rua A", "123", "Apto 101", "12345-678", "São Paulo", UnidadeFederativa.SAO_PAULO)

# Criar uma pessoa física
pessoa_fisica = Fisica(1, "João Silva", "11999999999", "joao@email.com", endereco, Sexo.MASCULINO, EstadoCivil.SOLTEIRO, "01/01/1990")
pessoa_fisica.validar_dados()

# Criar uma pessoa jurídica
pessoa_juridica = Juridica(2, "Empresa X", "1133333333", "contato@empresa.com", endereco, "12345678000195", "123456789")
pessoa_juridica.validar_dados()

print("Todas as validações foram bem-sucedidas.")
