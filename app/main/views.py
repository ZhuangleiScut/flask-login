from flask_login import login_required
from . import main


@main.route('/')
@login_required
def index():
    return 'Hello World!'