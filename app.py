# cSpell:disable
from flask import Flask, render_template, request
from random import random
import numpy, cv2, os
from datetime import datetime
from zipfile import ZipFile

app = Flask(__name__)
name_list = []





@app.route("/alnum-calc", methods=["GET", "POST"])
def alphanum_calculator():
    if request.method == "GET":
        return render_template("alnum_calc.html")
    if request.method == "POST":
        expression = request.form.get('expression')
        try:
            binnary = ''.join(format(ord(caractere), '08b') for caractere in expression)
            size = len(binnary)
            separator = 480
            array_2d = [[binnary[n:n + separator]] for n in range(0, size, separator) if n < size]
            mensage = False
        except:
            mensage = True
            binnary = None
        return render_template("alnum_calc.html", binnary=array_2d, mensage=mensage)



if __name__ == '__main__':
#    app.run(host='0.0.0.0', debug = True)
   app.run(debug = True)