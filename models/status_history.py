from sqlalchemy import Table, Column
from sqlalchemy.sql.sqltypes import DateTime, Integer
from config.db import meta

status_histories = Table(
    'status_history', meta ,
    Column('id', Integer, primary_key=True),
    Column('property_id', Integer),
    Column('status_id', Integer),
    Column('update_date', DateTime),    
)