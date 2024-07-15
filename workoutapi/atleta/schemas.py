from typing import Annotated, Optional
from contrib.schemas import BaseSchema, OutMixin
from pydantic import Field
from workoutapi.categorias.schema import CategoriaIn
from workoutapi.centro_treinamento.schemas import CentroTreinamentoAtletaOut

class Atleta(BaseSchema):
    nome: Annotated[str, Field(description="Nome do atleta", example='Joaquim', max_length=50)]
    idade: Annotated[int, Field(description="Idade do atleta", example=25, ge=0, le=100)]
    cpf: Annotated[str, Field(description="CPF do atleta", example='12345678900', min_length=11, max_length=11)]
    peso: Annotated[float, Field(description="Peso do atleta", example=80.5, ge=0, le=500)]
    altura: Annotated[float, Field(description="Altura do atleta", example=1.75, ge=0, le=3)]
    sexo: Annotated[str, Field(description="Sexo do atleta", example='M', min_length=1, max_length=1)]
    categorias: Annotated[CategoriaIn, Field(description="Nome da categoria")]
    centro_treinamento: Annotated[CentroTreinamentoAtletaOut, Field(description="Nome do centro de treinamento")]
    

class AtletaIn(Atleta):
    pass
    
class AtletaOut(Atleta, OutMixin):
    pass

class AtletaUpdate(BaseSchema):
    nome: Annotated[Optional[str], Field(None,description="Nome do atleta", example='Joaquim', max_length=50)]
    idade: Annotated[Optional [int], Field(None,description="Idade do atleta", example=25, ge=0, le=100)]
    peso: Annotated[Optional [float], Field(None,description="Peso do atleta", example=80.5, ge=0, le=500)]