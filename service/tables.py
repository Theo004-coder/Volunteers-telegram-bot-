from sqlalchemy import (
    Column,
    Integer,
    String,
    DateTime,
    Text,
    ForeignKey,
    Boolean,
    Float,
    Date
)
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship


base = declarative_base()

StudentsEvent = Table("StudentsEvent",
    Column('id', Integer, primary_key=True),
    Column('EventId', Integer, ForeignKey('Event.id')),
    Column('StudentId', Integer, ForeignKey('User.id')))

class Event(base):
    __tablename__ = "events"
    id = Column(Integer, autoincrement=True, primary_key=True)
    name = Column(String(32), nullable=False, unique=True)
    description = Column(String(1024), nullable=True)
    
    id_student = Column(Integer, ForeignKey("user.id"))
    students = relationship("User", secondary=StudentsEvent, backref="User")

class User(base):
    __tablename__ = "users"
    id = Column(Integer, autoincrement=True, primary_key=True)
    tg_id = Column(Integer, unique=True, nullable=False)
    is_admin = Column(Boolean, nullable=False, default=False)

    name = Column(String, nullable=True)
    surname = Column(String, nullable=True)
    patronymic = Column(String, nullable=True)

    email = Column(String, nullable=False, unique=True)
    phone_number = Column(String, nullable=False, unique=True)
    
    is_deleted = Column(Boolean, nullable=True, default=False)

    id_event = Column(Integer, ForeignKey("event.id"))
    event = relationship("Event", secondary=StudentsEvent, backref="Event")
