from contrib.models import BaseModel
from sqlalchemy import String
from sqlalchemy.orm import Mapped, mapped_column, relationship



class CategoriaModel(BaseModel):
    __tablename__='categorias'
    __table_args__ = {'extend_existing': True}
    
    pk_id: Mapped[int] = mapped_column(primary_key=True)
    nome: Mapped[str] = mapped_column(String(50), unique=True)
    atleta: Mapped['AtletaModel'] = relationship(back_populates='categorias') 