from flask import Flask, url_for, render_template

app = Flask(__name__)


@app.route('/')
def index():
    return render_template('index.html', url=url_for('show', message='it is staaaaaaas'))

@app.route('/show/<string:message>')
def show(message: str):
    return message


if __name__ == '__main__':
    app.run()