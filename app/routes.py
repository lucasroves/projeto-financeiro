from flask import render_template, request, redirect, url_for
from app import app, db
from app.models import User, Transaction

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/register', methods=['GET', 'POST'])
def register():
    # Lógica para registro de usuário
    return render_template('register.html')

@app.route('/login', methods=['GET', 'POST'])
def login():
    # Lógica para login de usuário
    return render_template('login.html')

@app.route('/profile')
def profile():
    # Lógica para visualização de perfil e saldo do usuário
    return render_template('profile.html')

@app.route('/transactions')
def transactions():
    # Lógica para visualização do histórico de transações do usuário
    return render_template('transactions.html')