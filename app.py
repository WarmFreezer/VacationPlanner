from flask import Flask

app = Flask(__name__)

@app.route('/')
def home():
    return "Hello world"

@app.route('/dad')
def dad():
   # Render the page
   return "Hello Dad!"

if __name__ == '__main__':
   # Run the app server on localhost:4449
   app.run('localhost', 4449)