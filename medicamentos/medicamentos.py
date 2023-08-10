class Medicamentos:
    def __init__(
        self,
        nome: str,
        principio_ativo: str,
        laboratorio: Laboratorios,
        descricao: str,
        preco: float,
    ):
        self._nome = nome
        self._principio_ativo = principio_ativo
        self._laboratorio = laboratorio
        self._descricao = descricao
        self._preco = preco

    @property
    def nome(self):
        return self._nome

    @property
    def principio_ativo(self):
        return self.__principio_ativo

    @property
    def laboratorio(self):
        return self._laboratorio

    @property
    def descricao(self):
        return self._descricao

    @property
    def preco(self):
        return self._preco


class MedicamentosQuimioterapicos(Medicamentos):
    def __init__(
        self,
        nome: str,
        principio_ativo: str,
        laboratorio: Laboratorios,
        descricao: str,
        preco: float,
        necessita_receita: bool,
    ):
        self._necessita_receita = necessita_receita
        super().__init__(nome, principio_ativo, laboratorio, descricao, preco)

    @property
    def necessita_receita(self):
        return self._necessita_receita


class MedicamentosFitoterapicos(Medicamentos):
    def __init__(
        self,
        nome: str,
        principio_ativo: str,
        laboratorio: Laboratorios,
        descricao: str,
        preco: float,
    ):
        super().__init__(nome, principio_ativo, laboratorio, descricao, preco)
