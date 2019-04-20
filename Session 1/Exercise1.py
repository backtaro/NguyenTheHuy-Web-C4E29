from flask import Flask, render_template, redirect
app = Flask(__name__)

personal_info = [
{
    "Name":"Huy Nguyen",
    "DOB":"30.05.92",
    "Age":"26",
    "Eyes": "Brown",
    "Blood": "O+",
    "Work":"Citibank",
    "School":"Univeristy of Washington",
    "Hobbies":"Gym, Tennis, Traveling",
}
]

@app.route('/about-me')
def info():
    return render_template('Exercise1.html', personal_info = personal_info)

@app.route('/school')
def hello():
    return redirect("http://techkids.vn", code=302)

if __name__ == '__main__':
  app.run(debug=True)
 