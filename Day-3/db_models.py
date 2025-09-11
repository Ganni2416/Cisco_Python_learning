from sqlalchemy.orm import declarative_base
from sqlalchemy import Column, Integer, String, Float, Boolean
Base = declarative_base()
class Employee(Base):
    __tablename__ = 'employee'
    id = Column(Integer, primary_key=True)
    name = Column(String(50), nullable=False)
    age = Column(Integer, nullable=False)
    salary = Column(Float, nullable=False)
    is_active = Column(Boolean, default=True)
    def __repr__(self):
        return f"Employee(id={self.id}, name='{self.name}', age={self.age}, salary={self.salary}, active={self.is_active})"