from exceptions.DelimitadorInvalidoException import (
    DelimitadorInvalidoException)

from parser import Parser


def check_delimiter_valid(input):
    if len(input) == 1:
        return True
    else:
        raise DelimitadorInvalidoException(input)


def parse_file(content):
    return Parser.parse_file(content)


def build_response(parsed_data, delimiter, direction):
    return Parser.build_response(parsed_data, delimiter, direction)


def check_direction(direction):
    if direction not in ['colunas', 'linhas', 'c', 'l']:
        raise Exception('Opção inválida')
    else:
        return True


def check_file_type(ftype):
    if ftype not in ['analysis', 'total']:
        raise Exception('Opção inválida')
    else:
        return True
