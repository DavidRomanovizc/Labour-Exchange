from . import jobs
from . import users
from .postgres import metadata, engine

metadata.create_all(bind=engine)
