import argparse
from common import SessionLocal, UserORM, TagORM, User, Tag

def update_user(db: SessionLocal, user_id: int, name: str = None, email: str = None, note: str = None, tags: list = None):
    user = db.query(UserORM).filter(UserORM.id == user_id).first()
    if user:
        if name is not None:
            user.name = name
        if email is not None:
            user.email = email
        if note is not None:
            user.note = note
        if tags is not None:
            user.tags.clear()
            for tag in tags:
                db_tag = db.query(TagORM).filter(TagORM.name == tag.name).first()
                if not db_tag:
                    db_tag = TagORM(name=tag.name)
                    db.add(db_tag)
                    db.commit()
                    db.refresh(db_tag)
                user.tags.append(db_tag)
        db.commit()
        db.refresh(user)
    return user

if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='Update a user.')
    parser.add_argument('--id', type=int, required=True, help='User ID')
    parser.add_argument('--name', type=str, help='User name')
    parser.add_argument('--email', type=str, help='User email')
    parser.add_argument('--note', type=str, help='User note')
    parser.add_argument('--tags', nargs='+', help='User tags')
    args = parser.parse_args()

    tags = [Tag(name=tag) for tag in args.tags] if args.tags else None  # Correctly instantiate Tag objects if provided
    db = SessionLocal()
    updated_user = update_user(db, args.id, args.name, args.email, args.note, tags)
    if updated_user:
        print({
            'id': updated_user.id,
            'name': updated_user.name,
            'email': updated_user.email,
            'note': updated_user.note,
            'tags': [tag.name for tag in updated_user.tags]
        })
    else:
        print(f'User with ID {args.id} not found.')

