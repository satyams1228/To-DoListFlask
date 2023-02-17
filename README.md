# To-DoListFlask

TODO List Application

This is a Flask application that allows users to create, update, and delete tasks in a TODO list.

Prerequisites

To run this application, you will need:

Python 3

Flask


Installing Dependencies

To install the dependencies for this application, run the following command:

pip install -r requirements.txt



Running the Application

To run the application, navigate to the project directory and run the following command:

python app.py





The application will be available at http://localhost:5000/ in your web browser.

API Endpoints

GET /tasks: returns a list of all tasks

GET /tasks/<id>: returns a single task with the specified ID

POST /tasks: creates a new task

PUT /tasks/<id>: updates a task with the specified ID

DELETE /tasks/<id>: deletes a task with the specified ID

PUT /tasks/<id>/complete: marks a task as complete

PUT /tasks/<id>/incomplete: marks a task as incomplete


Use Postman to check

