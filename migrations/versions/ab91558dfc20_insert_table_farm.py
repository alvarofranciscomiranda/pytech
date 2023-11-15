"""Insert table Farm

Revision ID: ab91558dfc20
Revises: 3dda4cee52cc
Create Date: 2023-11-08 19:09:09.959765

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = 'ab91558dfc20'
down_revision: Union[str, None] = '3dda4cee52cc'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('farm',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('name', sa.String(length=60), nullable=True),
    sa.Column('created_at', sa.DateTime(), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )
    op.add_column('inverter', sa.Column('farm_id', sa.Integer(), nullable=True))
    op.create_foreign_key(None, 'inverter', 'farm', ['farm_id'], ['id'])
    op.add_column('meter', sa.Column('farm_id', sa.Integer(), nullable=True))
    op.create_foreign_key(None, 'meter', 'farm', ['farm_id'], ['id'])
    op.add_column('sensor', sa.Column('farm_id', sa.Integer(), nullable=True))
    op.create_foreign_key(None, 'sensor', 'farm', ['farm_id'], ['id'])
    # ### end Alembic commands ###


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_constraint(None, 'sensor', type_='foreignkey')
    op.drop_column('sensor', 'farm_id')
    op.drop_constraint(None, 'meter', type_='foreignkey')
    op.drop_column('meter', 'farm_id')
    op.drop_constraint(None, 'inverter', type_='foreignkey')
    op.drop_column('inverter', 'farm_id')
    op.drop_table('farm')
    # ### end Alembic commands ###