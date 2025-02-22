# Task Master

A Flask-based Todo List application that helps you manage your daily tasks efficiently. The application features a clean and responsive user interface, SQLite database integration, and follows a modular architecture pattern.

## Features

- Add new tasks
- View all tasks with their creation dates
- Delete completed tasks
- Responsive design for mobile and desktop
- SQLite database persistence
- Clean and intuitive user interface

## Project Structure

```
task master/
├── app.py                  # Main application entry point
├── configs/                # Configuration files
│   ├── appconfig.py       # Application configuration
│   └── dbconfig.py        # Database configuration
├── models/                 # Database models
│   └── TodoListModel.py   # Todo list model definition
├── rest/                   # REST API endpoints
│   └── firstblueprint.py  # API route definitions
├── services/              # Business logic layer
│   └── updatetasks.py     # Task management services
├── static/                # Static files
│   └── css/
│       └── main.css       # Application styling
└── templates/             # HTML templates
    ├── base.html          # Base template
    └── index.html         # Main page template
```

## Technology Stack

- **Python Flask**: Web framework
- **SQLAlchemy**: ORM for database operations
- **SQLite**: Database
- **HTML/CSS**: Frontend interface
- **Jinja2**: Template engine

## Setup Instructions

1. Clone the repository
2. Create a virtual environment:
   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows: venv\Scripts\activate
   ```
3. Install dependencies:
   ```bash
   pip install flask flask-sqlalchemy
   ```
4. Set up the database:
   - The application will automatically create a SQLite database file (notebook.db)
   - You can configure a different database by setting the DATABASE_URL environment variable

5. Run the application:
   ```bash
   python app.py
   ```
   The application will be available at `http://localhost:5000`

## API Endpoints

- `GET /`: Display all tasks
- `POST /`: Create a new task
  - Parameters: `content` (task description)
- `GET/POST /delete/<id>`: Delete a task by ID

## Database Configuration

The application uses SQLite by default. The database configuration can be modified in `configs/appconfig.py`:

```python
SQLALCHEMY_DATABASE_URI = os.environ.get('DATABASE_URL', 'sqlite:///notebook.db')
```

You can override this by setting the `DATABASE_URL` environment variable.

## Usage

1. **Adding a Task**:
   - Enter your task in the input field at the bottom of the page
   - Click "Add Task" or press Enter

2. **Viewing Tasks**:
   - All tasks are displayed in a table format
   - Each task shows its content and creation date

3. **Deleting a Task**:
   - Click the "Delete" link next to any task to remove it

## Styling

The application features a responsive design with:
- Clean and modern interface
- Color-coded actions
- Mobile-friendly layout
- Hover effects for better interaction
- Consistent spacing and typography

## Error Handling

The application includes error handling for:
- Database operations (add/delete tasks)
- Form submissions
- Invalid routes

---

Created by Apurv
