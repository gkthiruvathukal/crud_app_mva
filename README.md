# CRUD Application with Pydantic, SQLAlchemy, and SQLite

This project demonstrates a simple CRUD (Create, Read, Update, Delete) application using Pydantic for data validation, SQLAlchemy for ORM (Object Relational Mapping), and SQLite for the database. The project is designed to illustrate how to separate concerns between data validation, ORM, and business logic.

Through a set of clever prompts, we have been able to generate this MVA as a first step toward re-creating one of our flagship programs for document storage and retrieval.

## Project Structure

- `common.py`: Contains the Pydantic models, SQLAlchemy ORM models, and database setup code.
- `create_user.py`: Script to create a new user in the database.
- `read_user.py`: Script to read user details from the database.
- `update_user.py`: Script to update user information in the database.
- `delete_user.py`: Script to delete a user from the database.
- `search_note.py`: Script to search users by their note using Full-Text Search (FTS).

## Requirements

- Python 3.7+
- SQLAlchemy
- Pydantic
- email-validator

## Setup

1. Create a virtual environment:
    ```bash
    python -m venv venv
    ```

2. Activate the virtual environment:
    - On Windows:
        ```bash
        venv\\Scripts\\activate
        ```
    - On macOS/Linux:
        ```bash
        source venv/bin/activate
        ```

3. Install the required packages:
    ```bash
    pip install sqlalchemy pydantic email-validator
    ```

4. Run the `common.py` script to set up the database:
    ```bash
    python common.py
    ```

## Usage

### Create a User

```bash
python create_user.py --id 1 --name "John Doe" --email "john.doe@example.com" --note "Sample note" --tags "tag1" "tag2"
```
### Read a User


```bash
python read_user.py --id 1
```

```bash
python update_user.py --id 1 --name "Jane Doe" --email "jane.doe@example.com" --note "Updated note" --tags "tag1" "tag3"
```

```bash
python delete_user.py --id 1
```


```bash
python search_note.py --query "sample"
```


## Explanation of various commands

- `common.py` - This script defines the data models using Pydantic and SQLAlchemy. It also sets up the SQLite database with Full-Text Search (FTS) enabled on the note field.

- `create_user.py` - This script creates a new user in the database. You need to provide the user ID, name, email, note, and at least one tag.

- `read_user.py` - This script reads the user details from the database based on the user ID provided.

- `update_user.py` - This script updates the user information in the database. You need to provide the user ID and any other field that you want to update.

- `delete_user.py` - This script deletes a user from the database based on the user ID provided.

- `search_note.py` - This script searches users by their note using Full-Text Search (FTS). You need to provide the search query.

