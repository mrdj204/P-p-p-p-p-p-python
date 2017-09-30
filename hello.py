from flask import Flask, render_template, Markup
app = Flask(__name__)

@app.route("/")
def index():
    return "<a href=./lol/>Fckn nerd!</a>"

@app.route('/<string:page_name>/')
def render_static(page_name):
    return render_template('%s.html' % page_name)

@app.route("/users/")
def userpage():
    users = ["Frank", "Steve", "Alice", "Bruce", "Sir Derpenhiemer III"]
    return render_template('user.html', **locals())

@app.route("/chart/")
def chart():
    labels = ["January","February","March","April","May","June","July","August"]
    values = [10,9,8,7,6,4,7,8]
    return render_template('chart.html', values=values, labels=labels)

if __name__ == "__main__":
    app.run(port=80)
