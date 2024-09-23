# models/enums/estado_civil.py
from enum import Enum

class EstadoCivil(Enum):
    SOLTEIRO = "Solteiro"
    CASADO = "Casado"
    SEPARADO = "Separado"
    DIVORCIADO = "Divorciado"
    VIUVO = "Viúvo"
