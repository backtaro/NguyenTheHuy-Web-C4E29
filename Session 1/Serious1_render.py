from flask import Flask, render_template
app = Flask(__name__)

@app.route('/bmi/<int:x>/<int:y>')
def bmi(x, y):
    bmi_cal = x*10000/(y*y)
    return render_template('Serious1.html', bmi_cal = bmi_cal)

if __name__ == '__main__':
  app.run(debug=True)