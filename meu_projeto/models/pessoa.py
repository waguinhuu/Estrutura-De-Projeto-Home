from models.endereco import Endereco
from abc import ABC

class Pessoa(ABC):
    def __init__(self, nome: str,telefone: str, email: str, endereco: Endereco) -> None:
        self.nome = nome
        self.telefone = telefone
        self.email = email
        self.endereco = endereco

    def __str__(self):
        return (
            f"Nome: {self.nome}\n"
            f"Telefone: {self.telefone}\n"
            f"Email: {self.email}\n"
            f"Endereco: {self.endereco}"
        )
