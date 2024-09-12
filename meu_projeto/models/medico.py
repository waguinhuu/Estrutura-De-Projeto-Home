from models.endereco import Endereco
from models.enums.genero import Genero
from models.enums.setor import Setor
from models.funcionario import Funcionario

class Medico(Funcionario):
    def __init__(self,nome: str,telefone: str, email: str, crm: str, sexo: Genero, endereco: Endereco, matricula: str, setor: Setor, salario: float) -> None:
        super().__init__(nome, telefone, email, sexo, endereco, matricula, setor, salario)
        self.crm = crm

    def salarioFinal(self) -> float:
        BONIFICACAO = 1.3
        return self.salario * BONIFICACAO

    def __str__(self) -> str:
        return (
            "\nMédico:\n"
            f"{super().__str__()}\n"
            f"Crm: {self.crm}\n"
            f"Salario Final: {self.salarioFinal()}"
        )
