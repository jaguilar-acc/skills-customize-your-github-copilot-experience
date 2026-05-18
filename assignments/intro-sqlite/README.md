# 📘 Assignment: Introduction to SQL and SQLite

## 🎯 Objective

Learn the basics of relational databases by creating and querying a local SQLite database from Python. Students will practice SQL statements, table design, and using the `sqlite3` module.

## 📝 Tasks

### 🛠️ Set Up Database and Seed Data

#### Description

Create a SQLite database file and populate it with sample data using the provided `seed.sql` file.

#### Requirements
Completed program should:

- Use the provided `seed.sql` to create tables and insert sample rows.
- Create a local SQLite database file (e.g., `books.db`).
- Provide a short Python script to initialize the database when run.

### 🛠️ Query Data with SQL

#### Description

Write functions that execute SQL `SELECT` queries to list and filter data.

#### Requirements
Completed program should:

- Implement a `list_books()` function that returns all books.
- Implement a `find_books_by_author(author)` function that finds books by author.
- Demonstrate `WHERE`, `ORDER BY`, and `LIMIT` usage in queries.

### 🛠️ CRUD Operations from Python

#### Description

Add functions to create, update, and delete records using parameterized SQL to avoid injection.

#### Requirements
Completed program should:

- Implement `add_book(title, author, year)` to insert a new book.
- Implement `update_book(book_id, **fields)` to update one or more columns.
- Implement `delete_book(book_id)` to remove a book.
- Use parameterized queries (placeholders) for all write operations.

## 🚀 Getting Started

- Prerequisites: Python 3.8+ (no external packages required).
- Initialize the database and run examples:

```bash
python starter_code.py --init
python starter_code.py --list
python starter_code.py --add "New Book" "Author Name" 2026
```

## 🔎 Files

- `starter_code.py` — starter script with helper functions and a simple CLI.
- `seed.sql` — SQL statements to create tables and insert sample data.

## 📚 Learning Outcomes

Students should be able to:

- Write basic SQL `CREATE`, `INSERT`, `SELECT`, `UPDATE`, and `DELETE` statements.
- Use Python's `sqlite3` module to run queries and manage transactions.
- Understand the basics of database schema design for a simple domain.
