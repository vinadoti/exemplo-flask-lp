from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)

URL = 'https://5000-cyan-marlin-ll559fu0.ws-us18.gitpod.io/'

livros = [
    {"id": 1, "titulo": "Estudar para a prova", "autor": "Machado de Assis", "categoria": "drama", "concluida": False},
    {"id": 2, "titulo": "Passear com o cachorro","autor": "Machado de Assis", "categoria": "drama","concluida": True},
    {"id": 3, "titulo": "Estudar mais para a prova","autor": "Machado de Assis", "categoria": "drama","concluida": False},
]

@app.route('/')
def index():
    return render_template('index.html', lista=livros)

@app.route('/create')
def create():
    return render_template('create.html')

@app.route('/save', methods=['POST'])  # <form action="/save" method="POST">
def save():
    titulo = request.form['titulo']      # Entrada do título
    autor = request.form['autor']  # Entrada do autor
    categoria = request.form['categoria'] # Entrada da categoria
    livro = { "titulo": titulo, "autor": autor, "categoria": categoria, "concluida": False }
    livros.append(livro)

    # Atribuindo o id            - Tentar fazer dinamico !!!
    #ultimo= livros[-1]

    return redirect(URL)

@app.route('/delete/<id>')  
def delete():
    del livros
    return redirect(URL)

app.run(debug=True)


# Implementar o DELETE!! (2,0 pontos)
# Implementar uma pesquisa (3,0 pontos)