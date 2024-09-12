from models.juridica import Juridica
from models.cliente import Cliente
from models.motoboy import Motoboy
from models.medico import Medico
from models.advogado import Advogado
from models.enums.genero import Genero
from models.enums.setor import Setor
from models.enums.unidade_federativa import UnidadeFederativa
from models.endereco import Endereco

juridica = Juridica("Wagner","719292308","wag@gmai.com",
                    Endereco("Rua A","92","sla","123323-2222","SFC",UnidadeFederativa.BAHIA.nome),"2331313-22","nn sei")

cliente = Cliente("Marta","719927363","marta@gmai.com",Genero.FEMININO.value,777,
                  Endereco("Rua B","99","sla","43900-000","STA",UnidadeFederativa.BAHIA.sigla))

motoboy = Motoboy("Thiago","71986335353","th@gmai.com","12e",Genero.MASCULINO.value,
                  Endereco("Rua C","22","noop","43800-000","Sao Francisco",UnidadeFederativa.RIO_DE_JANEIRO.sigla),
                  "333",Setor.ENGENHARIA.value,100)

medico = Medico("Luisa","7298392939","luisa@gmai.com","122",Genero.FEMININO.value,
                Endereco("Rua D", "34","apartamento","43900-22","Rocinha",UnidadeFederativa.RIO_DE_JANEIRO.nome),
                "333",Setor.SAUDE.value, 100)

advogado = Advogado("Paulo","8181818","paulo@gmai.com","33",Genero.MASCULINO.value,
                    Endereco("Rua E","11","nulo","45900-999","Baixada",UnidadeFederativa.SAO_PAULO.nome),
                    "9090",Setor.JURIDICO.value,100)



print(juridica)
print(cliente)
print(motoboy)
print(medico)
print(advogado)