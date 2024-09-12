from models.fisica import Fisica
from models.endereco import Endereco
from models.enums.genero import Genero

class Cliente(Fisica):
    def __init__(self, nome: str,telefone: str, email: str,sexo: Genero,protoculo_de_atendimento: int, endereco: Endereco) -> None:
        super().__init__(nome, telefone, email, sexo, endereco)
        self.protoculo_de_atendimento = protoculo_de_atendimento

    def __str__(self) -> str:
        return (
            "\nCliente:\n"
            f"{super().__str__()}\n"
            f"Protocolo de atendimento: {self.protoculo_de_atendimento}\n"
        )