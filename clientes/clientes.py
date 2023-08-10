from datetime import datetime, date
import re

# bd_clientes = {
#     "77542415603": {"nome": "Cliente Um", "data_nascimento": date(2000, 1, 1)},
#     "64559533806": {"nome": "Cliente Dois", "data_nascimento": date(1998, 5, 3)},
#     "04371114407": {"nome": "Cliente Três", "data_nascimento": date(2004, 2, 8)},
# }

from banco_dados.db import banco_dados

bd_clientes = banco_dados["bd_clientes"]


class ClienteJaCadastrado(Exception):
    def __init__(self, mensagem: str = "Cliente já cadastrado"):
        self._erro = mensagem
        super().__init__(self._erro)


class Clientes:
    def __init__(self, cpf: str = None):
        self._nome = None
        self._cpf = None
        self._data_nascimento = None

    def valida_cpf(self, cpf):
        cpf = re.sub(r"[!@#$%^&*-. ]", "", str(cpf)).zfill(11)
        if not cpf.isdigit():
            raise ValueError("CPF inválido")
        return cpf

    def _get_nome(self) -> str:
        return self._nome

    def _set_nome(self, nome: str) -> None:
        self._nome = nome

    nome = property(_get_nome, _set_nome)

    def _get_cpf(self):
        return self._cpf

    def _set_cpf(self, cpf: str) -> None:
        self._cpf = self.valida_cpf(cpf)

    cpf = property(_get_cpf, _set_cpf)

    def _get_data_nascimento(self):
        return datetime.strftime(self._data_nascimento, "%d/%m/%Y")

    def _set_data_nascimento(self, data_nascimento: date) -> None:
        self._data_nascimento = data_nascimento

    data_nascimento = property(_get_data_nascimento, _set_data_nascimento)

    def buscar_cliente(self, cpf: str) -> dict:
        if cpf in bd_clientes and bd_clientes[cpf]:
            client = bd_clientes[cpf]
            self.nome = client["nome"]
            self.cpf = cpf
            self.data_nascimento = client["data_nascimento"]
            return {"cpf": cpf, **client}
        else:
            return "Cliente não localizado"

    def cadastrar_cliente(self, nome: str, cpf: str, data_nascimento: str) -> None:
        cpf = self.valida_cpf(cpf)

        if cpf in bd_clientes:
            raise ClienteJaCadastrado()
        else:
            bd_clientes[cpf] = {
                "nome": nome,
                "data_nascimento": datetime.strptime(
                    data_nascimento, "%d/%m/%Y"
                ).date(),
            }
            self.buscar_cliente(cpf)
            return "Cliente cadastrado com sucesso"
