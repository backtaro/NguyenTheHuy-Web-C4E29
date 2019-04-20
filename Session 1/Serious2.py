from flask import Flask, render_template
app = Flask(__name__)

users = {
        “huy”:{
                “name” : “Nguyen Quang Huy”,
                “age” : 29
        },
        “tuananh”:{
                “name” : “Huynh Tuan Anh”,
                “age” : 22
        }
}

@app.route('/user/<username>')
def index(usersname):
    return render_template('Serious2.html', users = users)

if __name__ == '__main__':
  app.run(host:'127.0.0.1', port=8000, debug=True)
 