from flask import Flask,render_template
import os

application = Flask(__name__)
application.secret_key = os.urandom(24)

@application.route("/")
def First_view():
    return render_template("test.html")
if __name__ == '__main__':
    application.run("0.0.0.0",5000)