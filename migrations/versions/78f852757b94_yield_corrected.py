"""Yield corrected

Revision ID: 78f852757b94
Revises: 38e8537b40e4
Create Date: 2023-12-06 19:06:50.377230

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = '78f852757b94'
down_revision: Union[str, None] = '38e8537b40e4'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('inverter_data', sa.Column('yield', sa.Integer(), nullable=True))
    op.drop_column('inverter_data', 'yiel')
    op.add_column('meter_data', sa.Column('yield', sa.Integer(), nullable=True))
    op.drop_column('meter_data', 'yiel')
    # ### end Alembic commands ###


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('meter_data', sa.Column('yiel', sa.INTEGER(), autoincrement=False, nullable=True))
    op.drop_column('meter_data', 'yield')
    op.add_column('inverter_data', sa.Column('yiel', sa.INTEGER(), autoincrement=False, nullable=True))
    op.drop_column('inverter_data', 'yield')
    # ### end Alembic commands ###