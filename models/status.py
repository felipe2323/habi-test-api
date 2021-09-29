from sqlalchemy import Table, Column
from sqlalchemy.sql.sqltypes import Integer, String
from config.db import meta

""" Model: Status to use ORM """

status = Table(
    'status', meta ,
    Column('id', Integer, primary_key=True),
    Column('name', String(32)),
    Column('label', String(64)),    
)