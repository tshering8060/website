from flask import Flask
app = Flask(__name__)
@app.route('/')
def main_page():
return "<h1>Hello World!</h1>"
@app.route('/square/<x>')
def square(x):
x = int(x)
ans = x * x
return f"{x} ^ 2 = {ans}"
@app.route('/plus/<x>,<y>')
def plus(x,y):
ans = int(x) + int(y)
return f"{x} + {y} = {ans}"