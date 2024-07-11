from db.db_init import db  

class Question(db.Model):
    __tablename__ = 'questions'  
    __table_args__ = {'schema': 'data'}
    id = db.Column(db.Integer, primary_key=True)
    question = db.Column(db.Text)
    answer = db.Column(db.Text)
