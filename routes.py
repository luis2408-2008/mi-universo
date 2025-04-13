import logging
from flask import render_template, redirect, url_for, flash, request, abort
from flask_login import login_user, logout_user, login_required, current_user
from functools import wraps
from sqlalchemy import inspect, text
from app import db
from models import User
from forms import LoginForm, RegistrationForm

logger = logging.getLogger(__name__)

def admin_required(f):
    @wraps(f)
    def decorated_function(*args, **kwargs):
        if not current_user.is_authenticated or not current_user.is_admin:
            abort(403)
        return f(*args, **kwargs)
    return decorated_function

def init_routes(app):
    
    @app.errorhandler(403)
    def forbidden(error):
        return render_template('errors/403.html'), 403
    
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
            
            # Si es el primer usuario, lo convertimos automáticamente en administrador
            if User.query.count() == 0:
                user.is_admin = True
            
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
        
    @app.route('/admin')
    @login_required
    @admin_required
    def admin_panel():
        users = User.query.all()
        return render_template('admin/panel.html', users=users)
    
    @app.route('/admin/create_admin/<username>', methods=['POST'])
    @login_required
    def create_admin(username):
        # Solo permitimos que el primer usuario se convierta en administrador
        # o que un administrador existente cree nuevos administradores
        user_count = User.query.count()
        
        if user_count == 1 or (current_user.is_admin and current_user.username != username):
            user = User.query.filter_by(username=username).first_or_404()
            user.is_admin = True
            db.session.commit()
            flash(f'Usuario {username} ahora es administrador', 'success')
        else:
            flash('No tienes permisos para realizar esta acción', 'error')
            
        return redirect(url_for('admin_panel'))
        
    @app.route('/update_schema')
    def update_schema():
        """Ruta de utilidad para actualizar el esquema de la base de datos."""
        try:
            # Verificar si existe la columna is_admin
            inspector = db.inspect(db.engine)
            columns = [c['name'] for c in inspector.get_columns('user')]
            
            if 'is_admin' not in columns:
                # Añadir la columna is_admin
                db.session.execute(text("ALTER TABLE \"user\" ADD COLUMN is_admin BOOLEAN DEFAULT FALSE"))
                db.session.commit()
                flash('Esquema de base de datos actualizado correctamente.', 'success')
            else:
                flash('El esquema de base de datos ya está actualizado.', 'info')
            
            return redirect(url_for('index'))
        except Exception as e:
            db.session.rollback()
            flash(f'Error al actualizar el esquema: {str(e)}', 'error')
            return redirect(url_for('index'))
