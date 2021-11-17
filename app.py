from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)

#Sempre que acessar pela primeira vez o código, trocar a URL do index aqui:
URL= 'https://5000-aquamarine-kiwi-44oo1n1g.ws-us18.gitpod.io'

livros = [
    {"id": 1, "titulo": "Orgulho e Preconceito", "autor": "Jane Austen", "categoria": "Romance", "concluida": False},
    {"id": 2, "titulo": "1984","autor": "George Orwell", "categoria": "Suspense","concluida": True},
    {"id": 3, "titulo": "Dom Quixote de la Mancha","autor": "Miguel de Cervantes", "categoria": "Drama","concluida": False},
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

    #Definindo o id 
    if livros:
        identificacao = livros[-1]
    else:
        identificacao = {"id": 0}   


    #Moldando Lista e definindo dados
    #OBS: Ao definir o 'id' do registro, utilizamos o ultimo elemento da lista somando o valor de seu id + 1
    livro = {"id": identificacao["id"] + 1, "titulo": titulo, "autor": autor, "categoria": categoria, "concluida": False }
    
    #Adicionando a lista
    livros.append(livro)

    #Redirecionando para a página principal
    return redirect(URL + '/')

@app.route('/delete/<id>')
def delete(id):
    for indice, livro in enumerate(livros):
        if livro["id"] == int(id):
            del livros[indice]

    return redirect(URL + '/')

app.run(debug=True)

@app.route('/update/<id>')


# Implementar o DELETE!! (2,0 pontos)
# Implementar uma pesquisa (3,0 pontos)