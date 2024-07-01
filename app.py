

from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('base.html', title="Krishna's Resume Builder", page='home')

@app.route('/about')
def about():
    return render_template('base.html', title="About Krishna", page='about')

@app.route('/skills')
def skills():
    return render_template('base.html', title="Krishna's Skills", page='skills')

@app.route('/projects')
def projects():
    return render_template('base.html', title="Krishna's Projects", page='projects')

@app.route('/contact')
def contact():
    return render_template('base.html', title="Contact Krishna", page='contact')

if __name__ == '__main__':
    app.run(debug=True)

