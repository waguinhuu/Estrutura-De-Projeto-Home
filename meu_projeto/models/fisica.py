from meu_projeto.models.pessoa import Pessoa
from meu_projeto.models.endereco import Endereco
from meu_projeto.models.enums.genero import Genero
from abc import ABC

class Fisica(Pessoa, ABC):
    def __init__(self, nome: str,telefone: str, email: str,sexo: Genero, endereco: Endereco) -> None:
        super().__init__(nome, telefone, email, endereco)
        self.sexo = sexo

    def __str__(self) -> str:
        return (
            f"{super().__str__()}\n"
            f"Sexo: {self.sexo}\n"
        )