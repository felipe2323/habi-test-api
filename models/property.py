from sqlalchemy import Table, Column
from sqlalchemy.sql.sqltypes import BigInteger, Integer, String, Text
from config.db import meta

""" Model: Property to use ORM """

properties = Table(
    'property', meta ,
    Column('id', Integer, primary_key=True),
    Column('address', String(120)),
    Column('city', String(32)),
    Column('price', BigInteger),
    Column('description', Text),
    Column('year', Integer),
    
)
