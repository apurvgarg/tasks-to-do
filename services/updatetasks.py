from configs.dbconfig import db
from models.TodoListModel import TodoList

def add_task(task_content):
    new_task = TodoList(content=task_content)
    
    try:
        db.session.add(new_task)
        db.session.commit()
    except Exception as e:
        print(e)
        db.session.rollback()

# Function to delete a task by ID
def delete_task(task_id):
    task_to_delete = TodoList.query.get(task_id)

    try:
        db.session.delete(task_to_delete)
        db.session.commit()
    except Exception as e:
        print(e)
        db.session.rollback()