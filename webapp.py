from flask import Flask
from flask import render_template
from flask import request



app = Flask(__name__)
@app.route("/")
def landing_page():
    context = {'project': "flask-bootstrap", 'author': "Anubhav Sinha", 'items':["python", "flask", "jinja2", "bootstrap", "font-awesome", "jquery"] }
    return render_template('landing_page.html', **context)


if __name__ == "__main__":
    app.run(debug=True, host='0.0.0.0', port=80)
