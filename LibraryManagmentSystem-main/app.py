from flask import Flask, render_template, request, redirect, url_for, jsonify

app = Flask(__name__)

# Dummy data with more attributes including an image URL
books = [
    {
        "id": 1,
        "title": "1984",
        "author": "George Orwell",
        "genre": "Dystopian",
        "published": "1949",
        "image": "https://images.pexels.com/photos/5978364/pexels-photo-5978364.jpeg?auto=compress&cs=tinysrgb&dpr=2&h=650&w=940"
    },
    {
        "id": 2,
        "title": "To Kill a Mockingbird",
        "author": "Harper Lee",
        "genre": "Fiction",
        "published": "1960",
        "image": "https://images.pexels.com/photos/5978364/pexels-photo-5978364.jpeg?auto=compress&cs=tinysrgb&dpr=2&h=650&w=940"
    },
    {
        "id": 3,
        "title": "The Great Gatsby",
        "author": "F. Scott Fitzgerald",
        "genre": "Classic",
        "published": "1925",
        "image": "https://images.pexels.com/photos/5978364/pexels-photo-5978364.jpeg?auto=compress&cs=tinysrgb&dpr=2&h=650&w=940"
    },
]

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/books', methods=['GET'])
def get_books():
    return render_template('books.html', books=books)

@app.route('/books/<int:book_id>', methods=['GET'])
def get_book(book_id):
    book = next((book for book in books if book['id'] == book_id), None)
    if book:
        return jsonify(book)
    else:
        return jsonify({"error": "Book not found"}), 404

@app.route('/books', methods=['POST'])
def add_book():
    new_book = request.get_json()
    books.append(new_book)
    return jsonify(new_book), 201

if __name__ == '__main__':
    app.run(debug=True)
