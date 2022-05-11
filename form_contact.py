from flask_wtf import FlaskForm, CSRFProtect
from wtforms import StringField, TextAreaField, SubmitField
from wtforms.validators import DataRequired, Email

csrf = CSRFProtect()

class ContactForm(FlaskForm):
    name = StringField('Name', validators=[DataRequired('Nome não pode ficar vazio')])
    email = StringField('E-mail', validators=[DataRequired('E-mail não pode ficar vazio'),Email('Informe um email válido')])
    # subject = StringField('Assunto', validators=[DataRequired('Assunto não pode ficar vazio')])
    message = TextAreaField('Message', validators=[DataRequired('Mensagem não pode ficar vazio')])
    submit = SubmitField("Send")