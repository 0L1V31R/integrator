from flask import Flask, render_template, url_for

app = Flask(__name__)

@app.route('/')
def index():
    aluno = '/static/images/user-regular.svg'
    senai = '/static/images/senai.png'
    template = {
        'aluno' : aluno,
        'senai': senai,
    }
    return render_template('index.html', **template)

@app.route('/<card>&<temps>')
def index2(card=0, temps=0):
    aluno = '/static/images/user-regular.svg'
    senai = '/static/images/senai.png'
    data = {
        '0': 'Avaster',
        '1': 'Alumnster'
    }
    nome_do_aluno = data[card]
    if(float(temps) <= 37.5):
        tipo = 'normal'
    else:
        tipo = 'nonormal'
    
    template = {
        'cartao': card,
        'temperatura': temps,
        'aluno': aluno,
        'nome': nome_do_aluno,
        'tipo': tipo,
        'senai': senai,
    }
    template['redirect_url'] = url_for('index')
    return render_template('index2.html', **template)

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')