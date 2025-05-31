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
        existing_department = Department.query.filter_by(dept_code=form.dept_code.data).first()
        if existing_department:
            flash('이미 존재하는 부서 코드입니다. 다른 코드를 사용해주세요.', 'danger')
            return render_template('department/create.html', form=form)

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
    page = request.args.get('page', type=int, default=1)
    departments = Department.query.get_or_404(dept_code)
    # ▼ all() 때문에 list 객체로 반환되어 paginate 사용 불가
    # employees = Employee.query.filter(Employee.dept_code == dept_code).all()
    employees = Employee.query.order_by(Employee.hire_date.desc())  # paginate 사용하기 위해 변경
    employees = employees.paginate(page=page, per_page=10)
    return render_template('department/detail.html', department=departments, employees=employees)

# 사원 관련 라우트
@bp.route('/employee')
def list_employee():
    page = request.args.get('page', type=int, default=1)
    # employees = Employee.query.all() #all() 때문에 list 객체로 반환되어 paginate 사용 불가
    employees = Employee.query.order_by(Employee.hire_date.desc()) # paginate 사용하기 위해 변경
    employees = employees.paginate(page=page, per_page=10)
    return render_template('employee/list.html', employees=employees)

@bp.route('/employee/create', methods=['GET', 'POST'])
def create_employee():
    form = EmployeeForm()
    form.dept_code.choices = [(d.dept_code, d.dept_name) for d in Department.query.all()]  # choices 이용해서 사원등록 할 때 부서 보이게

    if form.validate_on_submit():
        existing_emp = Employee.query.filter_by(email=form.email.data).first()
        if existing_emp:
            flash('이미 존재하는 이메일 입니다.', 'danger')
            return render_template('employee/create.html', form=form)
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