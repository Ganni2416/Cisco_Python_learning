from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from db_models import Base, Employee
engine=create_engine('sqlite:///employee.db', echo=True)
Base.metadata.create_all(engine)
Session=sessionmaker(bind=engine)
session=Session()