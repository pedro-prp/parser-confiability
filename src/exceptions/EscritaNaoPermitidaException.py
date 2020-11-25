class EscritaNaoPermitidaException(Exception):
    def __init__(self, path):
        self.path = path

    def __str__(self):
        return f'Impossível escrever arquivos no caminho: "{self.path}"'
