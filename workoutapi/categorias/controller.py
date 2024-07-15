from workoutapi.categorias.schema import CategoriaIn, CategoriaOut
from workoutapi.categorias.models import CategoriaModel
from contrib.dependencies import DatabaseDependencies
from fastapi import APIRouter, Body, status, HTTPException
from uuid import uuid4
from pydantic import UUID4
from sqlalchemy.future import select

router = APIRouter()

@router.post('/', summary="Criar nova categoria", status_code=status.HTTP_201_CREATED, response_model=CategoriaOut)
async def post(db_session: DatabaseDependencies, categoria_in: CategoriaIn = Body(...)) -> CategoriaOut:
    
    categoria_out = CategoriaOut(id=uuid4(), **categoria_in.model_dump())
    categoria_model = CategoriaModel(**categoria_out.model_dump())
    
    db_session.add(categoria_model)
    await db_session.commit()
    return categoria_out

@router.get('/', summary="Consultar todas as categorias", status_code=status.HTTP_200_OK, response_model=list[CategoriaOut])
async def query(db_session: DatabaseDependencies) -> list[CategoriaOut]:
    categorias: list[CategoriaModel] = (await db_session.execute(select(CategoriaModel))).scalars().all()
    
    return categorias

@router.get('/{id}', summary="Consultar categoria por id", status_code=status.HTTP_200_OK, response_model=CategoriaOut)
async def query(id: UUID4, db_session: DatabaseDependencies) -> list[CategoriaOut]:
    categoria: CategoriaModel = (await db_session.execute(select(CategoriaModel).filter_by(id=id))).scalars().first()
    
    if not categoria:
        raise HTTPException(status_code=404, detail=f"Categoria nao encontrada no id {id}")
    
    
    return categoria