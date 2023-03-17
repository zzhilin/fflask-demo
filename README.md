## Description

- This is a backend server for the ArXiv bug report function
- Run with the frontend

## Steps

### Create virtual environment (below are based on mac)

if you want to use virtualenv:
`python3 -m venv venv`
activate env
`source venv/bin/activate`

### Install Dependencies

`pip install Flask, requests, Flask-SQLAlchemy, flask-cors`

### Create database

- run a python interactive shell
  `from app import db`
  `db.create_all()`
  `exit()`

### Start Server

1. Start frontend server
2. Start server
   `python app.py`
