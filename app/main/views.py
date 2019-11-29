from flask_login import login_required
from . import main


@main.route('/')
@login_required
def hello_world():
    return 'Hello World!'