import sqlite3
import argparse
from typing import List, Tuple, Optional

DB_FILE = "books.db"
SEED_FILE = "seed.sql"

def init_db(db_file: str = DB_FILE, seed_file: str = SEED_FILE):
    conn = sqlite3.connect(db_file)
    with open(seed_file, "r", encoding="utf-8") as f:
        sql = f.read()
    conn.executescript(sql)
    conn.commit()
    conn.close()
    print(f"Initialized database {db_file} from {seed_file}")

def get_connection(db_file: str = DB_FILE):
    return sqlite3.connect(db_file)

def list_books(db_file: str = DB_FILE) -> List[Tuple]:
    conn = get_connection(db_file)
    cur = conn.cursor()
    cur.execute("SELECT id, title, author, year FROM books ORDER BY id")
    rows = cur.fetchall()
    conn.close()
    return rows

def find_books_by_author(author: str, db_file: str = DB_FILE) -> List[Tuple]:
    conn = get_connection(db_file)
    cur = conn.cursor()
    cur.execute("SELECT id, title, author, year FROM books WHERE author = ?", (author,))
    rows = cur.fetchall()
    conn.close()
    return rows

def add_book(title: str, author: str, year: int, db_file: str = DB_FILE) -> int:
    conn = get_connection(db_file)
    cur = conn.cursor()
    cur.execute("INSERT INTO books (title, author, year) VALUES (?, ?, ?)", (title, author, year))
    conn.commit()
    book_id = cur.lastrowid
    conn.close()
    return book_id

def update_book(book_id: int, title: Optional[str] = None, author: Optional[str] = None, year: Optional[int] = None, db_file: str = DB_FILE) -> None:
    conn = get_connection(db_file)
    cur = conn.cursor()
    fields = []
    params = []
    if title is not None:
        fields.append("title = ?")
        params.append(title)
    if author is not None:
        fields.append("author = ?")
        params.append(author)
    if year is not None:
        fields.append("year = ?")
        params.append(year)
    if not fields:
        conn.close()
        return
    params.append(book_id)
    sql = f"UPDATE books SET {', '.join(fields)} WHERE id = ?"
    cur.execute(sql, params)
    conn.commit()
    conn.close()

def delete_book(book_id: int, db_file: str = DB_FILE) -> None:
    conn = get_connection(db_file)
    cur = conn.cursor()
    cur.execute("DELETE FROM books WHERE id = ?", (book_id,))
    conn.commit()
    conn.close()

def main():
    parser = argparse.ArgumentParser(description="Starter script for SQLite assignment")
    parser.add_argument("--init", action="store_true", help="Initialize the database from seed.sql")
    parser.add_argument("--list", action="store_true", help="List all books")
    parser.add_argument("--find-author", metavar="AUTHOR", help="Find books by author")
    parser.add_argument("--add", nargs=3, metavar=("TITLE", "AUTHOR", "YEAR"), help="Add a new book")
    parser.add_argument("--update", nargs=4, metavar=("ID", "TITLE", "AUTHOR", "YEAR"), help="Update a book")
    parser.add_argument("--delete", metavar="ID", help="Delete a book by ID")
    args = parser.parse_args()

    if args.init:
        init_db()
    elif args.list:
        rows = list_books()
        for r in rows:
            print(r)
    elif args.find_author:
        rows = find_books_by_author(args.find_author)
        for r in rows:
            print(r)
    elif args.add:
        title, author, year = args.add
        book_id = add_book(title, author, int(year))
        print(f"Added book with id={book_id}")
    elif args.update:
        book_id, title, author, year = args.update
        update_book(int(book_id), title=title, author=author, year=int(year))
        print("Updated book")
    elif args.delete:
        delete_book(int(args.delete))
        print("Deleted book")
    else:
        parser.print_help()

if __name__ == "__main__":
    main()
