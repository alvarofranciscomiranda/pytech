"""add farm unique key

Revision ID: 718928f28603
Revises: ab91558dfc20
Create Date: 2023-11-29 19:52:35.570417

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = '718928f28603'
down_revision: Union[str, None] = 'ab91558dfc20'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    pass


def downgrade() -> None:
    pass
