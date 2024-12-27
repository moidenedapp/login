from flask import Flask, render_template, request, redirect, url_for, render_template_string
from flask import session
from data import Users, Roles, Permissions, Modules

import os
import psycopg2

app = Flask(__name__)
app.secret_key = os.environ.get('SECRET_KEY')


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
    
    return render_template('login.html', error=error)

def is_valid_user(username :str, password :str) -> bool:
    try:

        user = Users().find(email=username)
        if not user:
            return False
        
        if user.password != password:
            return False
        
        session['user_id'] = user.id
        return True
    
    except Exception as e:
        print(f"Error al verificar usuario: {e}")
        return False

@app.route('/datos')
def show_data():
    try:
        if not session.get('user_id'):
            return redirect(url_for('login'))        
        user = Users().find(id=session.get('user_id'))
        return render_template('welcome.html', user=user)
        
    except Exception as e:
        return f"Error: {e}"
    

@app.route('/modules')
def show_modules():
    try:
        if not session.get('user_id'):
            return redirect(url_for('login'))        
        user = Users().find(id=session.get('user_id'))
        modules = Modules().all()

        return render_template('modules.html', user=user, modules=modules)
        
    except Exception as e:
        return f"Error: {e}"


@app.route('/modules/create')
def create_modules():
    try:
        if not session.get('user_id'):
            return redirect(url_for('login'))        
        
        return render_template('modules_form.html', id=0)
        
    except Exception as e:
        return f"Error: {e}"
    


@app.route('/modules/edit/<int:id>')
def edit_modules(id: int):
    try:
        if not session.get('user_id'):
            return redirect(url_for('login'))        
        
        module = Modules().find(id=id)
        return render_template('modules_form.html', id=id, module=module)
        
    except Exception as e:
        return f"Error: {e}"
    


@app.route('/modules/save',  methods=['POST'])
def save_modules():
    try:
        if not session.get('user_id'):
            return redirect(url_for('login'))  

        id = int(request.form.get('id'))
        name = request.form.get('name') 
        if name is None or name == '':
            return render_template('modules_form.html', id=id, error="El nombre del módulo es requerido.")

        if id == 0:
            module = Modules(name=name)
        else:
            module = Modules().find(id=id)
            module.name = name

        module.save()
        return redirect(url_for('show_modules'))
        
    except Exception as e:
        return f"Error: {e}"
    

@app.route('/modules/delete/<int:id>',  methods=['GEt'])
def delete_modules(id: int):
    try:
        if not session.get('user_id'):
            return redirect(url_for('login'))  

        module = Modules().find(id=id)
        if module:
            module.delete()
        return redirect(url_for('show_modules'))
        
    except Exception as e:
        return f"Error: {e}"
    


if __name__ == '__main__':
    app.run(debug=True)