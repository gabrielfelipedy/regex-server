import re

def validate_phone_number(phone):
    # Regex pattern to match both phone number formats
    phone_regex = r'^\(\d{2}\)\s\d{4,5}-\d{4}$'
    
    # Check if the phone number matches the pattern
    if not re.match(phone_regex, phone):
        return False
    
    return True


def validate_cpf(cpf):
    # Regex pattern to match both phone number formats
    cpf_regex = r'^\d{3}\.\d{3}\.\d{3}-\d{2}$'
    
    # Check if CPF matches the exact format
    if not re.match(cpf_regex, cpf):
        return False
    

    # OBS. EM UM CENÁRIO REAL, É FEITO UM CÁLCULO PARA VALIDAR OS DÍGITOS DO CPF, PORÉM NÃO SERÁ MOSTRADO AQUI POR NÃO ESTAR NO ESCOPO DO TRABALHO

    return True