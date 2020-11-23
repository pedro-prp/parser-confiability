class ArquivoNaoEncontradoException(Exception):

    def __init__(self, name):
        self.name = name

    def __str__(self):
        exception = f'Arquivo de nome "{self.name}" não existente.'

        return exception
