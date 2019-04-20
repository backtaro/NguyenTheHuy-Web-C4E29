from flask import Flask
app = Flask(__name__)

@app.route('/bmi/<int:x>/<int:y>')
def bmi(x, y):
    bmi_cal = x*10000/(y*y)
    
    if bmi_cal < 16:
        result = "Severely underweight"
    elif 16 <= bmi_cal <18.5:
        result = "Underweight"
    elif 18.5<= bmi_cal < 25:
        result = "Normal"
    elif 25 <= bmi_cal < 30:
        result = "Overweight"
    else:
        result = "Obese"

    return '{} - {}'.format(bmi_cal,result)

if __name__ == '__main__':
  app.run(debug=True)
 