from flask import Flask, request, make_response

app = Flask(__name__)

@app.route("/test/", methods = ["GET", "POST"])
def test():
    if request.method == "GET":
        print(request.headers)
        return str(request.headers) + "<br><br><br>Server runs successfully(maybe). Atleast it can serve this /test"