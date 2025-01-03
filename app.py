from flask import Flask, render_template
import requests

app = Flask(__name__)

@app.route('/')
def fetch_users():
    response = requests.get('https://randomuser.me/api/?results=30')
    data = response.json()

    users = [
        {
            'name': f"{item['name']['first']} {item['name']['last']}",
            'email': item['email'],
            'country': item['location']['country']
        }
        for item in data['results']
    ]

    return render_template('user_list.html', users=users)

if __name__ == '__main__':
    app.run(debug=True)

