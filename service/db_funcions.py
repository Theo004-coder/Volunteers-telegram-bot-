from .database.py import get_session
from tables.py import Event, User

def add_user(
        tg_id, 
        name,
        tg_name,
        surname,
        patronymic,
        email,
        phone
        )
    with get_session as session:
        try:
            new_user = User(
            tg_id=tg_id,
            tg_name = tg_name,
            email=email,
            phone=phone,
            name=name,
            surname=surname,
            patronymic=patronymic
        )
        except Exception as e:
            session.rollback()
            raise e
            
def add_event(
            name,
            description
            )
    with get_session as session:
        try:
            new_ev = Event(
            name=name,
            description=description
            )

def find_user(name, surname, patronymic):
    with get_session() as session:
        user = session.query(User).filter_by(name=name, surname=surname, patronymic=patronymic).first()
        return user

def delete_user(name, surname, patronymic):
    with get_session() as session:
        user = session.query(User).filter_by(name=name, surname=surname, patronymic=patronymic).first()
        user.is_deleted = True
        
def delete_user(name_event):
    with get_session() as session:
        event = session.query(Event).filter_by(name_event=name).first()
        event.is_deleted = True

def find_event(name_event):
    with get_session() as session:
        event = session.query(Event).filter_by(name=name).first()
        return event
        
def get_events_for_user(name, surname, patronymic):
    with get_session() as session:
        user = session.query(User).filter_by(name=name, surname=surname, patronymic=patronymic).first()
        if user:
            return user.events  # список объектов Event
        return []
        
def get_users_for_event(name_event):
    with get_session() as session:
        event = session.query(Event).filter_by(name_event=name).first()
        if event:
            return event.users  # список объектов Event
        return []