from flask import *
import sqlite3

app = Flask(__name__)

app.config['SECRET_KEY'] = '1q2e3e4r'

def getCon():
    conn = sqlite3.connect("database.db")
    conn.row_factory = sqlite3.Row
    return conn


@app.route('/')
def index():
    login = session.get('login')
    return render_template('index.html', login=login)

@app.route('/login', methods = ['GET', 'POST'])
def login():
    if request.method == 'POST':
        login = request.form['login']
        password = request.form['password']
        conn = getCon()
        user = conn.execute('SELECT * FROM users WHERE login = ? AND password = ?', (login, password))
        if user:
            session['login'] = user['login']
            return redirect(url_for('index'))
        else:
            flash("Не коректний пароль або логін")
            return redirect(url_for('login'))
    
    return render_template('login_html')

@app.route('/logout')
def logout():
    session.pop('login', None)
    return redirect(url_for('index'))

@app.route('/signup', methods = ['GET', 'POST'])
def signup():
    login = request.form['login']
    password = request.form['password']
    confirm_password = request.form('confirm_password')
    if password != confirm_password:
        flash("Паролі не співпадають")
        return redirect(url_for('signup'))
    conn = getCon()
    user = conn.execute('SELECT * FROM users WHERE login = ?', (login,)).fetchone()
    if user:
        flash('Логін зайнятий!')
        conn.close()
        return redirect(url_for('signup'))
    


if __name__ == '__main__':
    app.run()