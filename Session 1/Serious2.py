from flask import Flask, render_template
app = Flask(__name__)

user = {
        'huy':{
                'name' : 'Nguyen Quang Huy',
                'age' : 29
        },
        'tuananh':{
                'name' : 'Huynh Tuan Anh',
                'age' : 22
        }
}

@app.route('/user/<username>')
def index(username):
    for i in user.keys():
        if username in user.keys():
            user_result = user[i]
        else:
            user_result = "User not found"
    return render_template('Serious2.html', user_result = user_result)

if __name__ == '__main__':
  app.run(debug=True)
 