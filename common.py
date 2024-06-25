
from typing import List
from pydantic import BaseModel, EmailStr
from sqlalchemy import create_engine, Column, Integer, String, Table, ForeignKey, Text
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship, sessionmaker
from sqlalchemy.sql import text

Base = declarative_base()

# Association table for many-to-many relationship
user_tags = Table('user_tags', Base.metadata,
                  Column('user_id', Integer, ForeignKey('users.id')),
                  Column('tag_id', Integer, ForeignKey('tags.id')))

class UserORM(Base):
    __tablename__ = 'users'
    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, index=True)
    email = Column(String, unique=True, index=True)
    note = Column(Text)
    tags = relationship('TagORM', secondary=user_tags, back_populates='users')

class TagORM(Base):
    __tablename__ = 'tags'
    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, unique=True, index=True)
    users = relationship('UserORM', secondary=user_tags, back_populates='tags')

class Tag(BaseModel):
    name: str

class User(BaseModel):
    id: int
    name: str
    email: EmailStr
    note: str = ""
    tags: List[Tag] = []

# Create the SQLite database and enable FTS
engine = create_engine('sqlite:///./test.db')
Base.metadata.create_all(bind=engine)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

# Create the FTS table for the note field only
with engine.connect() as conn:
    conn.execute(text('''
        CREATE VIRTUAL TABLE IF NOT EXISTS user_fts USING fts5(
            note,
            content='users',
            content_rowid='id'
        )
    '''))

    # Create triggers to keep the FTS table updated
    conn.execute(text('''
        CREATE TRIGGER IF NOT EXISTS user_fts_insert AFTER INSERT ON users
        BEGIN
            INSERT INTO user_fts(rowid, note) VALUES (new.id, new.note);
        END;
    '''))

    conn.execute(text('''
        CREATE TRIGGER IF NOT EXISTS user_fts_delete AFTER DELETE ON users
        BEGIN
            INSERT INTO user_fts(user_fts, rowid, note) VALUES('delete', old.id, old.note);
        END;
    '''))

    conn.execute(text('''
        CREATE TRIGGER IF NOT EXISTS user_fts_update AFTER UPDATE ON users
        BEGIN
            INSERT INTO user_fts(user_fts, rowid, note) VALUES('delete', old.id, old.note);
            INSERT INTO user_fts(rowid, note) VALUES (new.id, new.note);
        END;
    '''))
