#Flask 설정 파일
import os #운영체게 관련 기능을 사용하기 위한 모듈

#현재 이 config.py 파일이 위치한 폴더 경로를 기준으로 SQLite 데이터베이스 파일 경로 설정
BASE_DIR = os.path.dirname(__file__)
SQLALCHEMY_DATABASE_URI = f"sqlite:///{os.path.join(BASE_DIR, 'pybo.db')}"
SQLALCHEMY_TRACK_MODIFICATIONS = False # 이벤트 시스템 사용 안함
SECRET_KEY = "jay"