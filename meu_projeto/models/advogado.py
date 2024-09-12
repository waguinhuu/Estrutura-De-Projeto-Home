from meu_projeto.models.endereco import Endereco
from meu_projeto.models.enums.genero import Genero
from meu_projeto.models.enums.setor import Setor
from meu_projeto.models.funcionario import Funcionario

class Advogado(Funcionario):
    def __init__(self,nome: str,telefone: str, email: str,oab: str,sexo: Genero, endereco: Endereco, matricula: str, setor: Setor, salario: float) -> None:
        super().__init__(nome, telefone, email, sexo, endereco, matricula, setor, salario)
        self.oab = oab

    def salarioFinal(self) -> float:
        BONIFICACA0 = 1.4
        return self.salario * BONIFICACA0
    def __str__(self) -> str:
        return (
            "\nAdvogado:\n"
            f"{super().__str__()}\n"
            f"OAB: {self.oab}\n"
            f"Salario Final: {self.salarioFinal()}"
        )
