from models.endereco import Endereco
from models.enums.genero import Genero
from models.enums.setor import Setor
from models.funcionario import Funcionario

class Motoboy(Funcionario):
    def __init__(self, nome: str,telefone: str, email: str, cnh: str, sexo: Genero, endereco: Endereco, matricula: str, setor: Setor, salario: float) -> None:
        super().__init__(nome, telefone, email, sexo, endereco, matricula, setor, salario)
        self.cnh = cnh

    def salarioFinal(self) -> float:
        BONIFICAO = 1.2
        return self.salario * BONIFICAO

    def __str__(self) -> str:
        return (
            "\nMotoboy:\n"
            f"{super().__str__()}\n"
            f"CNH: {self.cnh}\n"
            f"Salario final: {self.salarioFinal()}\n"
        )