from flask import Flask
app = Flask(__name__)


@app.route('/')
def index():
    return "Hello nama saya .... npm .... "

@app.route('/aboutme')
def about():
    return "saya suka .... dan .... "

if __name__ == '__main__':
    app.run(debug=True)
 