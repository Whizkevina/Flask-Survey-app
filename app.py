import urllib
from flask import Flask, render_template, request, redirect, url_for
from pymongo import MongoClient


app = Flask(__name__)

# URL Encode the username and password
username = urllib.parse.quote_plus("timmyondbeat")
password = urllib.parse.quote_plus("Hydrogen@2")

# Setup MongoDB connection
client = MongoClient(f"mongodb+srv://{username}:{password}@survey-app.r3cmbxz.mongodb.net/?retryWrites=true&w=majority&appName=survey-app")

db = client['surveyDB']
collection = db['user_data']

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/submit', methods=['POST'])
def submit():
    if request.method == 'POST':
        user_data = {
            'age': request.form['age'],
            'gender': request.form['gender'],
            'total_income': request.form['total_income'],
            'expenses': {
                'utilities': request.form.get('utilities', 0),
                'entertainment': request.form.get('entertainment', 0),
                'school_fees': request.form.get('school_fees', 0),
                'shopping': request.form.get('shopping', 0),
                'healthcare': request.form.get('healthcare', 0)
            }
        }
        print(user_data)
        collection.insert_one(user_data)
        # Redirect to thank you page
        return redirect(url_for('thank_you'))
    return render_template('index.html')

@app.route('/thank-you')
def thank_you():
    return render_template('thank_you.html')

if __name__ == '__main__':
    app.run(debug=True)
