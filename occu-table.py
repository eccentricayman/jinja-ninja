from flask import Flask, render_template

app = Flask(__name__)

@app.route("/")
def occupationsrender():
    OCUPATIONES = {}
    occupashuns = open("occupations.csv", "rU")
    occupashuns.readline()    
    for line in occupashuns:
        if line[0] == "\"":
            #i sincerely apologize for the next line, again
            OCUPATIONES[line[1:line.find("\"", 1, (len(line) + 1))].strip("\n")] = line[line.find(",", line.find("\"", 1, (len(line) + 1)), (len(line))) + 1:len(line)].strip("\n")
        else:
            x = line.split(",")
            OCUPATIONES[x[0].strip("\n")] = x[1].strip("\n")
            
    occupashuns.close()
    return render_template("occupations.html", occudict = OCUPATIONES.items())
            
if __name__ == "__main__":
    app.debug = True
    app.run()
