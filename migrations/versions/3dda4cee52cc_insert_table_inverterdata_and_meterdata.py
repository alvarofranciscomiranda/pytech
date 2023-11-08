"""Insert table InverterData and MeterData

Revision ID: 3dda4cee52cc
Revises: 2305fff1a19b
Create Date: 2023-11-08 18:56:13.724099

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = '3dda4cee52cc'
down_revision: Union[str, None] = '2305fff1a19b'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('inverter_data',
    sa.Column('inverter_id', sa.Integer(), nullable=False),
    sa.Column('read_at', sa.DateTime(), nullable=False),
    sa.Column('pac', sa.Integer(), nullable=True),
    sa.Column('pdc1', sa.Integer(), nullable=True),
    sa.Column('pdc2', sa.Integer(), nullable=True),
    sa.Column('pdc3', sa.Integer(), nullable=True),
    sa.Column('pdc4', sa.Integer(), nullable=True),
    sa.Column('yld', sa.Integer(), nullable=True),
    sa.Column('udc1', sa.Integer(), nullable=True),
    sa.Column('udc2', sa.Integer(), nullable=True),
    sa.Column('udc3', sa.Integer(), nullable=True),
    sa.Column('udc4', sa.Integer(), nullable=True),
    sa.Column('temperature', sa.Integer(), nullable=True),
    sa.Column('uac', sa.Integer(), nullable=True),
    sa.Column('status', sa.Integer(), nullable=True),
    sa.Column('error', sa.Integer(), nullable=True),
    sa.Column('iac', sa.Integer(), nullable=True),
    sa.Column('idc1', sa.Integer(), nullable=True),
    sa.Column('idc2', sa.Integer(), nullable=True),
    sa.Column('idc3', sa.Integer(), nullable=True),
    sa.Column('idc4', sa.Integer(), nullable=True),
    sa.ForeignKeyConstraint(['inverter_id'], ['inverter.id'], ),
    sa.PrimaryKeyConstraint('inverter_id', 'read_at')
    )
    op.create_table('meter_data',
    sa.Column('meter_id', sa.Integer(), nullable=False),
    sa.Column('read_at', sa.DateTime(), nullable=False),
    sa.Column('pac', sa.Integer(), nullable=True),
    sa.Column('yld', sa.Integer(), nullable=True),
    sa.Column('status', sa.Integer(), nullable=True),
    sa.Column('error', sa.Integer(), nullable=True),
    sa.Column('etotal_', sa.Integer(), nullable=True),
    sa.Column('pac1', sa.Integer(), nullable=True),
    sa.Column('pac2', sa.Integer(), nullable=True),
    sa.Column('pac3', sa.Integer(), nullable=True),
    sa.Column('uac1', sa.Integer(), nullable=True),
    sa.Column('uac2', sa.Integer(), nullable=True),
    sa.Column('uac3', sa.Integer(), nullable=True),
    sa.Column('qac1', sa.Integer(), nullable=True),
    sa.Column('qac2', sa.Integer(), nullable=True),
    sa.Column('qac3', sa.Integer(), nullable=True),
    sa.Column('iac1', sa.Integer(), nullable=True),
    sa.Column('iac2', sa.Integer(), nullable=True),
    sa.Column('iac3', sa.Integer(), nullable=True),
    sa.Column('fac', sa.Integer(), nullable=True),
    sa.Column('cos', sa.Integer(), nullable=True),
    sa.Column('pac_raw', sa.Integer(), nullable=True),
    sa.ForeignKeyConstraint(['meter_id'], ['meter.id'], ),
    sa.PrimaryKeyConstraint('meter_id', 'read_at')
    )
    # ### end Alembic commands ###


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('meter_data')
    op.drop_table('inverter_data')
    # ### end Alembic commands ###
