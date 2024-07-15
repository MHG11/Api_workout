from typing import Annotated
from contrib.schemas import BaseSchema, Field
from pydantic import UUID4


class CategoriaIn(BaseSchema):
    nome: Annotated[str, Field(description="Nome da categoria", example='Musculação', max_length=40)]
    
class CategoriaOut(CategoriaIn):
    id: Annotated[UUID4, Field(description="Identificador da categoria")]