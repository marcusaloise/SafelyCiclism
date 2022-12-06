from flask import Flask, render_template, request
import json

app = Flask(__name__)
app.config['SECRET_KEY'] = 'my_pass'

@app.route("/", methods=('GET', 'POST'))
def index():
    if request.method == 'POST':
        with open("data.json", "r") as read_file:
            data = json.load(read_file)

        id = len(data) + 1
        date = request.form['date']
        email = request.form['email']
        name = request.form['name']
        topic = request.form['topic']
        message = request.form['message']

        newData = {
            'id': id,
            'date': date,
            'email': email,
            'name': name,
            'topic': topic,
            'message': message
        }

        data.append(newData)

        with open("data.json", "w") as write_file:
                    json.dump(data, write_file)

    return render_template('index.html')