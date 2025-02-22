from flask import Blueprint, request, redirect
from services.updatetasks import *

service_routes = Blueprint('service_routes', __name__)


# Route for adding a new task
@service_routes.route('/', methods=['POST'])
def create_task():
    task_content = request.form.get('content')
    
    add_task(task_content)
    return redirect('/')

# Route for deleting a task by ID
@service_routes.route('/delete/<int:id>', methods=['POST', 'GET'])
def remove_task(id):
    delete_task(id)
    return redirect('/')