from flask import Flask, jsonify, request, render_template

app = Flask(__name__)

livros = [
    {
        'id': 1,
        'title': 'The Lord Of The Rings - The Society Of The Ring',
        'author': 'J.R.R. Tolkien'
    },
    {
        'id': 2,
        'title': 'Harry Potter and the Philosopher`s Stone',
        'author': 'J.K. Rowling'
    },
    {
        'id': 3,
        'title': 'Clean Code',
        'author': 'Robert C. Martin'
    }
]


@app.route('/')
def index():
    return '/livros extension'


@app.route('/livros', methods=['GET'])
def get_books_all():
    return jsonify(livros)


@app.route('/livros/<int:id>', methods=['GET'])
def get_book_by_id(id):
    for livro in livros:
        if livro.get('id') == id:
            return jsonify(livro)


@app.route('/livros/<int:id>', methods=['PUT'])
def edit_book_by_id(id):
    edited_book = request.get_json()
    for index, livro in enumerate(livros):
        if livro.get('id') == id:
            livros[index].update(edited_book)
            return jsonify(livros[index])


@app.route('/livros/', methods=['POST'])
def add_new_book():
    new_book = request.get_json()
    livros.append(new_book)

    return jsonify(new_book)


@app.route('/livros/<int:id>', methods=['DELETE'])
def delete_book(id):
    for index, livro in enumerate(livros):
        if livro.get('id') == id:
            del livros[index]

    return jsonify(livros)


app.run(port=5000, host='localhost', debug='True')
