from datetime import date

banco_dados = {
    "bd_clientes": {
        "77542415603": {"nome": "Cliente Um", "data_nascimento": date(2000, 1, 1)},
        "64559533806": {"nome": "Cliente Dois", "data_nascimento": date(1998, 5, 3)},
        "04371114407": {"nome": "Cliente Três", "data_nascimento": date(2004, 2, 8)},
    },
    "bd_laboratorios": {
        "58066331000104	": {
            "nome": "EMS",
            "endereco": "Rua Um",
            "telefone": "1144445555",
            "cidade": "São Paulo",
            "estado": "SP",
        },
        "75380556000150	": {
            "nome": "Aché",
            "endereco": "Rua Dois",
            "telefone": "1122223333",
            "cidade": "Belo Horizonte",
            "estado": "MG",
        },
        "42224316000107	": {
            "nome": "Medley",
            "endereco": "Rua Três",
            "telefone": "1166667777",
            "cidade": "Cascavel",
            "estado": "PR",
        },
    },
}
