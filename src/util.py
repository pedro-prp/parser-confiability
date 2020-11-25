from exceptions.ArquivoNaoEncontradoException import ArquivoNaoEncontradoException
from exceptions.DelimitadorInvalidoException import DelimitadorInvalidoException
from exceptions.EscritaNaoPermitidaException import EscritaNaoPermitidaException


def read_file(path):
    try:
        input_data = open(path)
    except:
        raise ArquivoNaoEncontradoException(path)

    return input_data.read()


def check_delimiter_valid(input):
    if len(input) == 1:
        return True
    else:
        raise DelimitadorInvalidoException(input)

def output_file(out_path, filename):
    try:
        a = 10 / 0
    except:
        raise EscritaNaoPermitidaException(out_path)
