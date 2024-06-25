
import argparse
from common import SessionLocal, UserORM

def delete_user(db: SessionLocal, user_id: int):
    user = db.query(UserORM).filter(UserORM.id == user_id).first()
    if user:
        db.delete(user)
        db.commit()
    return user

if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='Delete a user.')
    parser.add_argument('--id', type=int, required=True, help='User ID')
    args = parser.parse_args()

    db = SessionLocal()
    deleted_user = delete_user(db, args.id)
    if deleted_user:
        print(f'User with ID {args.id} deleted.')
    else:
        print(f'User with ID {args.id} not found.')
