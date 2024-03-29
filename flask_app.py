
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
                    <body id="main">
                        <h1 style="font-family:Avantgarde,TeX Gyre Adventor,URW Gothic L,sans-serif;left:30%;position:absolute;display:inline-block;color:#f4a529;text-align:center;background-image:linear-gradient(to left,#186118,#3eb489,#186118);border-radius:25px;font-style: oblique;"> ⠀⠀ BMI Calculator ⠀⠀ </h1>
                        <p> ⠀⠀  </p>
                        <p>  ⠀⠀ </p>
                        <h2>Your BMI is: <b>{BMI}</b></h2>
                        <p> Your BMI category is: {category}</p>
                        <p><a href=".">Click here to calculate again</a>
                    </body>
                </html>
            '''.format(BMI=BMI, category=category)
    return '''
    <html>
        <body id="main">
            {errors}
            <h1 style="font-family:Avantgarde,TeX Gyre Adventor,URW Gothic L,sans-serif;left:30%;position:absolute;display:inline-block;color:#f4a529;text-align:center;background-image:linear-gradient(to left,#186118,#3eb489,#186118);border-radius:25px;font-style: oblique;"> ⠀⠀ BMI Calculator ⠀⠀ </h1>
            <p> ⠀⠀  </p>
            <p>  ⠀⠀ </p>
            <p>Enter your height in Feet/Inches and your weight in Pounds:</p>
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
