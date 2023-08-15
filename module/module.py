# banco_dados = {
#     "bd_clientes": {
#         "77542415603": {"nome": "Raquel", "data_nascimento": date(2000, 1, 1)},
#         "64559533806": {"nome": "Bruno", "data_nascimento": date(1998, 5, 3)},
#         "04371114407": {"nome": "Mauricio", "data_nascimento": date(2004, 2, 8)},
#     },
#     "bd_laboratorios": {
#         "58066331000104": {
#             "nome": "EMS",
#             "endereco": "Rua Um",
#             "telefone": "1144445555",
#             "cidade": "São Paulo",
#             "estado": "SP",
#         },
#         "75380556000150": {
#             "nome": "Aché",
#             "endereco": "Rua Dois",
#             "telefone": "1122223333",
#             "cidade": "Belo Horizonte",
#             "estado": "MG",
#         },
#         "42224316000107": {
#             "nome": "Medley",
#             "endereco": "Rua Três",
#             "telefone": "1166667777",
#             "cidade": "Cascavel",
#             "estado": "PR",
#         },
#     },
# }

import json


def ler_arquivo(nome_arquivo="./banco_dados/db.json"):
    try:
        with open(nome_arquivo, "r") as arquivo:
            return json.loads(arquivo.read())
    except Exception as error:
        print(error)
        return None


def salvar_arquivo(novo_arquivo: dict, nome_arquivo="./banco_dados/db.json"):
    with open(nome_arquivo, "w") as arquivo:
        arquivo.write(json.dumps(novo_arquivo, ensure_ascii=False))
