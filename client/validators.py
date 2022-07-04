def cpf_valido(cpf):
    return len(cpf) == 11


def name_valido(name):
    return name.isalpha()


def rg_valido(rg):
    return len(rg) == 9


def phone_valido(phone):
    return len(phone) >= 11
