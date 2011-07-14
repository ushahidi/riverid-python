from flask import Flask
app = Flask(__name__)

@app.route("/api/signin")
def signin():
    return ""

@app.route("/api/register")
def register():
    return ""

@app.route("/api/emailconfirmation")
def emailconfirmation():
    return ""

@app.route("/api/passwordrecovery")
def passwordrecovery():
    return ""

@app.route("/api/jsonp")
def jsonp():
    return ""

if __name__ == "__main__":
    app.run()
