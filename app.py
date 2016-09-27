from flask import Flask, render_template
import utils.occupations as occupations
import random

app = Flask(__name__)

@app.route("/")
def occupationsrender():
    return render_template("occupations.html", occudict = occupations.getOccuDict(), randoccu = occupations.getRandOccu(random.randint(0, 24)))

if __name__ == "__main__":
    #app.debug = True
    app.run()
