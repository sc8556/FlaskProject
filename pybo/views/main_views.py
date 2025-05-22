from flask import Blueprint, render_template, url_for
from werkzeug.utils import redirect

from pybo.models import Question

bp = Blueprint('main', __name__, url_prefix='/')

@bp.route('/hello')
def hello_pybo():
    return 'Hello, Pybo!'

@bp.route('/')
def index():
    return redirect(url_for('emp.index_emp'))

# 홈 페이지
@bp.route('/emp')
def index_emp():  # 함수 이름이 'index_emp'이지만 url_for에서는 'index'를 찾고 있음
    return render_template('index.html')

@bp.route('/detail/<int:question_id>/')
def detail(question_id):
    question = Question.query.get_or_404(question_id)
    return render_template('question/question_detail.html', question=question)