from flask_wtf import FlaskForm 
from wtforms.fields import StringField, PasswordField, SubmitField, FloatField
from wtforms.validators import DataRequired, Length, EqualTo

class RegistrationForm(FlaskForm):
    username = StringField('Username', [DataRequired(), Length(min=6) ])
    password = PasswordField('Password', [DataRequired(), Length(min=6) ])
    confirm_password = PasswordField('Confirm Password', [DataRequired(), EqualTo('password') ])
    register = SubmitField('Register')


class LoginForm(FlaskForm):
    username = StringField('Username', [DataRequired() ])
    password = PasswordField('Password', [DataRequired()])
    login = SubmitField('Login')

class InputForm(FlaskForm):
    Average_Income =  FloatField('Average Income', [DataRequired() ] ,default= 60 ) 
    Ad_Spend_per_Car = FloatField('Ad Spend per Car' , [DataRequired() ], default = 19.80)
    Sales_to_Income_Ratio = FloatField('Sales to Income Ratio' , [DataRequired() ], default = 4.6 )
    send = SubmitField('Send')