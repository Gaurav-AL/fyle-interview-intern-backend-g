from flask import jsonify
from marshmallow.exceptions import ValidationError
from core import app
from core.apis.assignments.student import student_assignments_resources
from core.apis.assignments.teacher import teacher_assignments_resources

from core.libs import helpers
from core.libs.exceptions import FyleError


app.register_blueprint(student_assignments_resources, url_prefix='/student')
app.register_blueprint(teacher_assignments_resources,url_prefix='/teacher')


@app.route('/')
def ready():
    response = jsonify({
        'status': 'ready',
        'time': helpers.get_utc_now()
    })
    return response

@app.errorhandler(Exception)
def handle_error(err):
    print(err)
    if isinstance(err, FyleError):
        return jsonify(
            error=err.__class__.__name__, message=err.message
        ), err.status_code
    elif isinstance(err, ValidationError):
        return jsonify(
            error=err.__class__.__name__, message=err.messages
        ),400
    raise err


