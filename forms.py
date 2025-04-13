from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField
from wtforms.validators import DataRequired, Length, EqualTo, ValidationError
from models import User
from app import db

class LoginForm(FlaskForm):
    username = StringField('Usuario', validators=[DataRequired(message="Por favor ingresa tu nombre de usuario")])
    password = PasswordField('Contraseña', validators=[DataRequired(message="Por favor ingresa tu contraseña")])
    submit = SubmitField('Iniciar Sesión')

class RegistrationForm(FlaskForm):
    username = StringField('Usuario', validators=[
        DataRequired(message="Por favor ingresa un nombre de usuario"),
        Length(min=3, max=64, message="El nombre de usuario debe tener entre 3 y 64 caracteres")
    ])
    password = PasswordField('Contraseña', validators=[
        DataRequired(message="Por favor ingresa una contraseña"),
        Length(min=8, message="La contraseña debe tener al menos 8 caracteres")
    ])
    confirm_password = PasswordField('Confirmar Contraseña', validators=[
        DataRequired(message="Por favor confirma tu contraseña"),
        EqualTo('password', message="Las contraseñas deben coincidir")
    ])
    submit = SubmitField('Registrarse')
    
    def validate_username(self, username):
        user = db.session.query(User).filter_by(username=username.data).first()
        if user is not None:
            raise ValidationError('Este nombre de usuario ya está en uso. Por favor elige otro.')
