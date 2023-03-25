from sqlalchemy import Table, Column, String
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()

Items = Table(
    "Items",
    Base.metadata,
    Column("item_id", String(255), nullable=False, primary_key=True),
    Column("item_name", String(255), nullable=True),
    Column("item_description", String(255), nullable=True),
    Column("portion_kcal", String(255), nullable=True),
    Column("how", String(255), nullable=True),
    Column("producer_name", String(255), nullable=True),
)