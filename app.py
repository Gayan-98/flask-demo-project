from flask import Flask, render_template

app=Flask(__name__)


@app.route("/hello")
def hello():
    return "hello world"

@app.route("/")
def page1():
    return render_template("test.html")
app.run(debug=True)