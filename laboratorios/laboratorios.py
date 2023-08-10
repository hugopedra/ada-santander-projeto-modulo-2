


class Laboratorios:
    def __init__(self):
        self._cnpj = None
        self._nome = None
        self._endereco = None
        self._telefone = None
        self._cidade = None
        self._estado = None


def _get_cnpj(self) -> str:
    return self._cnpj


def _set_cnpj(self, cnpj: str) -> None:
    self._cnpj = cnpj


nome = property(_get_cnpj, _set_cnpj)


def _get_nome(self) -> str:
    return self._nome


def _set_nome(self, nome: str) -> None:
    self._nome = nome


nome = property(_get_nome, _set_nome)


def _get_endereco(self) -> str:
    return self._endereco


def _set_endereco(self, endereco: str) -> None:
    self._endereco = endereco


endereco = property(_get_endereco, _set_endereco)


def _get_telefone(self) -> str:
    return self._telefone


def _set_telefone(self, telefone: str) -> None:
    self._telefone = telefone


telefone = property(_get_telefone, _set_telefone)


def _get_cidade(self) -> str:
    return self._cidade


def _set_cidade(self, cidade: str) -> None:
    self._cidade = cidade


cidade = property(_get_cidade, _set_cidade)


def _get_estado(self) -> str:
    return self._estado


def _set_estado(self, estado: str) -> None:
    self._estado = estado


estado = property(_get_estado, _set_estado)
