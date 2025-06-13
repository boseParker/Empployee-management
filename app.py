from flask import Flask, render_template, request, redirect, url_for
from database import connect
from employee import *

app = Flask(__name__)
connect()  # create DB and table if not exists

@app.route('/')
def home():
    employees = get_all_employees()
    return render_template('index.html', employees=employees)

@app.route('/add', methods=['GET', 'POST'])
def add():
    if request.method == 'POST':
        name = request.form['name']
        email = request.form['email']
        job = request.form['job']
        dept = request.form['department']
        salary = float(request.form['salary'])
        msg = add_employee(name, email, job, dept, salary)
        return render_template('add.html', message=msg)
    return render_template('add.html')

@app.route('/delete/<int:id>')
def delete(id):
    delete_employee(id)
    return redirect(url_for('home'))

@app.route('/update/<int:id>', methods=['GET', 'POST'])
def update(id):
    employee = get_employee_by_id(id)
    if request.method == 'POST':
        name = request.form['name']
        email = request.form['email']
        job = request.form['job']
        dept = request.form['department']
        salary = float(request.form['salary'])
        update_employee(id, name, email, job, dept, salary)
        return redirect(url_for('home'))
    return render_template('update.html', employee=employee)

@app.route('/search', methods=['POST'])
def search():
    keyword = request.form['keyword']
    results = search_employee_by_name(keyword)
    return render_template('index.html', employees=results)

if __name__ == '__main__':
    app.run(debug=True)
