from flask import Flask, request, jsonify
import csv

app = Flask(__name__)

# Data source - CSV file to store tasks
CSV_FILE = 'tasks.csv'

# Function to read tasks from CSV file
def read_tasks():
    tasks = []
    with open(CSV_FILE, 'r') as file:
        reader = csv.DictReader(file)
        for row in reader:
            tasks.append(row)
    return tasks

# Function to write tasks to CSV file
def write_tasks(tasks):
    fieldnames = ['id', 'title', 'completed']
    with open(CSV_FILE, 'w', newline='') as file:
        writer = csv.DictWriter(file, fieldnames=fieldnames)
        writer.writeheader()
        for task in tasks:
            writer.writerow(task)

# Get all tasks
@app.route('/tasks')
def get_tasks():
    tasks = read_tasks()
    return jsonify(tasks)

# Get a task by ID
@app.route('/tasks/<int:task_id>')
def get_task(task_id):
    tasks = read_tasks()
    for task in tasks:
        if int(task['id']) == task_id:
            return jsonify(task)
    return jsonify({'message': 'Task not found'})

# Add a new task
@app.route('/tasks', methods=['POST'])
def add_task():
    tasks = read_tasks()
    task = {
        'id': len(tasks) + 1,
        'title': request.json['title'],
        'completed': False
    }
    tasks.append(task)
    write_tasks(tasks)
    return jsonify({'message': 'Task added successfully'})

# Update a task
@app.route('/tasks/<int:task_id>', methods=['PUT'])
def update_task(task_id):
    tasks = read_tasks()
    for task in tasks:
        if int(task['id']) == task_id:
            task['title'] = request.json.get('title', task['title'])
            task['completed'] = request.json.get('completed', task['completed'])
            write_tasks(tasks)
            return jsonify({'message': 'Task updated successfully'})
    return jsonify({'message': 'Task not found'})

# Delete a task
@app.route('/tasks/<int:task_id>', methods=['DELETE'])
def delete_task(task_id):
    tasks = read_tasks()
    for task in tasks:
        if int(task['id']) == task_id:
            tasks.remove(task)
            write_tasks(tasks)
            return jsonify({'message': 'Task deleted successfully'})
    return jsonify({'message': 'Task not found'})

# Mark a task as complete/incomplete
@app.route('/tasks/<int:id>/complete', methods=['PUT'])
def complete_task(id):
    tasks = load_tasks_from_csv()
    task = next((t for t in tasks if t['id'] == id), None)
    if not task:
        abort(404, description=f"Task with id {id} not found")
    task['completed'] = True
    save_tasks_to_csv(tasks)
    return jsonify({'message': f"Task with id {id} marked as complete"})

@app.route('/tasks/<int:id>/incomplete', methods=['PUT'])
def incomplete_task(id):
    tasks = load_tasks_from_csv()
    task = next((t for t in tasks if t['id'] == id), None)
    if not task:
        abort(404, description=f"Task with id {id} not found")
    task['completed'] = False
    save_tasks_to_csv(tasks)
    return jsonify({'message': f"Task with id {id} marked as incomplete"})


if __name__ == '__main__':
    app.run(debug=True)
