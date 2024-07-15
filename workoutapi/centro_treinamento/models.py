from contrib.models import BaseModel
from sqlalchemy import String
from sqlalchemy.orm import Mapped, mapped_column, relationship



class CentroTreinamentoModel(BaseModel):
    __tablename__='centro_treinamento'
    __table_args__ = {'extend_existing': True}
    
    pk_id: Mapped[int] = mapped_column(primary_key=True)
    nome: Mapped[str] = mapped_column( unique=True)
    proprietario: Mapped[str] = mapped_column(String(50))
    endereco: Mapped[str] = mapped_column(String(50))
    atleta: Mapped['AtletaModel'] = relationship(back_populates='centro_treinamento') 