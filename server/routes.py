from flask import Flask, request, make_response, send_from_directory, render_template

app = Flask(__name__)

@app.route("/test/", methods = ["GET", "POST"])
def test():
    if request.method == "GET":
        print(request.headers)
        return str(request.headers) + "<br><br><br>Server runs successfully(maybe). Atleast it can serve this /test"

@app.route("/", methods = ["GET", "POST"])
def landing():
    if request.method == "GET":
        return send_from_directory("../client/dist/Wap", "index.html")
    # return render_template("index.html")