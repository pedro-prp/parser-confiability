from exceptions.ArquivoNaoEncontradoException import ArquivoNaoEncontradoException
from exceptions.EscritaNaoPermitidaException import EscritaNaoPermitidaException
from pathlib import Path


def read_file(path):
    try:
        input_data = open(path)
    except:
        raise ArquivoNaoEncontradoException(path)

    return input_data.read()


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
