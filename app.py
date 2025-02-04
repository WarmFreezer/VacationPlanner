from flask import Flask

app = Flask(__name__)

@app.route('/')
@app.route('/home')
def home():
   # Render the page
   return "Hello Python!"

if __name__ == '__main__':
   # Run the app server on localhost:4449
   app.run('localhost', 4449)