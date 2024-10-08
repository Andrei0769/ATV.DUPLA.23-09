# Andrei Luiz de Jesus Souza Almeida 
# Caio Vinicius Mascarenhas costa 
#================ALUNOS=======================

# main.py

import os
from models.endereco import Endereco
from models.enums import UnidadeFederativa, Sexo, EstadoCivil
from models.fisica import Fisica
from models.juridica import Juridica
from models.prestacao_servico import PrestacaoServico
from models.fornecedor import Fornecedor

# Limpar a tela
os.system("cls || clear")

def criar_endereco():
    return Endereco("Rua A", "123", "Apto 101", "12345-678", "São Paulo", UnidadeFederativa.SAO_PAULO)

def criar_pessoa_fisica(endereco):
    return Fisica(1, "Andrei Luiz", "11999999999", "joao@email.com", endereco, 
                  Sexo.MASCULINO, EstadoCivil.SOLTEIRO, "01/01/1990")

def criar_pessoa_juridica(endereco):
    return Juridica(2, "Space X", "1133333333", "Space@empresa.com", endereco, 
                    "12345678000195", "123456789")

def criar_prestador_servico(endereco):
    return PrestacaoServico(
        3, "Serviço Y", "1144444444", "contato@servico.com", endereco, 
        "98765432000198", "987654321", contrato_inicio="01/01/2023", contrato_fim="31/12/2023"
    )

def criar_fornecedor(endereco):
    return Fornecedor(
        4, "Fornecedor Z", "1155555555", "contato@fornecedor.com", endereco, 
        "87654321000197", "876543210", produto="Matéria-prima"
    )

def validar_instancias(instancias):
    for instancia in instancias:
        instancia.validar_dados()


endereco = criar_endereco()

instancias = [
    criar_pessoa_fisica(endereco),
    criar_pessoa_juridica(endereco),
    criar_prestador_servico(endereco),
    criar_fornecedor(endereco)
]

validar_instancias(instancias)

# Imprimir as informações das instâncias
for instancia in instancias:
    print(instancia) 
