from models.enums.setor import Setor
from models.enums.genero import Genero
from models.endereco import Endereco
from models.fisica import Fisica
from abc import ABC, abstractmethod

class Funcionario(Fisica,ABC):
    def __init__(self, nome: str,telefone: str, email: str,sexo: Genero, endereco: Endereco, matricula: str, setor: Setor, salario: float):
        super().__init__(nome, telefone, email, sexo, endereco)
        self.matricula = matricula
        self.setor = setor
        self.salario = salario

    @abstractmethod
    def salarioFinal(self) -> float:
        pass

    def __str__(self) -> str:
        return (
            f"{super().__str__()}\n"
            f"Matricula: {self.matricula}\n"
            f"Setor: {self.setor}\n"
            f"Salario: {self.salario}"
        )
