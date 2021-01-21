from sqlalchemy import Integer, Column, ForeignKey, String, Boolean
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import create_engine

# from settings.consts import DB_URL
DB_URL = 'postgresql+psycopg2://andrii_fesh:vbhjcz4455@0.0.0.0:5432/lnu'

# Configure a Session class.
Session = sessionmaker()

# Create an engine which the Session will use for connections.
engine = create_engine(DB_URL)

# Create a configured Session class.
Session.configure(bind=engine)

# Create a Session
session = Session()

# Create a base for the models to build upon.
Base = declarative_base()


class Employee(Base):
    __tablename__ = 'employers'

    employee_id = Column(Integer, primary_key=True)
    name = Column(String, nullable=False)
    employee_url = Column(String)
    faculty_id = Column(Integer, ForeignKey('faculties.faculty_id'))


class Faculty(Base):
    __tablename__ = 'faculties'

    faculty_id = Column(Integer, primary_key=True)
    faculty_name = Column(String, nullable=False)
    faculty_url = Column(String, nullable=False)


class Department(Base):
    __tablename__ = 'departments'

    department_id = Column(Integer, primary_key=True)
    department_name = Column(String, nullable=False)
    department_url = Column(String, nullable=False)
    faculty_id = Column(Integer, ForeignKey('faculties.faculty_id'))


class User(Base):
    __tablename__ = 'users'
    chat_id = Column(Integer, primary_key=True)
    faculty = Column(String)
    admin_right = Column(Boolean, default=False)


Base.metadata.create_all(engine)
