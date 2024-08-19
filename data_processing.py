import urllib

import pandas as pd
from pymongo import MongoClient

class User:
    def __init__(self, age, gender, total_income, expenses):
        self.age = age
        self.gender = gender
        self.total_income = total_income
        self.expenses = expenses

def fetch_data():
    # URL Encode the username and password
    username = urllib.parse.quote_plus("timmyondbeat")
    password = urllib.parse.quote_plus("Hydrogen@2")

    # Setup MongoDB connection
    client = MongoClient(
        f"mongodb+srv://{username}:{password}@survey-app.r3cmbxz.mongodb.net/?retryWrites=true&w=majority&appName=survey-app")
    db = client['surveyDB']
    collection = db['user_data']

    data = list(collection.find())
    return data

def save_to_csv(data):
    df = pd.DataFrame(data)
    df.to_csv('user_data.csv', index=False)

if __name__ == "__main__":
    data = fetch_data()
    save_to_csv(data)
