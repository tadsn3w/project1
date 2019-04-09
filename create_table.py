# import os

# from sqlalchemy import create_engine
# from sqlalchemy.orm import scoped_session, sessionmaker

# engine = create_engine(os.getenv("DATABASE_URL"))
# db = scoped_session(sessionmaker(bind=engine))


# def main():
#     db.execute("CREATE TABLE users(id SERIAL PRIMARY KEY,user_name VARCHAR(20) NOT NULL,email VARCHAR(100) NOT NULL,password VARCHAR(30) NOT NULL);")


# if __name__ == "__main__":
#     main()

from sqlalchemy import MetaData
from sqlalchemy import Table, Column
from sqlalchemy import Integer, String

metadata = MetaData()
user_table =
