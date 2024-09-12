from meu_projeto.models.endereco import Endereco
from meu_projeto.models.enums.genero import Genero
from meu_projeto.models.enums.setor import Setor
from meu_projeto.models.funcionario import Funcionario

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