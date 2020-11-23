class DelimitadorInvalidoException(Exception):

    def __init__(self, delimiter):
        self.delimiter = delimiter

    def __str__(self):
        exception = (f'Delimitador de nome "{self.delimiter}" não é válido'
                     'são aceitos apenas delimitadores de um caractere')

        return exception
