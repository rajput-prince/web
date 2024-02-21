from flask import Flask, render_template, request
from pymongo import MongoClient

app = Flask(__name__)

client = MongoClient('mongodb://localhost:27017')
db = client['prince']
collection = db['student']

@app.route('/')
def index():
    # documents = collection.find()
    # return render_template('index.html', documents=documents)

    return render_template('index.html')
@app.route('/Register', methods=['POST'])
def submit_form():
    user_name = str(request.form.get('user_name'))
    user_email = request.form.get('user_email')
    user_mobile = request.form.get('user_mobile')
    user_address = request.form.get('user_address')

    data_to_insert = {
        "Name": user_name,
        "Email": user_email,
        "Phone no": user_mobile,
        "Address": user_address
    }

    result = collection.insert_one(data_to_insert)

    return f"Data inserted Succesfully with ID: {result.inserted_id}"

if __name__ == '__main__':
    app.run(debug=True) 