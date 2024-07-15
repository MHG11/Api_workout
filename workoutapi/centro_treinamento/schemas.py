from typing import Annotated
from contrib.schemas import BaseSchema, Field
from pydantic import UUID4


class CentroTreinamentoIn(BaseSchema):
    nome: Annotated[str, Field(description="Nome do centro", example='Ct porpo', max_length=20)]
    endereco: Annotated[str, Field(description="Endereço do centro", example='Rua das Laranjeiras', max_length=100)]
    proprietario: Annotated[str, Field(description="Nome do proprietário", example='Jorge', max_length=50)]
    
class CentroTreinamentoOut(CentroTreinamentoIn):
    id: Annotated[UUID4, Field(description="Identificador do centro de treinamento")]
    
class CentroTreinamentoAtletaOut(BaseSchema):
    nome: Annotated[str, Field(description="Nome do centro de treinamento", example='Ct porpo', max_length=50)]