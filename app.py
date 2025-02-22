from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('home.html')

@app.route('/menu')
def menu():
    return render_template('menu.html')

@app.route('/galeri')
def galeri():
    return render_template('galeri.html')

@app.route('/kontak')
def kontak():
    return render_template('kontak.html')

@app.route('/order')
def order():
    return render_template('order.html')

if __name__ == '__main__':  
    app.run('0.0.0.0', port=5000,debug=True)