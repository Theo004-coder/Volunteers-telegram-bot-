from sqlalchemy.ext.declarative import declarative_base
 
engine = create_engine('sqlite:///C:\Users\rom17\Documents\GitHub\Volunteers-telegram-bot-/users.db', echo=False)
Base = declarative_base()
 
