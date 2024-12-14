from flask import Flask  #flask module, Flask library

app = Flask(__name__)


@app.route("/")  #register route
def hello_world():
  return "Hello, Worlds!"


if __name__ == "__main__":
  app.run(host='0.0.0.0', debug=True)
