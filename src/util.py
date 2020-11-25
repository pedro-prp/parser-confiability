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

def output_file(out_path, filename, content=''):
    try:
        p = Path(out_path)
        p = p / filename
        if not p.exists():
            p.touch()
        with p.open('w') as output:
            output.write(content)
    except Exception as ex:
        print(ex)
        raise EscritaNaoPermitidaException(out_path)
