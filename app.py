from flask import Flask, render_template, request, redirect, url_for
from datetime import datetime

app = Flask(__name__)

reminders = []

@app.route('/')
def index():
    return render_template('index.html', reminders = reminders)

@app.route('/add', methods = ['GET', 'POST'])
def add_reminder():
    if request.method == 'POST':
        title = request.form['title']
        description = request.form.get('description')
        due_date = datetime.strptime(request.form['due_date'], '%Y-%m-%d %H:%M:%S')
        new_reminder = {'title': title, 'description': description, 'due_date': due_date}
        reminders.append(new_reminder)
        return redirect(url_for('index'))
    return render_template('add_reminder.html')

@app.route('/delete/<int:index>')
def delete_reminder(index):
    if 0 <= index < len(reminders):
        del reminders[index]
    return redirect(url_for('index'))

if __name__ == '__main__':
    app.run(debug=True)
