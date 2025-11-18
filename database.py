from sqlalchemy.ext.declarative import declarative_base
 
engine = create_engine('sqlite:///C:\\students.db', echo=False)
Base = declarative_base()
 
