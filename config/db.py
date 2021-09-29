from sqlalchemy import create_engine, engine, MetaData

engine = create_engine("mysql+pymysql://pruebas:VGbt3Day5R@3.130.126.210:3309/habi_db")
meta = MetaData()
conn = engine.connect()
