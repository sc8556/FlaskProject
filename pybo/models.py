from pybo import db

class Question(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    subject = db.Column(db.String(200), nullable=False)
    content = db.Column(db.Text(), nullable=False)
    create_date = db.Column(db.DateTime(), nullable=False)

class Answer(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    question_id = db.Column(db.Integer, db.ForeignKey('question.id', ondelete='CASCADE'))
    question = db.relationship('Question', backref=db.backref('answer_set'))
    content = db.Column(db.Text(), nullable=False)
    create_date = db.Column(db.DateTime(), nullable=False)

class Department(db.Model):
    dept_code = db.Column(db.String(10), primary_key=True)
    dept_name = db.Column(db.String(50), nullable=False)
    location = db.Column(db.String(100))
    create_date = db.Column(db.DateTime(), nullable=False)

class Employee(db.Model):
    emp_id = db.Column(db.Integer, primary_key=True)
    emp_name = db.Column(db.String(50), nullable=False)
    dept_code = db.Column(db.String(10), db.ForeignKey('department.dept_code', ondelete='CASCADE'))
    department = db.relationship('Department', backref=db.backref('emp_set'))
    email = db.Column(db.String(100), unique=True, nullable=False)
    hire_date = db.Column(db.DateTime(), nullable=False)
    position = db.Column(db.String(50))
    salary = db.Column(db.Float)

