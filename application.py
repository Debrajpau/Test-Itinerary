
from flask import Flask, request, render_template

import json

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])

def index():

    if request.method == 'POST':

        name = request.form['name']

        email = request.form['email']
 
        user_data = {'name': name, 'email': email}
 
        user_json = json.dumps(user_data, indent=4)
 
        with open('user_data.txt', 'w') as file:
 
            file.write(user_json)
 
    return render_template('form.html')
 
if __name__ == '__main__':
 
    app.run(debug=True)
 