from flask_wtf import FlaskForm #pip install flask-wtf
from wtforms import StringField, FloatField, DateField, SelectField, SubmitField
from wtforms.validators import DataRequired, Email, Length, Optional


class DepartmentForm(FlaskForm):
    dept_code = StringField('부서 코드', validators=[DataRequired(), Length(min=2, max=10)])
    dept_name = StringField('부서명', validators=[DataRequired(), Length(max=50)])
    location = StringField('위치', validators=[Length(max=100)])
    submit = SubmitField('등록')


class EmployeeForm(FlaskForm):
    emp_name = StringField('사원명', validators=[DataRequired(), Length(max=50)])
    email = StringField('이메일', validators=[DataRequired(), Email(), Length(max=100)])
    hire_date = DateField('입사일', format='%Y-%m-%d')
    position = StringField('직급', validators=[Length(max=50)])
    salary = FloatField('급여', validators=[Optional()])
    dept_code = SelectField('부서', validators=[DataRequired()], coerce=str)
    submit = SubmitField('등록')