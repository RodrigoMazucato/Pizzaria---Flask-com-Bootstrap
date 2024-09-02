from flask import Flask, render_template, request, redirect

class Pizzaria:
    lista = []
    def __init__(self, sabor, ingredientes, preco, filename):
        self.sabor = sabor
        self.ingredientes = ingredientes
        self.preco = preco
        self.filename = filename
        Pizzaria.lista.append(self)

app = Flask(__name__)

@app.get('/')
def exibir_projeto():
    return render_template('formulario.html')

@app.post('/cadastrar')
def cadastrar_pizza():
    sabor = request.form.get('sabor')
    ingredientes = request.form.get('ingredientes')
    preco = request.form.get('preco')
    file = request.files.get('file')
    if file:
        file.save(f'static/images/upload/{file.filename}')
    else:
        return "Nenhum arquivo selecionado", 400
    Pizzaria(sabor, ingredientes, preco, file.filename)
    return redirect('/exibir')

@app.get('/exibir')
def listar_pizzas():
    return render_template('exibir-pizzas.html', pizzas=Pizzaria.lista)
    

if __name__ == '__main__':
    app.run(debug=True)