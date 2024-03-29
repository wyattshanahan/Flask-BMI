
# This code runs the flask application and handles interfacing between python and HTML
# https://blog.pythonanywhere.com/169/#step-1-extract-the-processing-into-a-function
from flask import Flask, request
from calculator import processHost

app = Flask(__name__)
app.config["DEBUG"] = True

@app.route("/", methods=["GET", "POST"])
def calculator():
    errors = ""
    if request.method == "POST":
        weight = None
        heightFt = None
        heightIn = None
        try:
            weight = float(request.form["weight"])
        except:
            errors+= "<p color='red'>{!r} is not a number.</p>\n".format(request.form["weight"])
        try:
            heightFt = float(request.form["heightFt"])
        except:
            errors+= "<p color='red'>{!r} is not a number.</p>\n".format(request.form["heightFt"])
        try:
            heightIn = float(request.form["heightIn"])
        except:
            errors+= "<p color='red'>{!r} is not a number.</p>\n".format(request.form["heightIn"])
        if weight is not None and heightIn is not None and heightFt is not None:
            BMI, category = processHost(weight, heightFt, heightIn)
            BMI = round(BMI,2)
            return '''
                <html>
                    <body>
                        <p>Your BMI is: {BMI}</p>
                        <p> Your BMI category is: {category}</p>
                        <p><a href=".">Click here to calculate again</a>
                    </body>
                </html>
            '''.format(BMI=BMI, category=category)
    return '''
    <html>
        <body>
            {errors}
            <p>Enter your height and weight below:</p>
            <form method="post" action=".">
                <p><b>Height:</b></p>
                <p><input name="heightFt" type="number" min="0" size="6" step=".01"/> Feet</p>
                <p><input name="heightIn" type="number" size="6" step=".01"/> Inches</p>
                <p></p>
                <p><b>Weight:</b></p>
                <p><input name="weight" type="number" min="0" size="6" step=".01"/> Pounds</p>
                <p><input type="submit" value="Calculate!" /></p>
            </form>
        </body>
    </html>
'''.format(errors=errors)

@app.route('/bonjour')
def bonjour():
    return 'Bonjour!'
