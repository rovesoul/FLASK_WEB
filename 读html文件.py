from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def index(name):
   return render_template('hello.html',name="abcd" )  # 从templates中找到


if __name__ == '__main__':
    app.run(debug = True)