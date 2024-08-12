"""add content column to posts table

Revision ID: 425457e90228
Revises: f7027d144386
Create Date: 2024-08-12 12:35:45.737721

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = '425457e90228'
down_revision: Union[str, None] = 'f7027d144386'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    op.add_column('posts', sa.Column('content', sa.String(), nullable=False))
    pass


def downgrade() -> None:
    op.drop_column('posts', 'content')
    pass
