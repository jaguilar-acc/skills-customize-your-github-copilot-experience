# 📘 Assignment: Building REST APIs with FastAPI

## 🎯 Objective

Build a small REST API using the FastAPI framework to learn request handling, validation with Pydantic, and running a development server.

## 📝 Tasks

### 🛠️ Create a Basic API

#### Description

Implement a minimal FastAPI application that exposes endpoints to list and retrieve items.

#### Requirements
Completed program should:

- Provide a root `GET /` endpoint that returns a welcome message.
- Provide a `GET /items/{item_id}` endpoint that returns an item by ID.
- Use clear JSON responses and appropriate HTTP status codes.

### 🛠️ Add Create and Validation

#### Description

Add an endpoint to create new items using a Pydantic model and validate incoming data.

#### Requirements
Completed program should:

- Implement a `POST /items/` endpoint that accepts an item payload and returns the created item with status `201`.
- Validate request data using a Pydantic `BaseModel`.
- Return `400` for invalid or duplicate data as appropriate.

## 🚀 Getting Started

- Prerequisites: Python 3.8+ and `pip`.
- Install dependencies:

```
pip install -r requirements.txt
```

- Run the development server:

```
uvicorn starter_code:app --reload
```

## 🔎 Example Requests

- List root:

```
GET http://127.0.0.1:8000/
```

- Create an item (JSON body):

```
POST http://127.0.0.1:8000/items/
Content-Type: application/json

{
  "id": 1,
  "name": "Sample",
  "description": "A sample item",
  "price": 9.99
}
```

- Retrieve an item:

```
GET http://127.0.0.1:8000/items/1
```
