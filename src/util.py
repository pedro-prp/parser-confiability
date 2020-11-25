from exceptions.ArquivoNaoEncontradoException import ArquivoNaoEncontradoException
from exceptions.DelimitadorInvalidoException import DelimitadorInvalidoException


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
    pass