"""Device Data added

Revision ID: 38e8537b40e4
Revises: 718928f28603
Create Date: 2023-12-06 19:01:22.479461

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = '38e8537b40e4'
down_revision: Union[str, None] = '718928f28603'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('inverter_data', sa.Column('pdc5', sa.Integer(), nullable=True))
    op.add_column('inverter_data', sa.Column('pdc6', sa.Integer(), nullable=True))
    op.add_column('inverter_data', sa.Column('yiel', sa.Integer(), nullable=True))
    op.add_column('inverter_data', sa.Column('udc5', sa.Integer(), nullable=True))
    op.add_column('inverter_data', sa.Column('udc6', sa.Integer(), nullable=True))
    op.add_column('inverter_data', sa.Column('uac1', sa.Integer(), nullable=True))
    op.add_column('inverter_data', sa.Column('uac2', sa.Integer(), nullable=True))
    op.add_column('inverter_data', sa.Column('uac3', sa.Integer(), nullable=True))
    op.add_column('inverter_data', sa.Column('idc5', sa.Integer(), nullable=True))
    op.add_column('inverter_data', sa.Column('idc6', sa.Integer(), nullable=True))
    op.add_column('inverter_data', sa.Column('cos', sa.Integer(), nullable=True))
    op.drop_column('inverter_data', 'yld')
    op.add_column('meter_data', sa.Column('yiel', sa.Integer(), nullable=True))
    op.add_column('meter_data', sa.Column('etotal_c', sa.Integer(), nullable=True))
    op.add_column('meter_data', sa.Column('etotal_forward', sa.Integer(), nullable=True))
    op.add_column('meter_data', sa.Column('etotal_reverse', sa.Integer(), nullable=True))
    op.add_column('meter_data', sa.Column('etotal_raw', sa.Integer(), nullable=True))
    op.drop_column('meter_data', 'yld')
    op.drop_column('meter_data', 'etotal_')
    # ### end Alembic commands ###


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('meter_data', sa.Column('etotal_', sa.INTEGER(), autoincrement=False, nullable=True))
    op.add_column('meter_data', sa.Column('yld', sa.INTEGER(), autoincrement=False, nullable=True))
    op.drop_column('meter_data', 'etotal_raw')
    op.drop_column('meter_data', 'etotal_reverse')
    op.drop_column('meter_data', 'etotal_forward')
    op.drop_column('meter_data', 'etotal_c')
    op.drop_column('meter_data', 'yiel')
    op.add_column('inverter_data', sa.Column('yld', sa.INTEGER(), autoincrement=False, nullable=True))
    op.drop_column('inverter_data', 'cos')
    op.drop_column('inverter_data', 'idc6')
    op.drop_column('inverter_data', 'idc5')
    op.drop_column('inverter_data', 'uac3')
    op.drop_column('inverter_data', 'uac2')
    op.drop_column('inverter_data', 'uac1')
    op.drop_column('inverter_data', 'udc6')
    op.drop_column('inverter_data', 'udc5')
    op.drop_column('inverter_data', 'yiel')
    op.drop_column('inverter_data', 'pdc6')
    op.drop_column('inverter_data', 'pdc5')
    # ### end Alembic commands ###
