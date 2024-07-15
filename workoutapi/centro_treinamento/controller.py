from workoutapi.centro_treinamento.schemas import CentroTreinamentoIn, CentroTreinamentoOut
from workoutapi.centro_treinamento.models import CentroTreinamentoModel, CentroTreinamentoModel
from contrib.dependencies import DatabaseDependencies
from fastapi import APIRouter, Body, status, HTTPException
from uuid import uuid4
from pydantic import UUID4
from sqlalchemy.future import select

router = APIRouter()

@router.post('/', summary="Criar um novo centro de treinamento", status_code=status.HTTP_201_CREATED, response_model=CentroTreinamentoOut)
async def post(db_session: DatabaseDependencies, centro_treinamento_in: CentroTreinamentoIn = Body(...)) -> CentroTreinamentoOut:
    
    centro_treinamento_out = CentroTreinamentoOut(id=uuid4(), **centro_treinamento_in.model_dump())
    centro_treinamento_model = CentroTreinamentoModel(**centro_treinamento_out.model_dump())
    
    db_session.add(centro_treinamento_model)
    await db_session.commit()
    return centro_treinamento_out

@router.get('/', summary="Consultar todos os centros de treinamento", status_code=status.HTTP_200_OK, response_model=list[CentroTreinamentoOut])
async def query(db_session: DatabaseDependencies) -> list[CentroTreinamentoOut]:
    centro_treinamentos: list[CentroTreinamentoModel] = (await db_session.execute(select(CentroTreinamentoModel))).scalars().all()
    
    return centro_treinamentos

@router.get('/{id}', summary="Consultar centro por id", status_code=status.HTTP_200_OK, response_model=CentroTreinamentoOut)
async def query(id: UUID4, db_session: DatabaseDependencies) -> list[CentroTreinamentoOut]:
    centro_treinamento: CentroTreinamentoModel = (await db_session.execute(select(CentroTreinamentoModel).filter_by(id=id))).scalars().first()
    
    if not centro_treinamento:
        raise HTTPException(status_code=404, detail=f"Centro nao encontrada no id {id}")
    
    
    return centro_treinamento