from datetime import datetime

from workoutapi.centro_treinamento.models import CentroTreinamentoModel
from workoutapi.atleta.schemas import AtletaIn, AtletaOut, AtletaUpdate
from workoutapi.atleta.models import AtletaModel
from contrib.dependencies import DatabaseDependencies
from fastapi import APIRouter, Body, status, HTTPException
from uuid import uuid4
from pydantic import UUID4
from sqlalchemy.future import select
from workoutapi.categorias.models import CategoriaModel

router = APIRouter()

@router.post('/', summary="Criar novo atleta", status_code=status.HTTP_201_CREATED, response_model=AtletaOut)
async def post(db_session: DatabaseDependencies, atleta_in: AtletaIn = Body(...)) -> AtletaOut:
    
    categoria_nome = atleta_in.categoria.nome
    centro_treinamento_nome = atleta_in.centro_treinamento.nome
   
    categorias= (await db_session.execute(select(CategoriaModel).filter_by(nome=categoria_nome))).scalars().first()
    centro_treinamento = (await db_session.execute(select(CentroTreinamentoModel).filter_by(nome=centro_treinamento_nome))).scalars().first()
    
    if not categorias:
        raise HTTPException(status_code=400, detail=f"Categoria {categoria_nome} não foi encontrada")
    
    
    
    if not centro_treinamento:
        raise HTTPException(status_code=400, detail=f"Centro {centro_treinamento_nome} nao encontrado")
    
    try:
        atleta_out = AtletaOut(id=uuid4(),created_at=datetime.now(), **atleta_in.model_dump())
        atleta_model = AtletaModel(**atleta_out.model_dump(exclude={'categoria', 'centro_treinamento'}))
        atleta_model.categoria_id = categorias.pk_id
        atleta_model.centro_treinamento_id = centro_treinamento.pk_id
        
        
        db_session.add(atleta_model)
        await db_session.commit()
    except Exception:
        raise HTTPException(status_code=404, detail=f"Erro ao pesistir dados no banco") 
    
    return atleta_out

@router.get('/', summary="Consultar todos os atletas", status_code=status.HTTP_200_OK, response_model=list[AtletaOut])
async def query(db_session: DatabaseDependencies) -> list[AtletaOut]:
    atletas: list[AtletaModel] = (await db_session.execute(select(AtletaModel))).scalars().all()
    
    return [AtletaOut.model_validate(atleta) for atleta in atletas]

@router.get('/{id}', summary="Consultar atleta por id", status_code=status.HTTP_200_OK, response_model=AtletaOut)
async def query(id: UUID4, db_session: DatabaseDependencies) -> list[AtletaOut]:
    atleta: AtletaModel = (await db_session.execute(select(AtletaModel).filter_by(id=id))).scalars().first()
    
    if not atleta:
        raise HTTPException(status_code=500, detail=f'atleta {nome} não encontrado')
    
    
    return atleta

@router.patch('/{id}', summary="Editar atleta por id", status_code=status.HTTP_200_OK, response_model=AtletaUpdate)
async def query(id: UUID4, db_session: DatabaseDependencies, atleta_up: AtletaUpdate = Body(...)) -> list[AtletaUpdate]:
    atleta: AtletaModel = (await db_session.execute(select(AtletaModel).filter_by(id=id))).scalars().first()
    
    if not atleta:
        raise HTTPException(status_code=500, detail=f'atleta {nome} não encontrado')
    
    atleta_update = atleta_up.model_dump(exclude_unset=True)
    for key, value in atleta_update.items():
        setattr(atleta, key, value)
    
    
    await db_session.commit()
    await db_session.refresh(atleta)
    
    return atleta

@router.delete('/{id}', summary="Excluir atleta por id", status_code=status.HTTP_204_NO_CONTENT)
async def query(id: UUID4, db_session: DatabaseDependencies) -> None:
    atleta: AtletaModel = (await db_session.execute(select(AtletaModel).filter_by(id=id))).scalars().first()
    
    if not atleta:
        raise HTTPException(status_code=500, detail=f'atleta {nome} não encontrado')
    
    await db_session.delete(atleta)
    await db_session.commit()
    
    
