from exceptions.ArquivoNaoEncontradoException import ArquivoNaoEncontradoException


def read_file(path):
    try:
        input_data = open(path)

    except:
        raise ArquivoNaoEncontradoException(path)

    return input_data.read()

# def read_file(path):
#     f = open(path)

#     return f.read()
