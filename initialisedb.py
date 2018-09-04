from todo.app import db
from todo.models import User, Task
import os

if bool(os.environ.get('DEBUG', '')):
    db.drop_all()

db.create_all()

user = User()
user.username="sebastian"
user.email="sebastian@test.local"
user.password="thisshouldnotbeplaintext"


db.session.add(user)
db.session.commit()

