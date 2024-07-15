"""Adjust models for relationships

Revision ID: 39b5a0fce34e
Revises: 6334bf9680a6
Create Date: 2024-07-14 14:23:05.414287

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa
from sqlalchemy.dialects import postgresql

# revision identifiers, used by Alembic.
revision: str = '39b5a0fce34e'
down_revision: Union[str, None] = '6334bf9680a6'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('centro_treinamento')
    op.drop_table('atleta')
    op.drop_table('categorias')
    # ### end Alembic commands ###


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('categorias',
    sa.Column('pk_id', sa.INTEGER(), server_default=sa.text("nextval('categorias_pk_id_seq'::regclass)"), autoincrement=True, nullable=False),
    sa.Column('nome', sa.VARCHAR(length=50), autoincrement=False, nullable=False),
    sa.Column('id', sa.UUID(), autoincrement=False, nullable=False),
    sa.PrimaryKeyConstraint('pk_id', name='categorias_pkey'),
    sa.UniqueConstraint('nome', name='categorias_nome_key'),
    postgresql_ignore_search_path=False
    )
    op.create_table('atleta',
    sa.Column('pk_id', sa.INTEGER(), autoincrement=True, nullable=False),
    sa.Column('nome', sa.VARCHAR(length=50), autoincrement=False, nullable=False),
    sa.Column('cpf', sa.VARCHAR(length=11), autoincrement=False, nullable=False),
    sa.Column('idade', sa.INTEGER(), autoincrement=False, nullable=False),
    sa.Column('peso', sa.DOUBLE_PRECISION(precision=53), autoincrement=False, nullable=False),
    sa.Column('altura', sa.DOUBLE_PRECISION(precision=53), autoincrement=False, nullable=False),
    sa.Column('sexo', sa.VARCHAR(length=1), autoincrement=False, nullable=False),
    sa.Column('created_at', postgresql.TIMESTAMP(), autoincrement=False, nullable=False),
    sa.Column('categoria_id', sa.INTEGER(), autoincrement=False, nullable=False),
    sa.Column('centro_treinamento_id', sa.INTEGER(), autoincrement=False, nullable=False),
    sa.Column('id', sa.UUID(), autoincrement=False, nullable=False),
    sa.ForeignKeyConstraint(['categoria_id'], ['categorias.pk_id'], name='atleta_categoria_id_fkey'),
    sa.ForeignKeyConstraint(['centro_treinamento_id'], ['centro_treinamento.pk_id'], name='atleta_centro_treinamento_id_fkey'),
    sa.PrimaryKeyConstraint('pk_id', name='atleta_pkey'),
    sa.UniqueConstraint('cpf', name='atleta_cpf_key')
    )
    op.create_table('centro_treinamento',
    sa.Column('pk_id', sa.INTEGER(), autoincrement=True, nullable=False),
    sa.Column('nome', sa.VARCHAR(length=50), autoincrement=False, nullable=False),
    sa.Column('proprietario', sa.VARCHAR(length=50), autoincrement=False, nullable=False),
    sa.Column('endereco', sa.VARCHAR(length=50), autoincrement=False, nullable=False),
    sa.Column('id', sa.UUID(), autoincrement=False, nullable=False),
    sa.PrimaryKeyConstraint('pk_id', name='centro_treinamento_pkey'),
    sa.UniqueConstraint('nome', name='centro_treinamento_nome_key')
    )
    # ### end Alembic commands ###
