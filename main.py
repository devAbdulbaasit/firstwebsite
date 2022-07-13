import csv
from flask import Flask, render_template, request, redirect

app = Flask(__name__)

@app.route("/")
def hello_world():
    return render_template('index.html')

@app.route('/<string:page_name>')
def hello(page_name):
    return render_template(page_name)

def wtcsv(data):
    with open('database.csv', newline='', mode='a') as database:
        name = data["name"]
        email = data["email"]
        message = data["message"]
        csv_writer = csv.writer(database, delimiter=',', quotechar='"', quoting=csv.QUOTE_MINIMAL)
        csv_writer.writerow([name, email, message])

@app.route('/submit', methods=['POST', 'GET'])
def submit():
    if request.method == 'POST':
        data = request.form.to_dict()
        wtcsv(data)
        return redirect('tanks.html')
    else:
        return 'something went wrong, pls try again'


app.run(debug=True)
