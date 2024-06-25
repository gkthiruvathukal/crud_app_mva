
import argparse
from sqlalchemy.orm import Session
from common import User, Tag, UserORM, TagORM, SessionLocal

def create_user(db: Session, user: User):
    db_user = UserORM(id=user.id, name=user.name, email=user.email, note=user.note)
    db.add(db_user)
    db.commit()
    db.refresh(db_user)
    for tag in user.tags:
        db_tag = db.query(TagORM).filter(TagORM.name == tag.name).first()
        if not db_tag:
            db_tag = TagORM(name=tag.name)
            db.add(db_tag)
            db.commit()
            db.refresh(db_tag)
        db_user.tags.append(db_tag)
    db.commit()
    db.refresh(db_user)
    return db_user

if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='Create a new user.')
    parser.add_argument('--id', type=int, required=True, help='User ID')
    parser.add_argument('--name', type=str, required=True, help='User name')
    parser.add_argument('--email', type=str, required=True, help='User email')
    parser.add_argument('--note', type=str, help='User note', default="")
    parser.add_argument('--tags', nargs='+', required=True, help='User tags (at least one)')
    args = parser.parse_args()

    tags = [Tag(name=tag) for tag in args.tags]  # Correctly instantiate Tag objects
    user = User(id=args.id, name=args.name, email=args.email, note=args.note, tags=tags)

    db = SessionLocal()
    created_user = create_user(db, user)
    print(created_user)
