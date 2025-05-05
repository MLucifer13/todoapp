# Todosapp

A Django-based todo list application that allows users to manage their personal tasks. Each user can create, update, delete, and mark tasks as complete or incomplete. The app is designed with user authentication and a clean separation of concerns using Django's models, views, forms, and templates.

---

#### Video Demo:  <https://youtu.be/V76nYuwroo0>


## Table of Contents

- [Features](#features)
- [Project Structure](#project-structure)
- [Setup Instructions](#setup-instructions)
- [Full Functionality](#full-functionality)
- [Frontend](#frontend)
- [Usage](#usage)
- [Customization](#customization)
- [Contributing](#contributing)
- [License](#license)

---

## Features

- User registration and authentication (login required for all actions)
- Add, update, and delete tasks
- Toggle task completion status
- View completed and uncompleted task counts
- Each user sees only their own tasks
- Clean, modular Django codebase

---

## Project Structure

```
Todosapp/
│
├── manage.py
├── requirements.txt
├── db.sqlite3
│
├── todoapp/
│   ├── __init__.py
│   ├── admin.py
│   ├── apps.py
│   ├── forms.py
│   ├── migrations/
│   │   └── ... (migration files)
│   ├── models.py
│   ├── tests.py
│   ├── urls.py
│   ├── views.py
│   └── templates/
│       └── todoapp/
│           ├── index.html
│           ├── update_task.html
│           └── delete_task.html
│
├── static/
│   └── ... (CSS, JS, images)
│
└── README.md
```

**Key files and folders:**

- `manage.py`: Django's command-line utility.
- `requirements.txt`: Python dependencies.
- `todoapp/`: Main Django app.
  - `models.py`: Task model definition.
  - `forms.py`: Forms for creating and updating tasks.
  - `views.py`: All view logic (list, create, update, delete, toggle).
  - `urls.py`: URL routes for the app.
  - `templates/todoapp/`: HTML templates for rendering pages.
- `static/`: Static files (CSS, JS, images).

---

## Setup Instructions

1. **Clone the repository:**
   ```bash
   git clone <your-repo-url>
   cd Todosapp
   ```

2. **Create and activate a virtual environment:**
   ```bash
   python -m venv venv
   # On Windows:
   venv\Scripts\activate
   # On macOS/Linux:
   source venv/bin/activate
   ```

3. **Install dependencies:**
   ```bash
   pip install -r requirements.txt
   ```

4. **Apply migrations:**
   ```bash
   python manage.py migrate
   ```

5. **Create a superuser (optional, for admin access):**
   ```bash
   python manage.py createsuperuser
   ```

6. **Run the development server:**
   ```bash
   python manage.py runserver
   ```

7. **Access the app:**
   Open your browser and go to [http://127.0.0.1:8000/](http://127.0.0.1:8000/)

---

## Full Functionality

**Authentication:**
- Users must register and log in to access any todo functionality.
- Each user's tasks are private and only visible to them.

**Task Management:**
- **Add Task:**  
  Users can add a new task using a form on the homepage. Each task is linked to the user who created it.
- **Update Task:**  
  Users can update the title and completion status of their tasks.
- **Delete Task:**  
  Users can delete any of their tasks.
- **Toggle Completion:**  
  Users can mark a task as complete or incomplete with a single click.
- **Task Counts:**  
  The homepage displays the total number of tasks, completed tasks, and uncompleted tasks for the logged-in user.

**Security:**
- All task operations are protected by login requirements.
- Users cannot access or modify tasks belonging to other users.

---

## Frontend

**Technologies Used:**
- **Django Templates:**  
  All HTML pages are rendered using Django's template engine.
- **HTML5 & CSS3:**  
  The UI is built with standard HTML and CSS.  
  You can add your own styles in the `static/` directory.
- **Bootstrap (optional):**  
  You may use Bootstrap by including its CDN in your templates for responsive design and prebuilt components.
- **JavaScript (optional):**  
  For basic interactivity, you can add JS files in the `static/` directory and reference them in your templates.

**Main Templates:**
- `index.html`:  
  Displays the list of tasks, add task form, and task statistics.
- `update_task.html`:  
  Form for editing an existing task.
- `delete_task.html`:  
  Confirmation page for deleting a task.

**How the Frontend Works:**
- The homepage (`index.html`) shows all tasks for the logged-in user, with buttons/links to update, delete, or toggle completion.
- Forms are rendered using Django's form system for consistency and security.
- Static files (CSS, JS, images) are served from the `static/` directory.
- You can customize the look and feel by editing the HTML templates and adding your own CSS/JS.

---

## Usage

- **Register or log in** to your account.
- **Add new tasks** using the form on the homepage.
- **Update or delete tasks** by clicking the corresponding buttons next to each task.
- **Toggle completion status** by clicking the toggle button.
- **View task statistics**: The homepage shows counts of completed and uncompleted tasks.

---

## Customization

- **Templates:**  
  Modify HTML files in `todoapp/templates/todoapp/` to change the UI.
- **Static files:**  
  Add CSS/JS/images to the `static/` directory and reference them in your templates.
- **Models:**  
  Extend `Task` in `models.py` to add more fields (e.g., due date, priority).
- **Views/Forms:**  
  Update logic in `views.py` and `forms.py` to support new features.

---

## Contributing

1. Fork the repository.
2. Create a new branch for your feature or bugfix.
3. Commit your changes.
4. Push to your fork and submit a pull request.

---

## License

This project is for educational purposes.  
Feel free to use and modify it for your own learning or projects.
