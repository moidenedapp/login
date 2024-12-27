from flask import Flask, render_template, request, redirect, url_for, render_template_string
from flask import session
from data.db import DB
from dotenv import load_dotenv

import os
import psycopg2

app = Flask(__name__)
load_dotenv()
app.secret_key = os.environ.get('SECRET_KEY')

base = {
    'dbname': os.environ.get('DB_NAME'),
    'user': os.environ.get('DB_USER'),
    'password': os.environ.get('DB_PASSWORD'),
    'host': os.environ.get('DB_HOST'),
    'port': os.environ.get('DB_PORT')
}

@app.route('/', methods=['GET', 'POST'])
def login():
    error = None
    if request.method == 'POST':
        username = request.form.get('username')
        password = request.form.get('password')
        
        if username and password and is_valid_user(username, password):
            return redirect(url_for('show_data'))
        else:
            error = "El Usuario o Contraseña son Incorrectos."
    
    return render_template_string("""
    {% if error %}
        <p style="color: red;">{{ error }}</p>
    {% endif %}
    <form method="post">
        Usuario: <input type="text" name="username" /><br>
        Contraseña: <input type="password" name="password" /><br>
        <button type="submit">ENTRAR</button>
    </form>
    """, error=error)

def is_valid_user(username :str, password :str) -> bool:
    try:

        db = DB(base)
        user = db.connect().get_user_by_email(username)
        if not user:
            return False
        
        if not user.login(password):
            return False
        
        session['user_id'] = user.id
        return True
    
    except Exception as e:
        print(f"Error al verificar usuario: {e}")
        return False

@app.route('/datos')
def show_data():
    try:
        connection = psycopg2.connect(**base)
        cursor = connection.cursor()

        if not session.get('user_id'):
            return redirect(url_for('login'))

        query = """
        SELECT 
            a.id, a.name, a.lastname, b."name", d."name", 
            c.can_read, c.can_write, c.can_update, c.can_delete
        FROM 
            users a
        JOIN roles b ON a.role_id = b.id
        JOIN permissions c ON c.role_id = b.id
        JOIN modules d ON c.module_id = d.id WHERE a.id = %s
        """
        
        cursor.execute(query, (session['user_id'],))
        records = cursor.fetchall()
         
        cursor.close()
        connection.close()
        return render_template('table.html', records=records)
        
    except Exception as e:
        return f"Error: {e}"

if __name__ == '__main__':
    app.run(debug=True)