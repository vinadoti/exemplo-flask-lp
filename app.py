from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)

#Sempre que acessar pela primeira vez o código, trocar a URL do index aqui:
URL= 'https://5000-amaranth-crab-y4qk3gr1.ws-us17.gitpod.io'

lista_livros = [
    {"id": 1, "titulo": "Orgulho e Preconceito", "autor": "Jane Austen", "categoria": "Romance", "concluida": False},
    {"id": 2, "titulo": "1984","autor": "George Orwell", "categoria": "Suspense","concluida": True},
    {"id": 3, "titulo": "Dom Quixote de la Mancha","autor": "Miguel de Cervantes", "categoria": "Drama","concluida": False},
]

# Implementando o index ---------------------------------------------------------------------------------------------------
@app.route('/')
def index():
    return render_template('index.html', lista=lista_livros)

# Implementando o create ---------------------------------------------------------------------------------------------------
@app.route('/create')
def create():
    return render_template('create.html')

# Implementando o save ---------------------------------------------------------------------------------------------------
@app.route('/save', methods=['POST'])  # <form action="/save" method="POST">
def save():
    titulo = request.form['titulo']      # Entrada do título
    autor = request.form['autor']  # Entrada do autor
    categoria = request.form['categoria'] # Entrada da categoria

    # Definindo o 'id' dos livros //  
    if lista_livros:  #Verificando se possui itens na lista
        identificacao = lista_livros[-1]
    else:  #Caso não possua, atribuindo o valor 0 ao 'id'
        identificacao = {"id": 0}   

    #Criando a lista e definindo seus dados  // Após definir o 'id', utilizamos o 'identificação' somando + 1
    livro = {"id": identificacao["id"] + 1, "titulo": titulo, "autor": autor, "categoria": categoria, "concluida": False }
    
    #Adicionando o livro a lista
    lista_livros.append(livro)

    #Redirecionando para a página principal
    return redirect(URL + '/')

# Implementando o delete ---------------------------------------------------------------------------------------------------
@app.route('/delete/<id>')
def delete(id):
    for indice, livro in enumerate(lista_livros):
        if livro["id"] == int(id):
            del lista_livros[indice]

    return redirect(URL + '/')

# Implementando o search ---------------------------------------------------------------------------------------------------
@app.route('/search', methods=['POST'])  # <form action="/search" method="POST">
def search():
    busca_lista = [] # Criando nova lista para o resultado da pesquisa
    buscar = request.form['busca'] # Entrada do título
    if buscar > '':
        for livro in lista_livros: 
            if buscar.lower() in livro['titulo'].lower()  or buscar.lower() in livro['autor'].lower() or buscar.lower() in livro['categoria'].lower():   # Realiza a busca com o título, autor e categoria dos livros presentes na lista de livros
                busca_lista.append(livro)  # Criando nova lista com os resultados das buscas
        return render_template('search.html', busca_lista=busca_lista)

    return render_template('error.html') # Retornando página de erro

# Implementando a tela de alteração  ---------------------------------------------------------------------------------------------------
@app.route('/edit/<id>')   
def edit(id):
    for indice, livro in enumerate(lista_livros):
        if livro["id"] == int(id):
            return render_template('update.html', livro=livro)

    return render_template('error.html') # Retornando página de erro
    
# Implementando o update  ---------------------------------------------------------------------------------------------------
@app.route('/update/<id>', methods=['POST'])  # <form action="/update" method="POST">
def update(id):
    
    titulo = request.form['titulo']      # Entrada do título
    autor = request.form['autor']  # Entrada do autor
    categoria = request.form['categoria'] # Entrada da categoria

    #Percorrer a lista, verificar o 'id' e alterar os elementos
    for indice, livro in enumerate(lista_livros):
        if livro["id"] == int(id):
            livro["titulo"] = titulo
            livro["autor"] = autor
            livro["categoria"] = categoria
    
    #Redirecionando para a página principal
    return redirect(URL + '/' )

app.run(debug=True)