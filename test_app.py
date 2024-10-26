from flask import Flask

app = Flask(__name__)

@app.route('/')
def hello():
    return "Hello, World!"

if __name__ == '__main__':
    print("Starting the test application...")
    print("Open your web browser and navigate to http://127.0.0.1:5000")
    app.run(debug=True)
