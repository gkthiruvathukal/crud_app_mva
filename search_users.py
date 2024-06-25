
import argparse
from common import SessionLocal
from sqlalchemy.sql import text

def search_users_by_note(db: SessionLocal, query: str):
    return db.execute(text('''
        SELECT users.* FROM user_fts
        JOIN users ON user_fts.rowid = users.id
        WHERE user_fts.note MATCH :query
    '''), {'query': query}).fetchall()

if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='Search users by note.')
    parser.add_argument('--query', type=str, required=True, help='Search query')
    args = parser.parse_args()

    db = SessionLocal()
    users = search_users_by_note(db, args.query)
    for user in users:
        print(user)
