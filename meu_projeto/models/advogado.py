from models.endereco import Endereco
from models.enums.genero import Genero
from models.enums.setor import Setor
from models.funcionario import Funcionario

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
