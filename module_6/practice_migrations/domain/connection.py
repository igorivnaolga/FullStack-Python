from sqlalchemy.engine import create_engine
from sqlalchemy.orm import sessionmaker

db_url = "sqlite:///test.db"
# db_url = "postgresql://postgres:postgres@localhost:5432/lecture_6_practice"

engine = create_engine(db_url)
Session = sessionmaker(bind=engine)
session = Session()
