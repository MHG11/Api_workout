from datetime import datetime
from contrib.models import BaseModel
from sqlalchemy import DateTime, Float, ForeignKey, Integer, String
from sqlalchemy.orm import Mapped, mapped_column, relationship



class AtletaModel(BaseModel):
    __tablename__='atleta'
    __table_args__ = {'extend_existing': True}
    
    pk_id: Mapped[int] = mapped_column(primary_key=True)
    nome: Mapped[str] = mapped_column(String(50))
    idade: Mapped[int] = mapped_column(Integer)
    cpf: Mapped[str] = mapped_column(String(14), unique=True)
    peso: Mapped[float] = mapped_column(Float)
    altura: Mapped[float] = mapped_column(Float)
    sexo: Mapped[str] = mapped_column(String(1))
    created_at: Mapped[datetime] = mapped_column(DateTime(timezone=True), default=datetime.now, onupdate=datetime.now)
    categorias: Mapped['CategoriaModel'] = relationship(back_populates='atleta', lazy='selectin')
    categoria_id: Mapped[int] = mapped_column(ForeignKey('categorias.pk_id'))
    centro_treinamento: Mapped['CentroTreinamentoModel'] = relationship(back_populates='atleta', lazy='selectin') 
    centro_treinamento_id: Mapped[int] = mapped_column(ForeignKey('centro_treinamento.pk_id'))