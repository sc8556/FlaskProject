from flask import Blueprint, render_template, redirect, url_for, flash, request
from pybo.models import Department,Employee
from ..forms import DepartmentForm, EmployeeForm
from pybo import db
from datetime import datetime


bp = Blueprint('emp', __name__, url_prefix='/emp')


# 홈 페이지
@bp.route('/')
def index_emp():
    return render_template('index.html')

# 부서 관련 라우트
@bp.route('/department')
def list_department():
    departments = Department.query.all()
    return render_template('department/list.html', departments=departments)

@bp.route('/department/create', methods=['GET', 'POST'])
def create_department():
    form = DepartmentForm()
    if form.validate_on_submit():
        department = Department(
            dept_code=form.dept_code.data,
            dept_name=form.dept_name.data,
            location=form.location.data,
            create_date=datetime.now()
        )
        db.session.add(department)
        db.session.commit()
        flash('부서가 성공적으로 등록되었습니다.')
        return redirect(url_for('emp.list_department'))
    return render_template('department/create.html', form=form)

@bp.route('/department/<dept_code>')
def view_department(dept_code):
    departments = Department.query.get_or_404(dept_code)
    employees = Employee.query.filter(Employee.dept_code == dept_code).all()
    #department = db.relationship('Department', backref=db.backref('emp_set'))
    return render_template('department/detail.html', department=departments, employees=employees)

# 사원 관련 라우트
@bp.route('/employee')
def list_employee():
    employees = Employee.query.all()
    return render_template('employee/list.html', employees=employees)

@bp.route('/employee/create', methods=['GET', 'POST'])
def create_employee():
    form = EmployeeForm()
    form.dept_code.choices = [(d.dept_code, d.dept_name) for d in Department.query.all()]  # 초이스를 이용해서 부서
    if form.validate_on_submit():
        employee = Employee(
            emp_name=form.emp_name.data,
            email=form.email.data,
            hire_date=form.hire_date.data,
            position=form.position.data,
            salary=form.salary.data,
            dept_code=form.dept_code.data
        )
        db.session.add(employee)
        db.session.commit()
        flash('사원이 성공적으로 등록되었습니다.')
        return redirect(url_for('emp.list_employee'))
    return render_template('employee/create.html', form=form)

@bp.route('/employee/<int:emp_id>')
def view_employee(emp_id):
    employee = Employee.query.get_or_404(emp_id)
    return render_template('employee/detail.html', employee=employee)