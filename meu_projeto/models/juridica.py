from meu_projeto.models.pessoa import Pessoa
from meu_projeto.models.endereco import Endereco

class Juridica(Pessoa):
    def __init__(self,  nome: str, telefone: str, email: str, endereco: Endereco, cnpj: str, inscricaoEstadual: str) -> None:
        super().__init__(nome, telefone, email, endereco)
        self.cnpj = cnpj
        self.inscricaoEstadual = inscricaoEstadual

    def __str__(self) -> str:
        return (
            "\nJuridica:\n"
            f"{super().__str__()}"
            f"Cnpj: {self.cnpj}\n"
            f"Inscrição Estadual: {self.inscricaoEstadual}"
        )
