import csv
import os

from sqlalchemy import create_engine
from sqlalchemy.orm import scoped_session, sessionmaker

engine = create_engine(os.getenv("DATABASE_URL"))
db = scoped_session(sessionmaker(bind=engine))


def main():
    kount = 0
    f = open("books.csv")
    has_header = csv.Sniffer().has_header(f.read(1024))
    f.seek(0)
    reader = csv.reader(f)
    if has_header:
        next(reader)
    for isbn, title, author, year in reader:
        db.execute("INSERT INTO books (isbn, title, author,published) VALUES (:isbn, :title, :author, :published)",
                   {"isbn": isbn, "title": title, "author": author, "published": year})
        kount += 1
        print(f"ISBN: {isbn} , Book numero= {kount}")
    print(f"Books inserted {kount}")
    db.commit()


if __name__ == "__main__":
    main()
