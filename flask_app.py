
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
            <html lang="en">
            <head>
            <meta name="viewport" content="width=device-width">
            <meta name="author" content="Wyatt Shanahan">
            </head>
            <body style="background-color:#323232;color:#f4a529">
        <h1 style="font-family:Avantgarde,TeX Gyre Adventor,URW Gothic L,sans-serif;left:30%;position:absolute;display:inline-block;color:#f4a529;text-align:center;background-image:linear-gradient(to left,#186118,#3eb489,#186118);border-radius:25px;font-style: oblique;"> ⠀⠀ BMI Calculator ⠀⠀ </h1>
                <section id="output" style="left:33%;position:absolute;font-family:Avantgarde,TeX Gyre Adventor,URW Gothic L,sans-serif">
                <p>  ⠀⠀ </p>
                <h3>Your BMI is: <b>{BMI}</b></h3>
                <p> Your BMI category is: {category}</p>
                <p><a style="color:lime" href=".">Click here to calculate again</a>
                </section>
                </body>
                </html>
            '''.format(BMI=BMI, category=category)
    return '''
    <html lang="en">
        <head>
            <meta name="viewport" content="width=device-width">
            <meta name="author" content="Wyatt Shanahan">
        </head>
        <body style="background-color:#323232;color:#f4a529">
            {errors}
        <h1 style="font-family:Avantgarde,TeX Gyre Adventor,URW Gothic L,sans-serif;left:30%;position:absolute;display:inline-block;color:#f4a529;text-align:center;background-image:linear-gradient(to left,#186118,#3eb489,#186118);border-radius:25px;font-style: oblique;"> ⠀⠀ BMI Calculator ⠀⠀ </h1>
            <section id="input" style="left:33%;position:absolute;font-family:Avantgarde,TeX Gyre Adventor,URW Gothic L,sans-serif">
            <p> ⠀⠀  </p>
            <p><i><b>Enter your height and weight below:</b></i></p>
            <form method="post" action=".">
                <p><b>Height:</b></p>
                <p><input name="heightFt" type="number" min="0" size="6" step=".01" required/> Feet</p>
                <p><input name="heightIn" type="number" min="0" max="11" size="6" step=".01" required/> Inches</p>
                <p></p>
                <p><b>Weight:</b></p>
                <p><input name="weight" type="number" min="0" size="6" step=".01" required/> Pounds</p>
                <p><input type="submit" value="Calculate!" /></p>
            </form>
        </style>
        </body>
    </html>
'''.format(errors=errors)

@app.route('/bonjour')
def bonjour():
    return 'Bonjour!'
