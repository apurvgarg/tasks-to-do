from flask import Flask, redirect, render_template
from rest.firstblueprint import service_routes
from models.TodoListModel import TodoList 
from configs import appconfig, dbconfig

app = Flask(__name__)
app.config.from_object(appconfig.Config)

# Initialize the db with the app (db object now contains configuration)
dbconfig.db.init_app(app)

with app.app_context():
    dbconfig.db.create_all()

app.register_blueprint(service_routes)

# Route for displaying the tasks
@app.route('/', methods=['GET'])
def index():
    tasks = TodoList.query.order_by(TodoList.date_created).all()
    return render_template('index.html', tasks=tasks)

if __name__ == "__main__":
    app.run(debug=True)
