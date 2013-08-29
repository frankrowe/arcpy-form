from flask import Flask, render_template, request
app = Flask(__name__)



# Home page (localhost:5000)
@app.route("/")
def hello(name=None):
  return render_template('form.html', name=name)



# Form submit (localhost:5000/submit)
@app.route('/submit', methods=['POST'])
def submitForm():
  value1 = request.form['value1']
  value2 = request.form['value2']

  # do cool GIS things with form values here

  return render_template('success.html', value1=value1, value2=value2)



if __name__ == "__main__":
  app.run()