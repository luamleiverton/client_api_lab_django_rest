import re
from validate_docbr import CPF

def cpf_valido(cpf):
    cpf = CPF()
    return cpf.validate(cpf)


def name_valido(name):
    return name.isalpha()


def rg_valido(rg):
    return len(rg) == 9


def phone_valido(phone):
    '''Verifica formato do celular (11 91234-9876)'''
    modelo = '[0-9]{2} [0-9]{5}-[0-9]{4}'
    resposta = re.findall(modelo, phone)
    return resposta

