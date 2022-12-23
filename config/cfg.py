from sqlalchemy import create_engine, MetaData
from configparser import ConfigParser

config = ConfigParser()
config.read('config.ini')

meta = MetaData()

engine = create_engine()
conn = engine.connect()