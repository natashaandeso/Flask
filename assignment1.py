# create a route that is able to calculate the simple interest given the pricipal as 20000, rate as 7% and time as 8 years.
# import the flask framework
from flask import *


# Below will create a web server based application
app = Flask(__name__)


@app.route("/api/calc", methods=["POST"])
def calculator():
    if request.method == "POST":
        principal = request.form["principal"]
        rate = request.form["rate"]
        time = request.form["time"]
        simpleintrest = int(principal )* int(rate) * int(time) / 100

        return jsonify({"The answer is ": simpleintrest})
    


# below will run the application
app.run(debug=True)
