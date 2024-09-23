# Andrei Luiz de Jesus Souza Almeida 
# Caio Vinicius Mascarenhas costa 
#================ALUNOS=======================

import os

os.system("cls || clear")

# main.py
from models.endereco import Endereco
from models.enums import UnidadeFederativa, Sexo, EstadoCivil
from models.fisica import Fisica
from models.juridica import Juridica
from models.prestacao_servico import PrestacaoServico
from models.fornecedor import Fornecedor

# Criar um endereço
endereco = Endereco("Rua A", "123", "Apto 101", "12345-678", "São Paulo", UnidadeFederativa.SAO_PAULO)

# Criar uma pessoa física
pessoa_fisica = Fisica(1, "Andrei Luiz", "11999999999", "joao@email.com", endereco, Sexo.MASCULINO, EstadoCivil.SOLTEIRO, "01/01/1990")
pessoa_fisica.validar_dados()

# Criar uma pessoa jurídica
pessoa_juridica = Juridica(2, "Space X", "1133333333", "Space@empresa.com", endereco, "12345678000195", "123456789")
pessoa_juridica.validar_dados()

# Criar um prestador de serviço
prestador_servico = PrestacaoServico(
    3, "Serviço Y", "1144444444", "contato@servico.com", endereco, "98765432000198", "987654321", 
    contrato_inicio="01/01/2023", contrato_fim="31/12/2023"
)
prestador_servico.validar_dados()

# Criar um fornecedor
fornecedor = Fornecedor(
    4, "Fornecedor Z", "1155555555", "contato@fornecedor.com", endereco, "87654321000197", "876543210", 
    produto="Matéria-prima"
)
fornecedor.validar_dados()

print("Todas as validações foram bem-sucedidas.")
