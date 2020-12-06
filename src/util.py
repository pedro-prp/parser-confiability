from itertools import zip_longest

from exceptions.DelimitadorInvalidoException import (
    DelimitadorInvalidoException)


def check_delimiter_valid(input):
    if len(input) == 1:
        return True
    else:
        raise DelimitadorInvalidoException(input)


def parse_file(content):
    lines = content.split('\n')
    parsed = {}
    evolution = 0

    for line in lines:
        if not line.isnumeric():
            if not line:
                break

            evolution += 1
            parsed[evolution] = []
        else:
            parsed[evolution].append(int(line))

    return parsed


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


def build_response(parsed_data, delimiter, direction):
    check_direction(direction)
    check_delimiter_valid(delimiter)

    if direction in ['linhas', 'l']:
        response = []
        for key in parsed_data:
            values = parsed_data[key]
            values.insert(0, key)
            line = delimiter.join(str(x) for x in values)
            response.append(line)

        result = '\n'.join(response)
        return result
    else:
        response = []
        for key in parsed_data:
            values = parsed_data[key]
            values.insert(0, key)
            response.append([str(x) for x in values])

        result = list(zip_longest(*response, fillvalue=' '))
        res = []
        for line in result:
            res.append(delimiter.join(line))

        res = '\n'.join(res)
        return res
