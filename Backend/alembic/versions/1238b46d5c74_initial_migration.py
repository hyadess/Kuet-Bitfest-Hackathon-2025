"""Initial migration

Revision ID: 1238b46d5c74
Revises: 590dd2294cd1
Create Date: 2025-01-03 13:59:55.518058

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = '1238b46d5c74'
down_revision: Union[str, None] = '590dd2294cd1'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('user_train', sa.Column('is_approved', sa.Boolean(), nullable=False))
    # ### end Alembic commands ###


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('user_train', 'is_approved')
    # ### end Alembic commands ###
