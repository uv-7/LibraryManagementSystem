import pytest
from app import app

@pytest.fixture
def client():
    with app.test_client() as client:
        yield client

def test_home(client):
    """Test the home page."""
    rv = client.get('/')
    assert rv.status_code == 200
    assert b'Welcome to the Library Management System!' in rv.data

def test_get_books(client):
    """Test getting the list of books."""
    rv = client.get('/books')
    assert rv.status_code == 200
    assert b'1984' in rv.data
    assert b'To Kill a Mockingbird' in rv.data

def test_get_book(client):
    """Test getting a single book by id."""
    rv = client.get('/books/1')
    assert rv.status_code == 200
    assert b'1984' in rv.data

    rv = client.get('/books/100')
    assert rv.status_code == 404
    assert b'Book not found' in rv.data

def test_add_book(client):
    """Test adding a new book."""
    new_book = {"id": 4, "title": "Brave New World", "author": "Aldous Huxley", "genre": "Dystopian", "published": "1932"}
    rv = client.post('/books', json=new_book)
    assert rv.status_code == 201
    assert b'Brave New World' in rv.data

    # Verify the book was added
    rv = client.get('/books/4')
    assert rv.status_code == 200
    assert b'Brave New World' in rv.data
