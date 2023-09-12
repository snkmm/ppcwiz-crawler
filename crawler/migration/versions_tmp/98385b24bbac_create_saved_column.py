"""create saved column

Revision ID: 98385b24bbac
Revises: d58e26390e3c
Create Date: 2021-04-08 16:49:42.942429

"""
from alembic import op
import sqlalchemy as sa
from sqlalchemy.dialects import mysql

# revision identifiers, used by Alembic.
revision = '98385b24bbac'
down_revision = 'd58e26390e3c'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('sb_filter_neg_keyword',
        sa.Column('saved', sa.Float(), nullable=True)
    )
    op.add_column('sp_filter_neg_keyword',
        sa.Column('saved', sa.Float(), nullable=True)
    )
    op.alter_column('dtb_profile', 'created_datetime',
               existing_type=mysql.DATETIME(),
               server_default=sa.text('now()'),
               existing_nullable=True)
    op.alter_column('dtb_profile', 'updated_datetime',
               existing_type=mysql.DATETIME(),
               server_default=sa.text('now()'),
               existing_nullable=True)
    op.alter_column('dtb_user', 'created_datetime',
               existing_type=mysql.DATETIME(),
               server_default=sa.text('now()'),
               existing_nullable=True)
    op.alter_column('dtb_user', 'updated_datetime',
               existing_type=mysql.DATETIME(),
               server_default=sa.text('now()'),
               existing_nullable=True)
    op.alter_column('sb_ad_group', 'created_datetime',
               existing_type=mysql.DATETIME(),
               server_default=sa.text('now()'),
               existing_nullable=True)
    op.alter_column('sb_ad_group', 'updated_datetime',
               existing_type=mysql.DATETIME(),
               server_default=sa.text('now()'),
               existing_nullable=True)
    op.alter_column('sb_campaign', 'created_datetime',
               existing_type=mysql.DATETIME(),
               server_default=sa.text('now()'),
               existing_nullable=True)
    op.alter_column('sb_campaign', 'updated_datetime',
               existing_type=mysql.DATETIME(),
               server_default=sa.text('now()'),
               existing_nullable=True)
    op.alter_column('sb_filter_neg_keyword', 'created_datetime',
               existing_type=mysql.DATETIME(),
               server_default=sa.text('now()'),
               existing_nullable=True)
    op.alter_column('sb_filter_neg_keyword', 'updated_datetime',
               existing_type=mysql.DATETIME(),
               server_default=sa.text('now()'),
               existing_nullable=True)
    op.alter_column('sb_keyword', 'created_datetime',
               existing_type=mysql.DATETIME(),
               server_default=sa.text('now()'),
               existing_nullable=True)
    op.alter_column('sb_keyword', 'updated_datetime',
               existing_type=mysql.DATETIME(),
               server_default=sa.text('now()'),
               existing_nullable=True)
    op.alter_column('sb_keyword_report', 'created_datetime',
               existing_type=mysql.DATETIME(),
               server_default=sa.text('now()'),
               existing_nullable=True)
    op.alter_column('sb_keyword_report', 'updated_datetime',
               existing_type=mysql.DATETIME(),
               server_default=sa.text('now()'),
               existing_nullable=True)
    op.alter_column('sb_neg_keyword', 'created_datetime',
               existing_type=mysql.DATETIME(),
               server_default=sa.text('now()'),
               existing_nullable=True)
    op.alter_column('sb_neg_keyword', 'updated_datetime',
               existing_type=mysql.DATETIME(),
               server_default=sa.text('now()'),
               existing_nullable=True)
    op.alter_column('sd_ad_group', 'created_datetime',
               existing_type=mysql.DATETIME(),
               server_default=sa.text('now()'),
               existing_nullable=True)
    op.alter_column('sd_ad_group', 'updated_datetime',
               existing_type=mysql.DATETIME(),
               server_default=sa.text('now()'),
               existing_nullable=True)
    op.alter_column('sd_campaign', 'created_datetime',
               existing_type=mysql.DATETIME(),
               server_default=sa.text('now()'),
               existing_nullable=True)
    op.alter_column('sd_campaign', 'updated_datetime',
               existing_type=mysql.DATETIME(),
               server_default=sa.text('now()'),
               existing_nullable=True)
    op.alter_column('sd_neg_target', 'created_datetime',
               existing_type=mysql.DATETIME(),
               server_default=sa.text('now()'),
               existing_nullable=True)
    op.alter_column('sd_neg_target', 'updated_datetime',
               existing_type=mysql.DATETIME(),
               server_default=sa.text('now()'),
               existing_nullable=True)
    op.alter_column('sd_product_ad', 'created_datetime',
               existing_type=mysql.DATETIME(),
               server_default=sa.text('now()'),
               existing_nullable=True)
    op.alter_column('sd_product_ad', 'updated_datetime',
               existing_type=mysql.DATETIME(),
               server_default=sa.text('now()'),
               existing_nullable=True)
    op.alter_column('sd_target', 'created_datetime',
               existing_type=mysql.DATETIME(),
               server_default=sa.text('now()'),
               existing_nullable=True)
    op.alter_column('sd_target', 'updated_datetime',
               existing_type=mysql.DATETIME(),
               server_default=sa.text('now()'),
               existing_nullable=True)
    op.alter_column('sd_target_report', 'created_datetime',
               existing_type=mysql.DATETIME(),
               server_default=sa.text('now()'),
               existing_nullable=True)
    op.alter_column('sd_target_report', 'updated_datetime',
               existing_type=mysql.DATETIME(),
               server_default=sa.text('now()'),
               existing_nullable=True)
    op.alter_column('sp_ad_group', 'created_datetime',
               existing_type=mysql.DATETIME(),
               server_default=sa.text('now()'),
               existing_nullable=True)
    op.alter_column('sp_ad_group', 'updated_datetime',
               existing_type=mysql.DATETIME(),
               server_default=sa.text('now()'),
               existing_nullable=True)
    op.alter_column('sp_camp_neg_keyword', 'created_datetime',
               existing_type=mysql.DATETIME(),
               server_default=sa.text('now()'),
               existing_nullable=True)
    op.alter_column('sp_camp_neg_keyword', 'updated_datetime',
               existing_type=mysql.DATETIME(),
               server_default=sa.text('now()'),
               existing_nullable=True)
    op.alter_column('sp_campaign', 'created_datetime',
               existing_type=mysql.DATETIME(),
               server_default=sa.text('now()'),
               existing_nullable=True)
    op.alter_column('sp_campaign', 'updated_datetime',
               existing_type=mysql.DATETIME(),
               server_default=sa.text('now()'),
               existing_nullable=True)
    op.alter_column('sp_filter_neg_keyword', 'created_datetime',
               existing_type=mysql.DATETIME(),
               server_default=sa.text('now()'),
               existing_nullable=True)
    op.alter_column('sp_filter_neg_keyword', 'updated_datetime',
               existing_type=mysql.DATETIME(),
               server_default=sa.text('now()'),
               existing_nullable=True)
    op.alter_column('sp_keyword', 'created_datetime',
               existing_type=mysql.DATETIME(),
               server_default=sa.text('now()'),
               existing_nullable=True)
    op.alter_column('sp_keyword', 'updated_datetime',
               existing_type=mysql.DATETIME(),
               server_default=sa.text('now()'),
               existing_nullable=True)
    op.alter_column('sp_keyword_report', 'created_datetime',
               existing_type=mysql.DATETIME(),
               server_default=sa.text('now()'),
               existing_nullable=True)
    op.alter_column('sp_keyword_report', 'updated_datetime',
               existing_type=mysql.DATETIME(),
               server_default=sa.text('now()'),
               existing_nullable=True)
    op.alter_column('sp_neg_keyword', 'created_datetime',
               existing_type=mysql.DATETIME(),
               server_default=sa.text('now()'),
               existing_nullable=True)
    op.alter_column('sp_neg_keyword', 'updated_datetime',
               existing_type=mysql.DATETIME(),
               server_default=sa.text('now()'),
               existing_nullable=True)
    op.alter_column('sp_neg_target', 'created_datetime',
               existing_type=mysql.DATETIME(),
               server_default=sa.text('now()'),
               existing_nullable=True)
    op.alter_column('sp_neg_target', 'updated_datetime',
               existing_type=mysql.DATETIME(),
               server_default=sa.text('now()'),
               existing_nullable=True)
    op.alter_column('sp_product_ad', 'created_datetime',
               existing_type=mysql.DATETIME(),
               server_default=sa.text('now()'),
               existing_nullable=True)
    op.alter_column('sp_product_ad', 'updated_datetime',
               existing_type=mysql.DATETIME(),
               server_default=sa.text('now()'),
               existing_nullable=True)
    op.alter_column('sp_product_ad_report', 'created_datetime',
               existing_type=mysql.DATETIME(),
               server_default=sa.text('now()'),
               existing_nullable=True)
    op.alter_column('sp_product_ad_report', 'updated_datetime',
               existing_type=mysql.DATETIME(),
               server_default=sa.text('now()'),
               existing_nullable=True)
    op.alter_column('sp_target', 'created_datetime',
               existing_type=mysql.DATETIME(),
               server_default=sa.text('now()'),
               existing_nullable=True)
    op.alter_column('sp_target', 'updated_datetime',
               existing_type=mysql.DATETIME(),
               server_default=sa.text('now()'),
               existing_nullable=True)
    op.alter_column('sp_target_report', 'created_datetime',
               existing_type=mysql.DATETIME(),
               server_default=sa.text('now()'),
               existing_nullable=True)
    op.alter_column('sp_target_report', 'updated_datetime',
               existing_type=mysql.DATETIME(),
               server_default=sa.text('now()'),
               existing_nullable=True)
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.alter_column('sp_target_report', 'updated_datetime',
               existing_type=mysql.DATETIME(),
               server_default=sa.text('CURRENT_TIMESTAMP'),
               existing_nullable=True)
    op.alter_column('sp_target_report', 'created_datetime',
               existing_type=mysql.DATETIME(),
               server_default=sa.text('CURRENT_TIMESTAMP'),
               existing_nullable=True)
    op.alter_column('sp_target', 'updated_datetime',
               existing_type=mysql.DATETIME(),
               server_default=sa.text('CURRENT_TIMESTAMP'),
               existing_nullable=True)
    op.alter_column('sp_target', 'created_datetime',
               existing_type=mysql.DATETIME(),
               server_default=sa.text('CURRENT_TIMESTAMP'),
               existing_nullable=True)
    op.alter_column('sp_product_ad_report', 'updated_datetime',
               existing_type=mysql.DATETIME(),
               server_default=sa.text('CURRENT_TIMESTAMP'),
               existing_nullable=True)
    op.alter_column('sp_product_ad_report', 'created_datetime',
               existing_type=mysql.DATETIME(),
               server_default=sa.text('CURRENT_TIMESTAMP'),
               existing_nullable=True)
    op.alter_column('sp_product_ad', 'updated_datetime',
               existing_type=mysql.DATETIME(),
               server_default=sa.text('CURRENT_TIMESTAMP'),
               existing_nullable=True)
    op.alter_column('sp_product_ad', 'created_datetime',
               existing_type=mysql.DATETIME(),
               server_default=sa.text('CURRENT_TIMESTAMP'),
               existing_nullable=True)
    op.alter_column('sp_neg_target', 'updated_datetime',
               existing_type=mysql.DATETIME(),
               server_default=sa.text('CURRENT_TIMESTAMP'),
               existing_nullable=True)
    op.alter_column('sp_neg_target', 'created_datetime',
               existing_type=mysql.DATETIME(),
               server_default=sa.text('CURRENT_TIMESTAMP'),
               existing_nullable=True)
    op.alter_column('sp_neg_keyword', 'updated_datetime',
               existing_type=mysql.DATETIME(),
               server_default=sa.text('CURRENT_TIMESTAMP'),
               existing_nullable=True)
    op.alter_column('sp_neg_keyword', 'created_datetime',
               existing_type=mysql.DATETIME(),
               server_default=sa.text('CURRENT_TIMESTAMP'),
               existing_nullable=True)
    op.alter_column('sp_keyword_report', 'updated_datetime',
               existing_type=mysql.DATETIME(),
               server_default=sa.text('CURRENT_TIMESTAMP'),
               existing_nullable=True)
    op.alter_column('sp_keyword_report', 'created_datetime',
               existing_type=mysql.DATETIME(),
               server_default=sa.text('CURRENT_TIMESTAMP'),
               existing_nullable=True)
    op.alter_column('sp_keyword', 'updated_datetime',
               existing_type=mysql.DATETIME(),
               server_default=sa.text('CURRENT_TIMESTAMP'),
               existing_nullable=True)
    op.alter_column('sp_keyword', 'created_datetime',
               existing_type=mysql.DATETIME(),
               server_default=sa.text('CURRENT_TIMESTAMP'),
               existing_nullable=True)
    op.alter_column('sp_filter_neg_keyword', 'updated_datetime',
               existing_type=mysql.DATETIME(),
               server_default=sa.text('CURRENT_TIMESTAMP'),
               existing_nullable=True)
    op.alter_column('sp_filter_neg_keyword', 'created_datetime',
               existing_type=mysql.DATETIME(),
               server_default=sa.text('CURRENT_TIMESTAMP'),
               existing_nullable=True)
    op.alter_column('sp_campaign', 'updated_datetime',
               existing_type=mysql.DATETIME(),
               server_default=sa.text('CURRENT_TIMESTAMP'),
               existing_nullable=True)
    op.alter_column('sp_campaign', 'created_datetime',
               existing_type=mysql.DATETIME(),
               server_default=sa.text('CURRENT_TIMESTAMP'),
               existing_nullable=True)
    op.alter_column('sp_camp_neg_keyword', 'updated_datetime',
               existing_type=mysql.DATETIME(),
               server_default=sa.text('CURRENT_TIMESTAMP'),
               existing_nullable=True)
    op.alter_column('sp_camp_neg_keyword', 'created_datetime',
               existing_type=mysql.DATETIME(),
               server_default=sa.text('CURRENT_TIMESTAMP'),
               existing_nullable=True)
    op.alter_column('sp_ad_group', 'updated_datetime',
               existing_type=mysql.DATETIME(),
               server_default=sa.text('CURRENT_TIMESTAMP'),
               existing_nullable=True)
    op.alter_column('sp_ad_group', 'created_datetime',
               existing_type=mysql.DATETIME(),
               server_default=sa.text('CURRENT_TIMESTAMP'),
               existing_nullable=True)
    op.alter_column('sd_target_report', 'updated_datetime',
               existing_type=mysql.DATETIME(),
               server_default=sa.text('CURRENT_TIMESTAMP'),
               existing_nullable=True)
    op.alter_column('sd_target_report', 'created_datetime',
               existing_type=mysql.DATETIME(),
               server_default=sa.text('CURRENT_TIMESTAMP'),
               existing_nullable=True)
    op.alter_column('sd_target', 'updated_datetime',
               existing_type=mysql.DATETIME(),
               server_default=sa.text('CURRENT_TIMESTAMP'),
               existing_nullable=True)
    op.alter_column('sd_target', 'created_datetime',
               existing_type=mysql.DATETIME(),
               server_default=sa.text('CURRENT_TIMESTAMP'),
               existing_nullable=True)
    op.alter_column('sd_product_ad', 'updated_datetime',
               existing_type=mysql.DATETIME(),
               server_default=sa.text('CURRENT_TIMESTAMP'),
               existing_nullable=True)
    op.alter_column('sd_product_ad', 'created_datetime',
               existing_type=mysql.DATETIME(),
               server_default=sa.text('CURRENT_TIMESTAMP'),
               existing_nullable=True)
    op.alter_column('sd_neg_target', 'updated_datetime',
               existing_type=mysql.DATETIME(),
               server_default=sa.text('CURRENT_TIMESTAMP'),
               existing_nullable=True)
    op.alter_column('sd_neg_target', 'created_datetime',
               existing_type=mysql.DATETIME(),
               server_default=sa.text('CURRENT_TIMESTAMP'),
               existing_nullable=True)
    op.alter_column('sd_campaign', 'updated_datetime',
               existing_type=mysql.DATETIME(),
               server_default=sa.text('CURRENT_TIMESTAMP'),
               existing_nullable=True)
    op.alter_column('sd_campaign', 'created_datetime',
               existing_type=mysql.DATETIME(),
               server_default=sa.text('CURRENT_TIMESTAMP'),
               existing_nullable=True)
    op.alter_column('sd_ad_group', 'updated_datetime',
               existing_type=mysql.DATETIME(),
               server_default=sa.text('CURRENT_TIMESTAMP'),
               existing_nullable=True)
    op.alter_column('sd_ad_group', 'created_datetime',
               existing_type=mysql.DATETIME(),
               server_default=sa.text('CURRENT_TIMESTAMP'),
               existing_nullable=True)
    op.alter_column('sb_neg_keyword', 'updated_datetime',
               existing_type=mysql.DATETIME(),
               server_default=sa.text('CURRENT_TIMESTAMP'),
               existing_nullable=True)
    op.alter_column('sb_neg_keyword', 'created_datetime',
               existing_type=mysql.DATETIME(),
               server_default=sa.text('CURRENT_TIMESTAMP'),
               existing_nullable=True)
    op.alter_column('sb_keyword_report', 'updated_datetime',
               existing_type=mysql.DATETIME(),
               server_default=sa.text('CURRENT_TIMESTAMP'),
               existing_nullable=True)
    op.alter_column('sb_keyword_report', 'created_datetime',
               existing_type=mysql.DATETIME(),
               server_default=sa.text('CURRENT_TIMESTAMP'),
               existing_nullable=True)
    op.alter_column('sb_keyword', 'updated_datetime',
               existing_type=mysql.DATETIME(),
               server_default=sa.text('CURRENT_TIMESTAMP'),
               existing_nullable=True)
    op.alter_column('sb_keyword', 'created_datetime',
               existing_type=mysql.DATETIME(),
               server_default=sa.text('CURRENT_TIMESTAMP'),
               existing_nullable=True)
    op.alter_column('sb_filter_neg_keyword', 'updated_datetime',
               existing_type=mysql.DATETIME(),
               server_default=sa.text('CURRENT_TIMESTAMP'),
               existing_nullable=True)
    op.alter_column('sb_filter_neg_keyword', 'created_datetime',
               existing_type=mysql.DATETIME(),
               server_default=sa.text('CURRENT_TIMESTAMP'),
               existing_nullable=True)
    op.alter_column('sb_campaign', 'updated_datetime',
               existing_type=mysql.DATETIME(),
               server_default=sa.text('CURRENT_TIMESTAMP'),
               existing_nullable=True)
    op.alter_column('sb_campaign', 'created_datetime',
               existing_type=mysql.DATETIME(),
               server_default=sa.text('CURRENT_TIMESTAMP'),
               existing_nullable=True)
    op.alter_column('sb_ad_group', 'updated_datetime',
               existing_type=mysql.DATETIME(),
               server_default=sa.text('CURRENT_TIMESTAMP'),
               existing_nullable=True)
    op.alter_column('sb_ad_group', 'created_datetime',
               existing_type=mysql.DATETIME(),
               server_default=sa.text('CURRENT_TIMESTAMP'),
               existing_nullable=True)
    op.alter_column('dtb_user', 'updated_datetime',
               existing_type=mysql.DATETIME(),
               server_default=sa.text('CURRENT_TIMESTAMP'),
               existing_nullable=True)
    op.alter_column('dtb_user', 'created_datetime',
               existing_type=mysql.DATETIME(),
               server_default=sa.text('CURRENT_TIMESTAMP'),
               existing_nullable=True)
    op.alter_column('dtb_profile', 'updated_datetime',
               existing_type=mysql.DATETIME(),
               server_default=sa.text('CURRENT_TIMESTAMP'),
               existing_nullable=True)
    op.alter_column('dtb_profile', 'created_datetime',
               existing_type=mysql.DATETIME(),
               server_default=sa.text('CURRENT_TIMESTAMP'),
               existing_nullable=True)
    # ### end Alembic commands ###