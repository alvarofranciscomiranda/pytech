"""Add table InverterData and MeterData

Revision ID: 2305fff1a19b
Revises: 15d81fecb674
Create Date: 2023-11-08 18:46:14.246829

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = '2305fff1a19b'
down_revision: Union[str, None] = '15d81fecb674'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    pass
    # ### end Alembic commands ###


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    pass
    # ### end Alembic commands ###