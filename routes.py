import logging
from flask import render_template, redirect, url_for, flash, request
from flask_login import login_user, logout_user, login_required, current_user
from app import db
from models import User
from forms import LoginForm, RegistrationForm

logger = logging.getLogger(__name__)

def init_routes(app):
    
    @app.route('/')
    def index():
        if current_user.is_authenticated:
            return redirect(url_for('dashboard'))
        return render_template('index.html')
    
    @app.route('/login', methods=['GET', 'POST'])
    def login():
        if current_user.is_authenticated:
            return redirect(url_for('dashboard'))
        
        form = LoginForm()
        if form.validate_on_submit():
            user = db.session.query(User).filter_by(username=form.username.data).first()
            
            if user is None or not user.check_password(form.password.data):
                flash('Usuario o contraseña incorrectos', 'error')
                return redirect(url_for('login'))
            
            login_user(user)
            next_page = request.args.get('next')
            if not next_page or next_page.startswith('/'):
                next_page = url_for('dashboard')
            return redirect(next_page)
        
        return render_template('login.html', form=form)
    
    @app.route('/register', methods=['GET', 'POST'])
    def register():
        if current_user.is_authenticated:
            return redirect(url_for('dashboard'))
        
        form = RegistrationForm()
        if form.validate_on_submit():
            user = User(username=form.username.data)
            user.set_password(form.password.data)
            
            try:
                db.session.add(user)
                db.session.commit()
                flash('¡Registro exitoso! Ahora puedes iniciar sesión.', 'success')
                return redirect(url_for('login'))
            except Exception as e:
                db.session.rollback()
                logger.error(f"Error during registration: {str(e)}")
                flash('Ocurrió un error durante el registro. Por favor intenta de nuevo.', 'error')
        
        return render_template('register.html', form=form)
    
    @app.route('/logout')
    @login_required
    def logout():
        logout_user()
        flash('Has cerrado sesión correctamente', 'info')
        return redirect(url_for('index'))
    
    @app.route('/dashboard')
    @login_required
    def dashboard():
        return render_template('dashboard.html')
    
    @app.route('/bigbang')
    @login_required
    def bigbang():
        return render_template('sections/bigbang.html')
    
    @app.route('/teorias')
    @login_required
    def teorias():
        return render_template('sections/teorias.html')
    
    @app.route('/conspiraciones')
    @login_required
    def conspiraciones():
        return render_template('sections/conspiraciones.html')
