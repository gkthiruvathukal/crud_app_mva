import argparse
from common import SessionLocal, UserORM

def get_user(db: SessionLocal, user_id: int):
    return db.query(UserORM).filter(UserORM.id == user_id).first()

if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='Read a user.')
    parser.add_argument('--id', type=int, required=True, help='User ID')
    args = parser.parse_args()

    db = SessionLocal()
    user = get_user(db, args.id)
    if user:
        user_info = {
            'id': user.id,
            'name': user.name,
            'email': user.email,
            'note': user.note,
            'tags': [tag.name for tag in user.tags]
        }
        print(user_info)
    else:
        print(f'User with ID {args.id} not found.')

