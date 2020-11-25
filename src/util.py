from exceptions.ArquivoNaoEncontradoException import ArquivoNaoEncontradoException
from exceptions.DelimitadorInvalidoException import DelimitadorInvalidoException
from exceptions.EscritaNaoPermitidaException import EscritaNaoPermitidaException
from pathlib import Path

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
        p = Path(out_path)
        p = p / filename
        with p.open() as output:
            output.write("foo_bar")
    except:
        raise EscritaNaoPermitidaException(out_path)
